import math
import random

import pygame
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Nitin's Game")
icon = pygame.image.load('cargo-ship.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 420
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 8

for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(50)

bulletImg = pygame.image.load('bullet.png')
bulletX = playerX
bulletY = 420
# bulletX_change = 0.1
bulletY_change = 10
bullet_state = 'ready'

backgroundImg = pygame.image.load('background.jpg')
mixer.music.load('background.wav')
mixer.music.play(-1)


def player(x, y, ):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def bullet_fire(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))


def iscollison(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

name_font  = pygame.font.Font('nitin_text.ttf',24)
def show_author():
    name = name_font.render("Made By Nitin Singh",True,(255,255,255))
    screen.blit(name,(500 , 20))

def show_score():
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (10, 10))


game_over_font  = pygame.font.Font('nitin_text.ttf',60)
def game_over_text():
    game_over = game_over_font.render("Game Over", True, (255, 255, 255))
    screen.blit(game_over, (250, 250))



running = True
while running:
    screen.fill((244, 0, 250))
    screen.blit(backgroundImg, (0, 0))
    # playerX += 0.1
    # if playerX > 880:
    #     playerX = 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    bullet_fire(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    for i in range(num_of_enemy):
        enemyX[i] += enemyX_change[i]

        if enemyY[i] > 350:
            for j in range(num_of_enemy):
                enemyY[j] = 1000
            game_over_text()
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        if enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
        collison = iscollison(enemyX[i], enemyY[i], bulletX, bulletY)
        if collison:
            collision_sound = mixer.Sound('explosion.wav')
            collision_sound.play()
            bulletY = 420
            bullet_state = 'ready'
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    if bullet_state == 'fire':
        bullet_fire(bulletX, bulletY)
        bulletY -= 2

    if bulletY < 0:
        bulletY = 420
        bullet_state = 'ready'

    player(playerX, playerY)
    show_score()
    show_author()
    pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400))
    pygame.display.update()



