import pygame

class Fighter():
    def __init__(self, x, y, screen_width, screen_height):
        #oyuncu özellikleri
        self.width = int(screen_width * 0.08)   
        self.height = int(screen_height * 0.16) 
        

        self.flip = False
        self.rect = pygame.Rect((x, y, self.width, self.height))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.attack_cooldown = 0

    def move(self, screen_width, screen_height, surface, target):  #HAREKET METODU, Hız ayarlaması buradan yapılacak.
        SPEED = self.screen_width * 0.01
        GRAVITY = self.screen_height * 0.003
        JUMP_POWER = -self.screen_height * 0.05
        dx = 0
        dy = 0

    #tuşları dinle
        key = pygame.key.get_pressed()
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1  # Saldırı aralığı
        else:
            self.attacking = False

        #Yalnızca saldırı yapamıyorken diğer hareketler yapılabilir
        if not self.attacking:
            #HAREKET / MOVEMENT a,d,w
            if key[pygame.K_a]:
                dx = -SPEED
            if key[pygame.K_d]:
                dx = SPEED
            #ZIPLAMA / JUMP
            if key[pygame.K_w] and not self.jump:
                self.vel_y = JUMP_POWER
                self.jump = True
            #SALDIRI / ATTACK
            if key[pygame.K_m] or key[pygame.K_l]:
                self.attack(surface, target)

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
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
           self.vel_y = 0
           self.jump = False
           dy = screen_height - 110 - self.rect.bottom

        #OYUNCULARIN BİRBİRİNE BAKMASI

        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

    #oyuncunun yerini güncelle
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        if self.attacking:
            return
        self.attack_cooldown = 20
        self.attacking = True
        attack_width = self.width * 2.5
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10
        
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)