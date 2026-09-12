import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Smart Traffic Signal Simulator")

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
YELLOW = (242, 201, 76)
RED = (235, 87, 87)
GREEN = (39, 174, 96)

COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
SIGNAL_CHANGE_EVENT = pygame.USEREVENT + 2

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((60, 30))
        self.color = (47, 128, 237)
        self.image.fill(self.color)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.velocity_x = 5

    def update(self):
        self.rect.x += self.velocity_x

        if self.rect.left > SCREEN_WIDTH:
            pygame.event.post(pygame.event.Event(COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(SIGNAL_CHANGE_EVENT))
            self.rect.right = 0

    def change_color(self):
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.image.fill(self.color)


class TrafficLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = "GREEN"

    def toggle_state(self):
        if self.state == "GREEN":
            self.state = "RED"
        else:
            self.state = "GREEN"

    def draw(self, surface):
        pygame.draw.rect(surface, (30, 30, 30), (self.x, self.y, 40, 90))
        
        red_color = RED if self.state == "RED" else (80, 0, 0)
        green_color = GREEN if self.state == "GREEN" else (0, 80, 0)
        
        pygame.draw.circle(surface, red_color, (self.x + 20, self.y + 25), 15)
        pygame.draw.circle(surface, green_color, (self.x + 20, self.y + 65), 15)


car = Car(x=10, y=285)
traffic_light = TrafficLight(x=650, y=100)

car_group = pygame.sprite.Group()
car_group.add(car)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == COLOR_CHANGE_EVENT:
            car.change_color()
            
        elif event.type == SIGNAL_CHANGE_EVENT:
            traffic_light.toggle_state()

    car_group.update()

    screen.fill(WHITE)
    
    pygame.draw.rect(screen, GRAY, (0, 250, SCREEN_WIDTH, 100))
    pygame.draw.line(screen, YELLOW, (0, 300), (SCREEN_WIDTH, 300), 5)
    
    traffic_light.draw(screen)
    car_group.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
