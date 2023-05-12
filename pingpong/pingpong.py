import pygame, random

pygame.init()

red = [100,240,255]
lBlue = [100,240,255]

screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Surface")
screen.fill(lBlue)

clock = pygame.time.Clock()

posX, posY = 0, 370
speedX, speedY = 3, 4
directionX, directionY = 0, 0
gameover = False

player = pygame.Rect(posX, posY, 120, 120)
playerImage = pygame.image.load("R.png")
playerImage = pygame.transform.scale(playerImage, [player.width, player.height])

enemyCounter = 0
totalEnemies = 100
score = 0

enemies = {}
def check_collision(enemyRect, score):
    global enemies
    if player.colliderect(enemyRect):
        if enemyImageName == "bee.png":
            score -= 1
        elif enemyImageName == "ch.png":
            score += 1
        enemies[enemyImageName].remove(enemyRect)
    return score

while not gameover:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RIGHT:
                 directionX = "move_right"
             elif event.key == pygame.K_LEFT:
                  directionX = "move_left"
        elif event.type == pygame.KEYUP:
            if event.type == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                speedX = 0
    if directionX == "move_left":
        if posX > 0:
            posX -= 3
    elif directionX == "move_right":
        if posX + 30 < screenX:
            posX += 3
    player = pygame.Rect(posX, posY, 120, 140)
    screen.blit(playerImage, player)

    posX += speedX

    if posX >= screenX - playerImage.get_rect().width or posX <= 0:
        speedX = -speedX

    enemyCounter += 1
    if enemyCounter >= totalEnemies:
        enemyCounter = 0
        enemyImageName = "ch.png" if random.randint(1, 2) == 1 else "bee.png"
        enemyImage = pygame.image.load(enemyImageName)
        enemyImage = pygame.transform.scale(enemyImage, [60, 73])
        enemyCoords = [random.randint(0, screenX - 100), random.randint(0, screenY - 100), 60, 73]
        if enemyImageName not in enemies:
            enemies[enemyImageName] = []
        enemies[enemyImageName].append(pygame.Rect(enemyCoords))
        
    for enemyImageName, enemyRects in enemies.items():
        enemyImage = pygame.image.load(enemyImageName)
        enemyImage = pygame.transform.scale(enemyImage, [60, 73])
        for enemyRect in enemyRects[:]:
            if player.colliderect(enemyRect):
                if enemyImageName == "bee.png":
                    score -= 1
                elif enemyImageName == "ch.png":
                    score += 1
        enemies[enemyImageName].remove(enemyRect)
            enemyRect.top += 1  # сдвигаем врагов на 1 пиксель вниз
            screen.blit(enemyImage, enemyRect)
        ruut = pygame.draw.rect(screen, red, [posX, posY, 30, 30])

    pygame.display.flip()
    screen.fill(lBlue)

    print(score)
    if score == 20:
      gameover = True

pygame.quit()
