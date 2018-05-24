import pygame;
import random;

pygame.init();
clock = pygame.time.Clock();

screen_size = (1200, 800);
game_display = pygame.display.set_mode(screen_size);
font = pygame.font.SysFont('hooge0555cyr2', 25);
black = (0, 0, 0);
white = (255, 255, 255);
points = [];
FPS = 45;

class Pong_Ball:
    def __init__(self):
        self.location = [screen_size[0]/2, screen_size[1]/2];
        self.direction = random.choice([-1, 1]);
        self.up_or_down = 0;

    def display_ball(self, ball_speed, player_one, player_two):
        if(self.check_screen_collision()):
            self.up_or_down = -(self.up_or_down);
        elif(self.check_player_collision(player_one)):
            self.direction = -(self.direction);
            if(self.up_or_down == 0):
                self.up_or_down = random.choice([-1, 1]);

        elif(self.check_player_collision(player_two)):
            self.direction = -(self.direction);
            if (self.up_or_down == 0):
                self.up_or_down = random.choice([-1, 1]);

        self.location[0] += round((ball_speed * self.direction) * 5.0) / 5.0;
        self.location[1] += round((ball_speed * self.up_or_down) * 5.0) / 5.0;
        pygame.draw.rect(game_display, white, [self.location[0], self.location[1], 20, 20]);

    def check_player_collision(self, player):
        for i in player.paddle_list:
            if(self.location == i):
                return True;

    def check_screen_collision(self):
        return self.location[1] == screen_size[1] or self.location[1] == 0;

class Paddle:
    def __init__(self, x, y):
        self.paddle_list = [];
        self.x = x;
        self.y = y;

        self.initialize_paddle();

    def initialize_paddle(self):
        for i in range(100, 0, -10):
            self.paddle_list.append([int(self.x), int(i + self.y)]);
        self.paddle_list.append([int(self.x), int(self.y)]);
        for i in range(int(self.y) - 10, int(self.y - 60) - 50, -10):
            self.paddle_list.append([int(self.x), int(i)]);

    def draw_paddle(self, move):
        for i in self.paddle_list:
            if(move < 0):
                if(self.check_upper_edge()):
                    i[1] += move;
            elif(move > 0):
                if (self.check_lower_edge()):
                    i[1] += move;
            pygame.draw.rect(game_display, white, [i[0], i[1], 20, 20]);

    def check_upper_edge(self):
        return self.paddle_list[len(self.paddle_list) - 1][1] != 0;

    def check_lower_edge(self):
        return self.paddle_list[0][1] != screen_size[1];

def display_players(player_one, player_two, move_one, move_two):
    player_one.draw_paddle(move_one);
    player_two.draw_paddle(move_two);
def display_ball(ball, ball_speed, player_one, player_two):
    ball.display_ball(ball_speed, player_one, player_two);
def display_points():
    u = 0;

def render_screen(player_one, player_two, ball, ball_speed, move_one, move_two):
    game_display.fill(black);
    display_players(player_one, player_two, move_one, move_two);
    display_ball(ball, ball_speed, player_one, player_two);

    pygame.display.update();

    clock.tick(FPS);

def main():
    player_one = Paddle(screen_size[0] - 70, screen_size[1]/2);
    player_two = Paddle(70, screen_size[1]/2);
    ball = Pong_Ball();

    paddle_speed = 10;
    ball_speed = 10;

    move_one = 0;
    move_two = 0;

    game_over = False;
    restart = False;

    while(not game_over):
        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                #QUIT
                if(event.type == pygame.QUIT):
                    game_over = True;
                if(event.key == pygame.K_q):
                    game_over = True;
                if(event.key == pygame.K_r):
                    restart = True;

                #MOVEMENT PLAYER 1
                if(event.key == pygame.K_UP):
                    move_one -= paddle_speed;
                if(event.key == pygame.K_DOWN):
                    move_one += paddle_speed;

                # MOVEMENT PLAYER 1
                if(event.key == pygame.K_w):
                    move_two -= paddle_speed;
                if (event.key == pygame.K_s):
                    move_two += paddle_speed;

            #RELEASE KEY
            if(event.type == pygame.KEYUP):
                if(event.key == pygame.K_UP):
                    move_one = 0;
                if(event.key == pygame.K_DOWN):
                    move_one = 0;
                if (event.key == pygame.K_w):
                    move_two = 0;
                if(event.key == pygame.K_s):
                    move_two = 0;

            if(restart):
                restart = False;
                main();

        render_screen(player_one, player_two, ball, ball_speed, move_one, move_two);

if __name__ == '__main__':
    main();