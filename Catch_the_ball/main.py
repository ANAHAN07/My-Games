import pygame       # Importing the game fuctions from "pygame" module.
import random       # Importing the randomize fuctions from "random" module.


pygame.init()
pygame.mixer.init()  # Initialize sound mixer

WIDTH, HEIGHT = (1080, 720)          # Screen Resolution Setting.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")         # Game Title.


WHITE = (255, 255, 255)     # White Color.
RED = (255, 0, 0)           # Red Color.
BLUE = (0, 0, 255)          # Blue Color.
BLACK = (0, 0, 0)           # Black Color.


ball_radius = 15    # Ball size.
ball_x = random.randint(ball_radius, WIDTH - ball_radius)   # Ball Spawn Area Random.
ball_y = 0
ball_speed = 11     # Ball Speed.


player_cursor_width = 100   # Catch Cursor Width.
player_cursor_height = 20   # Catch Cursor Height.
player_cursor_x = WIDTH // 2 - player_cursor_width // 2
player_cursor_y = HEIGHT - 40
player_cursor_speed = 9     # Catch Cursor Speed.


score = 0       # Score.
font = pygame.font.Font(None, 36)   # Font.
game_over_font = pygame.font.Font(None, 60)  # Larger Font.
author_font = pygame.font.Font(None, 24)  # Font for Author.

# Load sound effects
catch_sound = pygame.mixer.Sound("beep.wav")
fail_sound = pygame.mixer.Sound("fail.wav")

running = True              # Game running in Loop.
while running:
    pygame.time.delay(20)  # Controls the speed of the game.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()     # Key Settings
    if keys[pygame.K_a] and player_cursor_x > 0:        # To move the player Left press on "a" button on your Keyboard.
        player_cursor_x -= player_cursor_speed
    if keys[pygame.K_d] and player_cursor_x < WIDTH - player_cursor_width:  # To move the player Right Left press on "d" button on your Keyboard.
        player_cursor_x += player_cursor_speed

    
    ball_y += ball_speed    # Ball Movement CMD.

    
    if ball_y + ball_radius >= player_cursor_y and player_cursor_x < ball_x < player_cursor_x + player_cursor_width:    # Check's if the ball has hitted by the player_cursor.
        score += 1      # If hitted the the score will be counted as 1.
        catch_sound.play()  # Play sound when ball is caught

        
        if score % 10 == 0:
            ball_speed += 3         # Increases the ball speed after score 10.

        
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)   # Ball resets.
        ball_y = 0  


    if ball_y > HEIGHT:             # If the ball misses the player_cursor.
        fail_sound.play()  # Play sound on game over
        screen.fill(WHITE)      # Background will be White.

        
        game_over_text = ("YOU FAILED! BETTER LUCK NEXT TIME")                # Game over message.
        text_surface = game_over_font.render(game_over_text, True, RED)      # Game over txt color.

        
        text_width, text_height = game_over_font.size(game_over_text)       # Making the game over text in the center.
        text_x = (WIDTH - text_width) // 2
        text_y = (HEIGHT - text_height) // 2

        
        screen.blit(text_surface, (text_x, text_y))     # Making text.
        pygame.display.update()
        pygame.time.delay(3000)     # Once the game over the game will ReStart after 3 seconds.

        
        score = 0       # Reseting the score.
        ball_speed = 5  # Reseting the ball speed.
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)   # Ball Spawn Area Random.
        ball_y = 0


    screen.fill(WHITE)      # Drawing everything , Clearing the screen.
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)  # Drawing the ball.
    pygame.draw.rect(screen, BLUE, (player_cursor_x, player_cursor_y, player_cursor_width, player_cursor_height))  # Drawing the player_cursor.

    
    score_text = font.render(f"Score: {score}", True, BLACK)    # Display score.
    screen.blit(score_text, (10, 10))       # Displaying on the top Left corner.

    
    author_txt = "Powered by ``AN_Productions``"        # Output: Powered by ``AN_Productions``.
    author_text_surface = author_font.render(author_txt, True, BLACK)   # author txt color.
    author_text_width, _ = author_font.size(author_txt)                 # author txt size.
    screen.blit(author_text_surface, (WIDTH - author_text_width - 10, 10))  # Displaying on the top Right corner.

    pygame.display.update()  # Update the screen

pygame.quit()
