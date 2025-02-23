import pygame

class Fighter():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 100))
        self.vel_y = 0
        self.jump = False
        self.attack_type = 0

    def move(self, screen_width, screen_height, surface):  #HAREKET METODU, Hız ayarlaması buradan yapılacak.
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

    #tuşları dinle
        key = pygame.key.get_pressed()

    #hareket a,d,w
        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED
    #zıplama
        if key[pygame.K_w] and self.jump == False:
            self.vel_y = -30
            self.jump = True
    #sadırı
        if key[pygame.K_m] or key[pygame.K_l]:
            self.attack(surface)

            #hangi saldırı çeşidinin kullandığını algıla
            if key[pygame.K_m]:
                self.attack_type = 1
            if key[pygame.K_l]:
                self.attack_type = 2

    #yerçekimi etkisi için
        self.vel_y += GRAVITY   
        dy += self.vel_y

    #oyuncunun ekrandan düşmemesi için
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width = - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
           self.vel_y = 0
           self.jump = False
           dy = screen_height - 110 - self.rect.bottom

    #oyuncunun yerini güncelle
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface):
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)