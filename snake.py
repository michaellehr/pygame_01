import sys, pygame
pygame.init()

clock = pygame.time.Clock()

size = width, height = 640, 640
speed = 1
speed_arr = [speed, 0]
black = 0, 0, 0
red = pygame.Color(200, 0, 0)
green = pygame.Color(0, 200, 0)
blue = pygame.Color(0, 0, 200)

board_scale=20
snake_length=10

rows, cols = (int(width/board_scale), int(height/board_scale))
board=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    board.append(col)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snake")

background = pygame.Surface(screen.get_size())
background = background.convert()

snake_head=pygame.Rect(width/2,height/2,board_scale,board_scale)

ball = pygame.transform.scale(pygame.image.load("intro_ball.gif"), (20, 20) )

lose = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
       if speed_arr[0] != 0:
           speed_arr = [0, -speed]
    if keys[pygame.K_DOWN]:
       if speed_arr[0] != 0:
           speed_arr = [0, speed]
    if keys[pygame.K_LEFT]:
        if speed_arr[1] != 0:
           speed_arr = [-speed, 0]
    if keys[pygame.K_RIGHT]:
       if speed_arr[1] != 0:
            speed_arr = [speed, 0]

    snake_head = snake_head.move(speed_arr)
    if snake_head.top <= 0:
        lose = True
    if snake_head.bottom >= height:
        lose = True
    if snake_head.left <= 0:
        lose = True
    if snake_head.right >= width:
        lose = True

    board_pos = [int(snake_head.centerx/board_scale), int(snake_head.centery/board_scale)]
    if board[board_pos[0]][board_pos[1]] > 1:
        lose = True
    elif board[board_pos[0]][board_pos[1]] == 0:
        # move
        for x in range(0,len(board)):
            for y in range(0,len(board[x])):
                if board[x][y] == snake_length:
                    board[x][y] = 0
                elif board[x][y] != 0:
                    board[x][y] = board[x][y]+1
        board[board_pos[0]][board_pos[1]] = 1


    screen.fill(black)

    if lose:
        font = pygame.font.Font(None, 32)
        text = font.render("YOU LOSE", True, (200, 100, 100))
        textpos = text.get_rect(centerx=background.get_width() / 2, centery=background.get_height() / 2)
        background.blit(text, textpos)
        screen.blit(background, (0, 0))
    else:
        for x in range(0,len(board)):
            for y in range(0,len(board[x])):
                if board[x][y] == 1:
                    snake_piece=pygame.Rect(x * board_scale,
                                            y * board_scale,
                                            board_scale,
                                            board_scale)
                    #pygame.Surface.fill(screen, red, snake_piece)
                    screen.blit(ball, snake_piece)
                if board[x][y] > 1:
                    snake_piece=pygame.Rect(x * board_scale,
                                            y * board_scale,
                                            board_scale,
                                            board_scale)
                    pygame.Surface.fill(screen, green, snake_piece)
                
        pygame.Surface.fill(screen, red, snake_head)

    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000