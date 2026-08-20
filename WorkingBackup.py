from settings import *

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.ball_bounceX, self.ball_bounceY = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        # ball_bounce_simple_bounce variables init
        self.ball_bounce_velX = 5
        self.ball_bounce_velY = 5
        self.ball_bounce = pygame.Rect((self.ball_bounceX, self.ball_bounceY), (25, 25))
            # VECTOR
        self.ball_pos = pygame.Vector2(self.ball_bounceX, self.ball_bounceY)
        self.ball_vel = pygame.Vector2(250, 0)
        
        # ball_with_gravity_bounce variables init
        self.Gball_bounce = pygame.Rect((self.ball_bounceX, self.ball_bounceY), (25, 25)) # ball with gravity
        self.Gball_pos = pygame.Vector2(self.ball_bounceX, self.ball_bounceY)
        self.Gball_vel = pygame.Vector2(250, 0)
        self.Gball_bounce_stableF_Y = False

    def ball_bounce_simple_bounce(self):
        # movement
        self.ball_bounceX += self.ball_bounce_velX
        self.ball_bounceY += self.ball_bounce_velY
        
        if self.ball_bounce.bottom > SCREEN_HEIGHT:
            self.ball_bounceY = SCREEN_HEIGHT - self.ball_bounce.h
            self.ball_bounce_velY *= -1
        if self.ball_bounce.top < 0:
            self.ball_bounceY = 0
            self.ball_bounce_velY *= -1
        if self.ball_bounce.right > SCREEN_WIDTH:
            self.ball_bounceX = SCREEN_WIDTH - self.ball_bounce.w
            self.ball_bounce_velX *= -1
        if self.ball_bounce.left < 0:
            self.ball_bounceX = 0
            self.ball_bounce_velX *= -1
        
        self.ball_bounce.x, self.ball_bounce.y = self.ball_bounceX, self.ball_bounceY
        self.ball_bounce.topleft = (self.ball_bounceX, self.ball_bounceY)
        
        pygame.draw.ellipse(self.screen, "red", self.ball_bounce)
    
    def ball_bounce_simple_bounce_vec(self):
        #movement
        self.ball_pos += self.ball_vel * self.dt
        if self.ball_bounce.bottom > SCREEN_HEIGHT:
            self.ball_pos.y = SCREEN_HEIGHT - self.ball_bounce.h
            self.ball_vel.y *= -1
        if self.ball_bounce.top < 0:
            self.ball_pos.y = 0
            self.ball_vel.y *= -1
        if self.ball_bounce.right > SCREEN_WIDTH:
            self.ball_pos.x = SCREEN_WIDTH - self.ball_bounce.w
            self.ball_vel.x *= -1
        if self.ball_bounce.left < 0:
            self.ball_pos.x = 0
            self.ball_vel.x *= -1
        
        self.ball_bounce.topleft = (self.ball_pos.x, self.ball_pos.y)
        
        pygame.draw.ellipse(self.screen, "red", self.ball_bounce)
    
    def ball_with_gravity_bounce(self):
        self.GRAVITY = 500
        # v = at
        if not self.Gball_bounce_stableF_Y:
            self.Gball_vel.y += self.GRAVITY * self.dt
        self.Gball_pos += self.Gball_vel * self.dt
        if self.Gball_bounce.bottom > SCREEN_HEIGHT:
            self.Gball_pos.y = SCREEN_HEIGHT - self.Gball_bounce.h
            self.Gball_vel.y *= -75/100
            if self.Gball_vel.y < -10 and self.Gball_vel.y > -50:
                self.Gball_vel.y = 0
                self.Gball_bounce_stableF_Y = True
        if self.Gball_bounce.top < 0:
            self.Gball_pos.y = 0
            self.Gball_vel.y *= -1
        if self.Gball_bounce.right > SCREEN_WIDTH:
            self.Gball_pos.x = SCREEN_WIDTH - self.Gball_bounce.w
            self.Gball_vel.x *= -80/100
        if self.Gball_bounce.left < 0:
            self.Gball_pos.x = 0
            self.Gball_vel.x *= -80/100
        
        self.Gball_bounce.topleft = (self.Gball_pos.x, self.Gball_pos.y)
        print(self.Gball_pos, "  ::::  ", self.Gball_vel)
        
        pygame.draw.ellipse(self.screen, "red", self.Gball_bounce)
    
    def run(self):
        self.running = True
        while self.running:
            self.screen.fill("black")
            self.dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # self.ball_bounce_simple_bounce()
            # self.ball_bounce_simple_bounce_vec()
            self.ball_with_gravity_bounce()
            
            pygame.display.flip()
            
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()