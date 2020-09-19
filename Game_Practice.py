import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
    # "screen =" 써줄 것! -> 스택오버플로우에서 배움

# 화면 타이틀 설정
pygame.display.set_caption("Won Game") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\User\\Desktop\\pygame\\background.png")
    # 역슬러시를 2개로 바꾸어주거나 슬러시로 바꾸어주어야 함.

# 캐릭터(스프라이트) 불러오기
charactor = pygame.image.load("C:\\Users\\User\\Desktop\\pygame\\charactor.png")

# 캐릭터가 움직이기 위한 작업
charactor_size = charactor.get_rect().size
    # 캐릭터 사이즈를 튜플로 저장하는 함수임
    # charactor_size를 출력을 해보면 (50, 100)으로 나옴
chraractor_width = charactor_size[0]
    # charactor_size[0] -> 캐릭터 사이즈의 가로 좌표를 의미
chraractor_height = charactor_size[1]
    # charactor_size[1] -> 캐릭터 사이즈의 세로 좌표를 의미
charactor_x_pos = (screen_width - chraractor_width) / 2
    # 최초의 가로 포지션이 화면 한가운데 있음.
    # 정중앙에 오게 하려면 캐릭터 크기도 계산을 해야 함.
charactor_y_pos = screen_height - chraractor_height
    # 최초의 세로 포지션이 화면 제일 아래에 있음.
    # 캐릭터 높이를 빼주는 이유는 구현이 시작되는 위치 기준이기 때문

# 이동할 좌표
to_x = 0
to_y = 0

# cnt = 0 -> running의 원리를 이해하기 위해 임시로

# 적 캐릭터
enemy = pygame.image.load("C:\\Users\\User\\Desktop\\pygame\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width - enemy_width) / 2
enemy_y_pos = screen_height - enemy_height

# 이동속도
charactor_speed = 0.5

# 이벤트 루프 (이벤트 루프를 돌고 있는 동안 게임은 꺼지지 않음)

running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30)
        # 게임화면의 초당 프레임수 설정 (dt는 이동속도를 제어하기 위한 변수임)
        # 초당 tick이 30번
    # print("fps: "+ str(clock.get_fps())) #fps를 출력할 수 있음

    # 캐릭터의 이동 거리를 고정값으로 하면 fps를 적게할 수록 느리게 이동함.
        # 왜냐면 fps는 초당 동작이 실행되는 횟수를 의미하기 때문
        # 따라서 고정값으로 하면 안됨 (프레임 별로 게임 속도가 달라지면 안되기 때문)

    for event in pygame.event.get(): # 이벤트(키보드나 마우스의 입력을 받고 있는 상황을 의미함.)가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하면 종료 (윈도우 창 닫기 클릭)
            running = False

        # 키보드 입력 (캐릭터 이동)
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인 (down이 아래가 아니라 눌렀다는 뜻)
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽 방향으로
                to_x -= charactor_speed #
            elif event.key == pygame.K_RIGHT: # 캐릭터 오른쪽으로
                to_x += charactor_speed
            elif event.key == pygame.K_UP: # 캐릭터 위로
                to_y -= charactor_speed
            elif event.key == pygame.K_DOWN: # 캐릭터 아래로
                to_y += charactor_speed

        if event.type == pygame.KEYUP: # 키가 떼어졌는지 확인
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: # 떼어진 키가 어떤 키인지 확인
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    #cnt += 1
    #print(cnt)
        # 이걸 실행해보면 전체 while running은 계속해서 돌고 있는 상태임

    charactor_x_pos += to_x * dt # 여기에 dt를 곱하면 이동속도가 fps에 상대성을 가지게 됨
    charactor_y_pos += to_y * dt    # 1회 runnning 당 이속 * 1/fps 만큼 이동한다는 것으로 생각하면 간단하다
                                    # 그러면 결국 초당 이동거리 = 이속이 나온다! (즉 fps에 관계 없이 1초에 이동하는 거리는 동일하다.)

                            # 이 위치 계산이 for문 밖에 있는 이유는
                            # for문 안에 있으면 1개의 입력에만 반응함 -> 꾹 누르고 있는 입력을 반영할 수 없음
                            # running이 돌아가고 있기 때문에 입력을 누르고 있다고 to_x = 5인 상태를 유지함
                            # 그래서 running이 돌아갈 때마다 여기서 5씩 더해서 이동이 구현됨
                            # 입력을 뗀다면 to_x = 0이기 때문에 running이 돌아도 정지가 구현됨
                            # 만약에 for문 안에 있다면 입력의 변화가 일어나야지 위치가 계산됨
                            # 따라서 계속 누르고 있어도 절대로 계산은 1번만 일어남!

    # 경계값 처리 (캐릭터가 화면 밖으로 나가는 것을 방지)
        # 입력과 관련된 부분이 아니기 때문에 입력 for문 외에 존재함.
    if charactor_x_pos < 0: # 왼쪽 경계
        charactor_x_pos = 0
    elif charactor_x_pos > screen_width - chraractor_width: # 오른쪽 경계
        charactor_x_pos = screen_width - chraractor_width

        # 만약에 새로경계와 가로경계를 나란히 elif로 이어서 처리하면
            # elif로 묶였기 때문에 대각선으로 이동할 때 세로는 적용 안됨.
            # 왜냐면 두개를 동시에 고려하지 않고 가로, 세로 중에 하나만 고려하기 때문
    if charactor_y_pos < 0:
        charactor_y_pos = 0
    elif charactor_y_pos > screen_height - chraractor_height:
        charactor_y_pos = screen_height - chraractor_height

    screen.blit(background, (0,0))
        # screen.blit -> 화면에 무언가를 처음 구현하는 함수
        # 백그라운드를 설정하는 과정
        # (0,0)은 화면 구석을 의미함 (왼쪽에서 0, 오른쪽에서 0)
            # 이 위치를 기준으로 화면이 구현됨.

    screen.blit(charactor, (charactor_x_pos, charactor_y_pos))

    # 적캐릭터 구현
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))


    pygame.display.update() # 게임화면 다시 그리기

# 게임이 끝나면 pygame 종료
pygame.quit()
