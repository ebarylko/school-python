#Ball Class
#Eitan

import pygame, random, turtle

#window and speed

WIDTH = 1024 
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
screen.fill((0, 0, 0))	
speeds = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
colors = ["aquamarine", "azure", "blue", "beige", "orange", "green"]

class Ball:
    """
    Represents a ball on the screen
    """
    def __init__(self):
        #pre: (None)
        #post: initializes the ball attributes
        self.color = random.choice(colors)
        self.size = random.randrange(25, 50)
        self.x = random.randint(50, 975)
        self.y = random.randint(50, 743)
        self.horizontal_speed = random.choice(speeds)
        self.vertical_speed = random.choice(speeds)
        self.border = self.size + 5
        
    def draw(self):
        #pre:(None)
        #post: draws the ball on the screen, moves the ball using current speed,
        # and check if the ball hit the borders
        pygame.draw.circle(screen, (self.color), (self.x, self.y), self.size, 5)
        self.move()
        self.bounce()

    def move(self):
        #pre: (None)
        #post:changes the ball's x and y coordinate according to current speed
        self.x += self.horizontal_speed
        self.y += self.vertical_speed
        
    def bounce(self):
        #pre: None
        #post: changes horizontal speed if ball is at the left/right side,
        #changes vertical speed if the ball is at the top/bottom side

        # checks if it hits the left/right side
        if self.x < self.border or self.x > WIDTH - self.border:
            self.horizontal_speed *= -1

            #checks if it hits the top/bottom side
        if self.y < self.border or self.y > HEIGHT - self.border:
            self.vertical_speed *= -1

balls = [Ball() for x in range(10)]
rungame = True
while rungame:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False	

            
    for b in balls:
        b.draw()
    pygame.display.update()
    clock.tick(30)

pygame.quit()	
