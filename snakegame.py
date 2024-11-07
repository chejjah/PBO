import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Base class GameObject
class GameObject:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def draw(self, game_window):
        pygame.draw.rect(game_window, self.color, pygame.Rect(self.position[0], self.position[1], 10, 10))

# Snake class
class Snake(GameObject):
    def __init__(self, position):
        super().__init__((0, 255, 0), position)
        self.body = [list(position), [position[0] - 10, position[1]], [position[0] - 20, position[1]]]
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def change_direction(self, direction):
        if direction == 'UP' and self.direction != 'DOWN':
            self.change_to = 'UP'
        elif direction == 'DOWN' and self.direction != 'UP':
            self.change_to = 'DOWN'
        elif direction == 'LEFT' and self.direction != 'RIGHT':
            self.change_to = 'LEFT'
        elif direction == 'RIGHT' and self.direction != 'LEFT':
            self.change_to = 'RIGHT'

    def move(self):
        self.direction = self.change_to
        if self.direction == 'UP':
            self.position[1] -= 10
        elif self.direction == 'DOWN':
            self.position[1] += 10
        elif self.direction == 'LEFT':
            self.position[0] -= 10
        elif self.direction == 'RIGHT':
            self.position[0] += 10
        self.body.insert(0, list(self.position))

    def shrink(self):
        self.body.pop()

    def draw(self, game_window):
        for pos in self.body:
            pygame.draw.rect(game_window, self.color, pygame.Rect(pos[0], pos[1], 10, 10))

    def check_collision(self, frame_size_x, frame_size_y):
        # Check collision with walls
        if self.position[0] < 0 or self.position[0] >= frame_size_x:
            return True
        if self.position[1] < 0 or self.position[1] >= frame_size_y:
            return True
        # Check collision with body
        for block in self.body[1:]:
            if self.position == block:
                return True
        return False

# Apple class
class Apple(GameObject):
    def __init__(self, frame_size_x, frame_size_y):
        super().__init__((255, 0, 0), [random.randrange(1, (frame_size_x // 10)) * 10,
                                        random.randrange(1, (frame_size_y // 10)) * 10])

    def respawn(self, frame_size_x, frame_size_y):
        self.position = [random.randrange(1, (frame_size_x // 10)) * 10,
                         random.randrange(1, (frame_size_y // 10)) * 10]

# Game class
class Game:
    def __init__(self):
        self.frame_size_x = 720
        self.frame_size_y = 480
        self.game_window = pygame.display.set_mode((self.frame_size_x, self.frame_size_y))
        pygame.display.set_caption('Snake Game')
        self.fps_controller = pygame.time.Clock()
        self.snake = Snake([100, 50])
        self.apple = Apple(self.frame_size_x, self.frame_size_y)
        self.apple_extra = Apple(self.frame_size_x, self.frame_size_y)  # Extra apple
        self.apple_extra.color = (0, 0, 255)  # Second apple is blue
        self.score = 0

    def show_score(self):
        font = pygame.font.SysFont('Arial', 20)
        score_surface = font.render('Score : ' + str(self.score), True, (0, 0, 0))
        score_rect = score_surface.get_rect()
        score_rect.midtop = (72, 15)
        self.game_window.blit(score_surface, score_rect)

    def game_over(self):
        font = pygame.font.SysFont('Arial', 90)
        game_over_surface = font.render('U DIE!', True, (255, 0, 0))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (self.frame_size_x / 2, self.frame_size_y / 4)
        self.game_window.fill((0, 0, 0))
        self.game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction('UP')
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction('DOWN')
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction('LEFT')
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction('RIGHT')
                    elif event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))

            self.snake.move()
            if self.snake.position == self.apple.position:
                self.score += 1
                self.apple.respawn(self.frame_size_x, self.frame_size_y)
            elif self.snake.position == self.apple_extra.position:
                self.score += 1
                self.apple_extra.respawn(self.frame_size_x, self.frame_size_y)
            else:
                self.snake.shrink()

            self.game_window.fill((255, 255, 255))
            self.snake.draw(self.game_window)
            self.apple.draw(self.game_window)
            self.apple_extra.draw(self.game_window)
            self.show_score()

            if self.snake.check_collision(self.frame_size_x, self.frame_size_y):
                self.game_over()

            pygame.display.update()
            self.fps_controller.tick(10)

# Run the game
if __name__ == '__main__':
    game = Game()
    game.run()
