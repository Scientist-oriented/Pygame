import pygame

import random

############################################################################
# 0. 반드시 해야하는 것들
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("Won Game") # 게임 이름

# FPS
clock = pygame.time.Clock()

###############################################################################
# 1. 사용자 게임 초기 (배경화면, 게임이미지, 자표, 폰트 등)

# 배경 이미지 불러오기
opening = pygame.image.load("C:\\Users\\User\\Desktop\pygame\\evading_Joon\\resources\\opening.png")
background = pygame.image.load("C:\\Users\\User\\Desktop\pygame\\evading_Joon\\resources\\background.png")
gameover = pygame.image.load("C:\\Users\\User\\Desktop\pygame\\evading_Joon\\resources\\gameover.png")

# 캐릭터(스프라이트) 불러오기
charactor = pygame.image.load("C:\\Users\\User\\Desktop\pygame\\evading_Joon\\resources\\charactor.png")

# 캐릭터가 움직이기 위한 작업
charactor_size = charactor.get_rect().size
chraractor_width = charactor_size[0]
chraractor_height = charactor_size[1]


# 이동할 좌표
to_x = 0
to_y = 0

# 적 캐릭터 3명
enemy1 = pygame.image.load("C:\\Users\\User\\Desktop\pygame\\evading_Joon\\resources\\enemy.png")
enemy1_size = enemy1.get_rect().size
enemy1_width = enemy1_size[0]
enemy1_height = enemy1_size[1]


enemy2 = pygame.image.load("C:\\Users\\User\\Desktop\pygame\\evading_Joon\\resources\\enemy.png")
enemy2_size = enemy2.get_rect().size
enemy2_width = enemy2_size[0]
enemy2_height = enemy2_size[1]


enemy3 = pygame.image.load("C:\\Users\\User\\Desktop\pygame\\evading_Joon\\resources\\enemy.png")
enemy3_size = enemy3.get_rect().size
enemy3_width = enemy3_size[0]
enemy3_height = enemy3_size[1]


# 이동속도
charactor_speed = 0.75

# 적 캐릭터 이동 변수
enemy_Drop = 0.5

# 텍스트 입력
game_font = pygame.font.Font(None, 50) # 폰트 객체를 생성함 (폰트와 크기)


# 오프닝 화면
running = "opening"

########################################################################################
# 2. 이벤트 루프 (이벤트 루프를 돌고 있는 동안 게임은 꺼지지 않음)

while True:
    while running == "opening":
        dt = clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_ticks = pygame.time.get_ticks()
                    running = "ongame"

                    # 게임 초기 설정을 다 해주어야 함
                    enemy1_x_pos = 0
                    enemy1_y_pos = 0

                    enemy2_x_pos = 230
                    enemy2_y_pos = 50

                    enemy3_x_pos = 340
                    enemy3_y_pos = 100

                    charactor_x_pos = (screen_width - chraractor_width) / 2
                    charactor_y_pos = screen_height - chraractor_height

                    to_x = 0
        screen.blit(opening, (0,0))
        pygame.display.update()

    while running == "ongame":
        dt = clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # 2-1. 키보드 입력 (캐릭터 이동)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_x -= charactor_speed
                elif event.key == pygame.K_RIGHT:
                    to_x += charactor_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0

        # 2-2. 게임캐릭터 이동 위치 정의
        charactor_x_pos += to_x * dt
        charactor_y_pos += to_y * dt

        # 적 캐릭터 이동
        enemy1_y_pos += enemy_Drop * dt
        enemy2_y_pos += enemy_Drop * dt
        enemy3_y_pos += enemy_Drop * dt

        # 맨 밑에 내려오면 재생성

        if enemy1_y_pos > 640:
            enemy1_y_pos = 0
            enemy1_x_pos = random.randrange(1,590)
        if enemy2_y_pos > 640:
            enemy2_y_pos = 0
            enemy2_x_pos = random.randrange(1,590)
        if enemy3_y_pos > 640:
            enemy3_y_pos = 0
            enemy3_x_pos = random.randrange(1,590)


        # 경계값 처리 (캐릭터가 화면 밖으로 나가는 것을 방지)

        if charactor_x_pos < 0:
            charactor_x_pos = 0
        elif charactor_x_pos > screen_width - chraractor_width:
            charactor_x_pos = screen_width - chraractor_width

        # 2-3. 충돌 처리
        charactor_rect = charactor.get_rect()
        charactor_rect.left = charactor_x_pos
        charactor_rect.top = charactor_y_pos

        enemy1_rect = enemy1.get_rect()
        enemy1_rect.left = enemy1_x_pos
        enemy1_rect.top = enemy1_y_pos

        enemy2_rect = enemy2.get_rect()
        enemy2_rect.left = enemy2_x_pos
        enemy2_rect.top = enemy2_y_pos

        enemy3_rect = enemy3.get_rect()
        enemy3_rect.left = enemy3_x_pos
        enemy3_rect.top = enemy3_y_pos

        if charactor_rect.colliderect(enemy1_rect):
            running = "gameover"
            end_ticks = pygame.time.get_ticks()

        if charactor_rect.colliderect(enemy2_rect):
            running = "gameover"
            end_ticks = pygame.time.get_ticks()

        if charactor_rect.colliderect(enemy3_rect):
            running = "gameover"
            end_ticks = pygame.time.get_ticks()

        # 적 이동


        # 2-4. 타이머 집어 넣기
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        timer = game_font.render(str(round(elapsed_time, 2)), True, (0, 0, 0))


        # 15초 마다 스테이지 설정

        if elapsed_time < 5:
            enemy_Drop = 0.5
            stage = game_font.render("      Stage 1", True, (0, 0, 0))

        if 5 <= elapsed_time < 10:
            enemy_Drop = 0.6
            stage = game_font.render("      Stage 2", True, (0, 0, 0))

        if 10 <= elapsed_time < 15:
            enemy_Drop = 0.7
            stage = game_font.render("      Stage 3", True, (0, 0, 0))

        if 15 <= elapsed_time < 20:
            enemy_Drop = 0.8
            stage = game_font.render("      Stage 4", True, (0, 0, 0))

        if 25 <= elapsed_time < 30:
            enemy_Drop = 0.9
            stage = game_font.render("      Stage 5", True, (0, 0, 0))

        if elapsed_time > 30:
            enemy_Drop = 1
            stage = game_font.render("Final Stage", True, (0, 0, 0))


        # 2-5. 스크린에 구현
        screen.blit(background, (0,0))
        screen.blit(charactor, (charactor_x_pos, charactor_y_pos))
        screen.blit(enemy1, (enemy1_x_pos, enemy1_y_pos))
        screen.blit(enemy2, (enemy2_x_pos, enemy2_y_pos))
        screen.blit(enemy3, (enemy3_x_pos, enemy3_y_pos))
        screen.blit(timer, (10, 10))
        screen.blit(stage, (290, 10))


        # 2-6. 화면 업데이트는 필수요소
        pygame.display.update()

    # 게임이 꺼지기 전에 게임오버 화면 보여주기
    while running == "gameover":
        dt = clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_ticks = pygame.time.get_ticks()
                    running = "opening"

        score_time = (end_ticks - start_ticks) / 1000
        score = game_font.render(str(round(score_time, 2)), True, (0, 0, 0))

        screen.blit(gameover, (0,0))
        screen.blit(score, (10, 10))
        pygame.display.update()
