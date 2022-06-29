import pygame, sys, time, os
from pygame.locals import *
import random

SIZE = 50
BACKGROUND_COLOR = (255, 255, 255)

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.x = 250
        self.y = 250

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,9)*SIZE
        self.y = random.randint(1,9)*SIZE

    def bawlsd(self):
        self.image = pygame.image.load("resources/apple2.jpg").convert()

class Snake(pygame.sprite.Sprite):

    def __init__(self, parent_screen):

        self.parent_screen = parent_screen
        self.direction = 'down'

        self.up_sp_g = [pygame.image.load("resources/g_u_1.png"),
                        pygame.image.load("resources/g_u_2.png"),
                        pygame.image.load("resources/g_u_3.png"),
                        pygame.image.load("resources/g_u_4.png")]
        self.down_sp_g = [pygame.image.load("resources/g_d_1.png"),
                        pygame.image.load("resources/g_d_2.png"),
                        pygame.image.load("resources/g_d_3.png"),
                        pygame.image.load("resources/g_d_4.png")]
        self.left_sp_g = [pygame.image.load("resources/g_l_1.png"),
                        pygame.image.load("resources/g_l_2.png"),
                        pygame.image.load("resources/g_l_3.png"),
                        pygame.image.load("resources/g_l_4.png")]
        self.right_sp_g = [pygame.image.load("resources/g_r_1.png"),
                          pygame.image.load("resources/g_r_2.png"),
                          pygame.image.load("resources/g_r_3.png"),
                          pygame.image.load("resources/g_r_4.png")]

        self.current_spt = 0
        self.image = self.down_sp_g[self.current_spt]

        self.length = 1

        self.x = 50
        self.y = 250

        self.points = 0

        self.is_animating = False

    def up_col(self):
        self.y = 0
        self.draw()
    def lef_col(self):
        self.x = 0
        self.draw()
    def dow_col(self):
        self.y = 450
        self.draw()
    def rig_col(self):
        self.x = 450
        self.draw()

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_kieto(self):
        self.direction = 'kieto'

    def animation(self):
        self.is_animating = True

    def walk(self):
        # update head
        if self.direction == 'left' and self.x >= 50:
            self.x -= SIZE
            self.image = self.left_sp_g[int(self.current_spt)]
        if self.direction == 'right' and self.x <= 400:
            self.x += SIZE
            self.image = self.right_sp_g[int(self.current_spt)]
        if self.direction == 'up' and self.y >= 50:
            self.y -= SIZE
            self.image = self.up_sp_g[int(self.current_spt)]
        if self.direction == 'down' and self.y <= 400:
            self.y += SIZE
            self.image = self.down_sp_g[int(self.current_spt)]
        if self.direction == "kieto":
            self.x = self.x
            self.y = self.y

        self.draw()

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        if self.is_animating == True:
            self.current_spt += .99
            if self.current_spt >= 3:
                self.current_spt = 0

        pygame.display.flip()

class Guide:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen

        self.nl111 = [pygame.image.load("resources/n_l1_1_1.png"),
                      pygame.image.load("resources/n_l1_1_2.png")]
        self.nl121 = [pygame.image.load("resources/n_l1_2_1.png"),
                      pygame.image.load("resources/n_l1_2_2.png"),
                      pygame.image.load("resources/n_l1_2_3.png"),
                      pygame.image.load("resources/n_l1_2_4.png"),
                      pygame.image.load("resources/n_l1_2_5.png"),
                      pygame.image.load("resources/n_l1_2_6.png")]
        self.nl2 = [pygame.image.load('resources/n_l2_1.png'),
                    pygame.image.load('resources/n_l2_2.png'),
                    pygame.image.load('resources/n_l2_3.png'),
                    pygame.image.load('resources/n_l2_4.png'),
                    pygame.image.load('resources/n_l2_5.png'),
                    pygame.image.load('resources/n_l2_6.png')]
        self.nl3 = [pygame.image.load('resources/n_l3_1.png'),
                    pygame.image.load('resources/n_l3_2.png')]
        self.nl4 = [pygame.image.load('resources/n_l4_1.png'),
                    pygame.image.load('resources/n_l4_2.png'),
                    pygame.image.load('resources/n_l4_3.png'),
                    pygame.image.load('resources/n_l4_4.png'),
                    pygame.image.load('resources/n_l4_5.png')]
        self.nl5 = [pygame.image.load('resources/n_l5_1.png')]
        self.nl6 = [pygame.image.load('resources/n_l6_1.png'),
                    pygame.image.load('resources/n_l6_2.png')]

        self.current_spt = 1
        self.nguide = self.nl111[self.current_spt]
        self.spt_name = 'nl111'

    def update(self):

        if self.spt_name == 'nl111':
            self.parent_screen.blit(self.nguide, (150, 510))
            self.current_spt += .9
            if self.current_spt >= 2:
                self.current_spt = 0
            self.nguide = self.nl111[int(self.current_spt)]
        if self.spt_name == 'nl121':
            self.parent_screen.blit(self.nguide, (150, 510))
            self.current_spt += .9
            if self.current_spt >= 6:
                self.current_spt = 0
            self.nguide = self.nl121[int(self.current_spt)]
        if self.spt_name == 'nl2':
            self.parent_screen.blit(self.nguide, (150, 510))
            self.current_spt += .9
            if self.current_spt >= 6:
                self.current_spt = 0
            self.nguide = self.nl2[int(self.current_spt)]
        if self.spt_name == 'nl3':
            self.parent_screen.blit(self.nguide, (150, 510))
            self.current_spt += .9
            if self.current_spt >= 2:
                self.current_spt = 0
            self.nguide = self.nl3[int(self.current_spt)]
        if self.spt_name == 'nl4':
            self.parent_screen.blit(self.nguide, (0, 360))
            self.current_spt += .9
            if self.current_spt >= 5:
                self.current_spt = 0
            self.nguide = self.nl4[int(self.current_spt)]
        if self.spt_name == 'nl5':
            self.parent_screen.blit(self.nguide, (150, 510))
            self.current_spt += .9
            if self.current_spt >= 1:
                self.current_spt = 0
            self.nguide = self.nl5[int(self.current_spt)]
        if self.spt_name == 'nl6':
            self.parent_screen.blit(self.nguide, (0, 0))
            self.current_spt += .9
            if self.current_spt >= 2:
                self.current_spt = 0
            self.nguide = self.nl6[int(self.current_spt)]
        pygame.display.flip()

class mainScreen:

    def __init__(self, parent_screen):
        self.parent_screen = parent_screen

        # Main screen
        self.mainscreen = [pygame.image.load("resources/main0.jpg"),
                           pygame.image.load("resources/main1.jpg"),
                           pygame.image.load("resources/main2.jpg"),
                           pygame.image.load("resources/main3.jpg")]
        self.current_spt = 0
        self.bg = self.mainscreen[self.current_spt]

    def update(self):
        self.parent_screen.blit(self.bg, (0,0))
        self.current_spt += .3
        if self.current_spt >= 3:
            self.current_spt = 0
        self.bg = self.mainscreen[int(self.current_spt)]
        pygame.display.flip()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("LSD")
        icon = pygame.image.load('resources/apple.jpg')
        pygame.display.set_icon(icon)

        pygame.mixer.init()

        self.surface = pygame.display.set_mode((500, 700))
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)
        self.guide = Guide(self.surface)
        self.mainscreen = mainScreen(self.surface)

        self.texts = ""
        self.textcounter = 0

        self.lvl1bg = [pygame.image.load("resources/lvl1_bg1.JPG"),
                       pygame.image.load("resources/lvl1_bg2.JPG")]
        self.lvl2bg = [pygame.image.load('resources/lvl2_bg1.jpg'),
                       pygame.image.load('resources/lvl2_bg2.jpg')]
        self.lvl3bg = [pygame.image.load('resources/lvl3_bg1.jpg'),
                       pygame.image.load('resources/lvl3_bg2.jpg'),
                       pygame.image.load('resources/lvl3_bg3.jpg'),
                       pygame.image.load('resources/lvl3_bg4.jpg')]
        self.lvl4bg = [pygame.image.load('resources/lvl4_bg1.jpg'),
                       pygame.image.load('resources/lvl4_bg2.jpg'),
                       pygame.image.load('resources/lvl4_bg3.jpg'),
                       pygame.image.load('resources/lvl4_bg4.jpg')]
        self.lvl5bg = [pygame.image.load('resources/lvl5_bg1.jpg'),
                       pygame.image.load('resources/lvl5_bg2.jpg'),
                       pygame.image.load('resources/lvl5_bg3.jpg'),
                       pygame.image.load('resources/lvl5_bg4.jpg'),
                       pygame.image.load('resources/lvl5_bg5.jpg'),
                       pygame.image.load('resources/lvl5_bg6.jpg'),
                       pygame.image.load('resources/lvl5_bg7.jpg'),
                       pygame.image.load('resources/lvl5_bg8.jpg'),
                       pygame.image.load('resources/lvl5_bg9.jpg'),
                       pygame.image.load('resources/lvl5_bg10.jpg'),
                       pygame.image.load('resources/lvl5_bg11.jpg'),
                       pygame.image.load('resources/lvl5_bg12.jpg'),
                       pygame.image.load('resources/lvl5_bg13.jpg'),
                       pygame.image.load('resources/lvl5_bg14.jpg')]
        self.lvl6bg = pygame.image.load('resources/lvl6_bg1.jpg')

        self.cs = 0
        self.bg = pygame.image.load("resources/background.jpg")
        self.bgnumber = 0

    def play_background_music(self,music_name):
        if music_name == 'main':
            pygame.mixer.music.load('resources/ms_main.wav')
            pygame.mixer.music.play(-1)
        if music_name == 'bg1':
            pygame.mixer.music.load('resources/ms_bg1.wav')
            pygame.mixer.music.play(-1)
        if music_name == 'bg2':
            pygame.mixer.music.load('resources/ms_bg2.wav')
            pygame.mixer.music.play(-1)
        if music_name == 'bg3':
            pygame.mixer.music.load('resources/ms_bg3.wav')
            pygame.mixer.music.play(-1)
        if music_name == 'bg4':
            pygame.mixer.music.load('resources/ms_bg4.wav')
            pygame.mixer.music.play(-1)
        if music_name == 'bg5':
            pygame.mixer.music.load('resources/ms_bg5.wav')
            pygame.mixer.music.play(-1)
        if music_name == 'bg6':
            pygame.mixer.music.load('resources/ms_bg6.wav')
            pygame.mixer.music.play(-1)

    def play_sound(self, sound_name):
        if sound_name == "crash":
            sound = pygame.mixer.Sound("resources/crash.wav")
        if sound_name == 'ding':
            sound = pygame.mixer.Sound("resources/ding.wav")
        if sound_name == 'scratch':
            sound = pygame.mixer.Sound("resources/scratch.wav")
        if sound_name == 'crying':
            sound = pygame.mixer.Sound("resources/crying.wav")
        if sound_name == 'scream':
            sound = pygame.mixer.Sound("resources/scream.wav")
        pygame.mixer.Sound.play(sound)

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def render_background(self,namebg):
        if namebg == "nolvl":
            self.surface.blit(self.bg, (0,0))
        if namebg == "lvl1":
            self.surface.blit(self.bg, (0, 0))
            self.cs += .4
            if self.cs >= 2:
                self.cs = 0
            self.bg = self.lvl1bg[int(self.cs)]
        if namebg == "lvl2":
            self.surface.blit(self.bg, (0, 0))
            self.cs += .6
            if self.cs >= 2:
                self.cs = 0
            self.bg = self.lvl2bg[int(self.cs)]
        if namebg == "lvl3":
            self.surface.blit(self.bg, (0, 0))
            self.cs += .8
            if self.cs >= 4:
                self.cs = 0
            self.bg = self.lvl3bg[int(self.cs)]
        if namebg == "lvl4":
            self.surface.blit(self.bg, (0, 0))
            self.cs += .8
            if self.cs >= 4:
                self.cs = 0
            self.bg = self.lvl4bg[int(self.cs)]
        if namebg == "lvl5":
            self.surface.blit(self.bg, (0, 0))
            self.cs += 1.75
            if self.cs >= 14:
                self.cs = 0
            self.bg = self.lvl5bg[int(self.cs)]
        if namebg == "lvl6":
            self.bg = self.lvl6bg
            self.surface.blit(self.bg, (0,0))
        pygame.display.flip()

    def render_background_main(self):
        self.mainscreen.update()

    def opaca(self,opalvl):
        if opalvl == 1:
            xd = pygame.image.load('resources/opacidad1.PNG')
            self.surface.blit(xd, (0, 0))
        if opalvl == 2:
            xd = pygame.image.load('resources/opacidad2.PNG')
            self.surface.blit(xd, (0, 0))

    def play(self):

        if self.bgnumber == 1:
            self.render_background('lvl1')
        if self.bgnumber == 2:
            self.render_background('lvl2')
        if self.bgnumber == 3:
            self.render_background('lvl3')
        if self.bgnumber == 4:
            self.render_background('lvl4')
        if self.bgnumber == 5:
            self.render_background('lvl5')
        if self.bgnumber == 6:
            self.render_background('lvl6')

        if self.bgnumber == 6:
            self.apple.bawlsd()

        self.apple.draw()
        self.snake.walk()

        self.snake.animation()
        self.display_score()
        if self.bgnumber == 1:
            self.guide.update()
        if self.bgnumber == 2:
            self.guide.update()
        if self.bgnumber == 3:
            self.guide.update()
        if self.bgnumber == 4:
            self.guide.update()
        if self.bgnumber == 5:
            self.guide.update()

        if self.bgnumber == 5:
            self.opaca(1)
        if self.bgnumber == 6:
            self.opaca(2)

        pygame.display.flip()

        # snake eating apple scenario
        if self.is_collision(self.snake.x, self.snake.y, self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.apple.move()
            self.snake.points += 1

        #Cambiar sprites de guia
        if self.snake.points == 0:
            self.guide.spt_name = 'nl111'
        if self.snake.points == 20:
            self.guide.spt_name = 'nl121'
        if self.snake.points == 40:
            self.guide.spt_name = 'nl2'
        if self.snake.points == 70:
            self.guide.spt_name = 'nl3'
        if self.snake.points == 100:
            self.guide.spt_name = 'nl4'
        if self.snake.points == 130:
            self.guide.spt_name = 'nl5'
        if self.snake.points == 188:
            self.guide.spt_name = 'nl6'

    def display_score(self):
        font = pygame.font.SysFont('Merchant Copy Wide',30)
        score = font.render(f"<Score: {self.snake.points}>",True,(255,255,255),)
        self.surface.blit(score,(10,510))
        font2 = pygame.font.SysFont('Merchant Copy Wide', 15)
        controles = font2.render("<CONTROLES:>", True, (255, 255, 255))
        self.surface.blit(controles, (10, 560))
        usep = font2.render("<Pausa---------------P>",True,(255,255,255))
        self.surface.blit(usep, (10, 580))
        useo = font2.render("<Despausa---------O>", True, (255, 255, 255))
        self.surface.blit(useo, (10, 600))
        usespc = font2.render("<Siguiente---Space>", True, (255, 255, 255))
        self.surface.blit(usespc, (10, 620))
        useesc = font2.render("<Salir--------------Esc>", True, (255, 255, 255))
        self.surface.blit(useesc, (10, 640))
        pygame.display.flip()

    def text(self):
        font = pygame.font.SysFont('Merchant Copy Wide', 25)
        if self.textcounter == 0:
            dial1 = font.render('', True, (255, 255, 255))
            self.surface.blit(dial1, (310, 510))

        #Primera parte
        if self.textcounter == 1:
            dial1 = font.render('Bienvenidx amigx <3,', True, (255, 255, 255))
            self.surface.blit(dial1, (310, 510))
            dial2 = font.render('las personas me', True, (255, 255, 255))
            self.surface.blit(dial2, (310, 530))
            dial3 = font.render('llaman "Guía" y', True, (255, 255, 255))
            self.surface.blit(dial3, (310, 550))
            dial4 = font.render('seré tu acompañante', True, (255, 255, 255))
            self.surface.blit(dial4, (310, 570))
            dial5 = font.render('en este viaje uwu', True, (255, 255, 255))
            self.surface.blit(dial5, (310, 590))
            dial6 = font.render('Presiona "Barra', True, (255, 255, 255))
            self.surface.blit(dial6, (310, 610))
            dial7 = font.render('Espaciadora" para', True, (255, 255, 255))
            self.surface.blit(dial7, (310, 630))
            dial8 = font.render('saltar los textos', True, (255, 255, 255))
            self.surface.blit(dial8, (310, 650))
        if self.textcounter == 2:
            dial1 = font.render('Te explicare de una', True, (255, 255, 255))
            self.surface.blit(dial1, (310, 510))
            dial2 = font.render('forma sencilla como', True, (255, 255, 255))
            self.surface.blit(dial2, (310, 530))
            dial3 = font.render('funciona esto:', True, (255, 255, 255))
            self.surface.blit(dial3, (310, 550))
        if self.textcounter == 3:
            dial1 = font.render('Tu controlas al', True, (255, 255, 255))
            self.surface.blit(dial1, (310, 510))
            dial2 = font.render('personaje usando', True, (255, 255, 255))
            self.surface.blit(dial2, (310, 530))
            dial3 = font.render('"Flechas"', True, (255, 255, 255))
            self.surface.blit(dial3, (310, 550))
            skull = pygame.image.load("resources/g_d_1.png")
            self.surface.blit(skull, (200, 200))
        if self.textcounter == 4:
            dial1 = font.render('Tu misión es consumir', True, (255, 255, 255))
            self.surface.blit(dial1, (310, 510))
            dial2 = font.render('los cuadros de LSD', True, (255, 255, 255))
            self.surface.blit(dial2, (310, 530))
            dial3 = font.render('que aparezcan en', True, (255, 255, 255))
            self.surface.blit(dial3, (310, 550))
            dial4 = font.render('pantalla', True, (255, 255, 255))
            self.surface.blit(dial4, (310, 570))
            dial5 = font.render('', True, (255, 255, 255))
            self.surface.blit(dial5, (310, 590))
            dial6 = font.render('Puedes consumir', True, (255, 255, 255))
            self.surface.blit(dial6, (310, 610))
            dial7 = font.render('cuantos quieras,', True, (255, 255, 255))
            self.surface.blit(dial7, (310, 630))
            dial8 = font.render('pero recuerda que', True, (255, 255, 255))
            self.surface.blit(dial8, (310, 650))
            skull = pygame.image.load("resources/apple.jpg")
            self.surface.blit(skull, (200, 200))
        if self.textcounter == 5:
            dial1 = font.render('excederse puede', True, (255, 255, 255))
            self.surface.blit(dial1, (310, 510))
            dial2 = font.render('ser peligroso', True, (255, 255, 255))
            self.surface.blit(dial2, (310, 530))
            dial3 = font.render('Si necesitas pausar,', True, (255, 255, 255))
            self.surface.blit(dial3, (310, 550))
            dial4 = font.render('usa "P"', True, (255, 255, 255))
            self.surface.blit(dial4, (310, 570))
            dial5 = font.render('', True, (255, 255, 255))
            self.surface.blit(dial5, (310, 590))
            dial6 = font.render('Y para regresar,', True, (255, 255, 255))
            self.surface.blit(dial6, (310, 610))
            dial7 = font.render('presiona "O"', True, (255, 255, 255))
            self.surface.blit(dial7, (310, 630))
            skull = pygame.image.load("resources/apple.jpg")
            self.surface.blit(skull, (200, 200))
        if self.textcounter == 6:
            dial1 = font.render('Esta aventura', True, (255, 255, 255))
            self.surface.blit(dial1, (310, 510))
            dial2 = font.render('audiovisual no es', True, (255, 255, 255))
            self.surface.blit(dial2, (310, 530))
            dial3 = font.render('apta para personas', True, (255, 255, 255))
            self.surface.blit(dial3, (310, 550))
            dial4 = font.render('fotosensibles, por', True, (255, 255, 255))
            self.surface.blit(dial4, (310, 570))
            dial5 = font.render('favor no continúes', True, (255, 255, 255))
            self.surface.blit(dial5, (310, 590))
            dial6 = font.render('si ese es su caso', True, (255, 255, 255))
            self.surface.blit(dial6, (310, 610))
        if self.textcounter == 7:
            dial1 = font.render('En cualquier', True, (255, 255, 255))
            self.surface.blit(dial1, (310, 510))
            dial2 = font.render('momento puedes', True, (255, 255, 255))
            self.surface.blit(dial2, (310, 530))
            dial3 = font.render('volver a la', True, (255, 255, 255))
            self.surface.blit(dial3, (310, 550))
            dial4 = font.render('realidad pulsando', True, (255, 255, 255))
            self.surface.blit(dial4, (310, 570))
            dial5 = font.render('"Esc"', True, (255, 255, 255))
            self.surface.blit(dial5, (310, 590))
        if self.textcounter == 8:
            dial1 = font.render('Esta experiencia', True, (255, 255, 255))
            self.surface.blit(dial1, (310, 510))
            dial2 = font.render('es recreativa y', True, (255, 255, 255))
            self.surface.blit(dial2, (310, 530))
            dial3 = font.render('no busca', True, (255, 255, 255))
            self.surface.blit(dial3, (310, 550))
            dial4 = font.render('incentivar el uso', True, (255, 255, 255))
            self.surface.blit(dial4, (310, 570))
            dial5 = font.render('de drogas', True, (255, 255, 255))
            self.surface.blit(dial5, (310, 590))
            dial6 = font.render('psicodélicas', True, (255, 255, 255))
            self.surface.blit(dial6, (310, 610))
        if self.textcounter == 9:
            dial1 = font.render('Dicho esto,', True, (255, 255, 255))
            self.surface.blit(dial1, (310, 510))
            dial2 = font.render('hay que alocarnos', True, (255, 255, 255))
            self.surface.blit(dial2, (310, 530))
            dial3 = font.render(':0', True, (255, 255, 255))
            self.surface.blit(dial3, (310, 550))

        #2da
        if self.textcounter == 10:
            dial1 = font.render('Ke loko esta', True, (255, 255, 255))
            self.surface.blit(dial1, (310, 510))
            dial2 = font.render('esto, ya', True, (255, 255, 255))
            self.surface.blit(dial2, (310, 530))
            dial3 = font.render('empece a', True, (255, 255, 255))
            self.surface.blit(dial3, (310, 550))
            dial4 = font.render('marearme', True, (255, 255, 255))
            self.surface.blit(dial4, (310, 570))
            dial5 = font.render('DJ cambiale', True, (255, 255, 255))
            self.surface.blit(dial5, (310, 590))
            dial6 = font.render('d rola o-O', True, (255, 255, 255))
            self.surface.blit(dial6, (310, 610))

        #3ra
        if self.textcounter == 11:
            dial1 = font.render('Perdi mis', True, (255, 255, 255))
            self.surface.blit(dial1, (310, 510))
            dial2 = font.render('gafas, creo que', True, (255, 255, 255))
            self.surface.blit(dial2, (310, 530))
            dial3 = font.render('ya fue suficiente', True, (255, 255, 255))
            self.surface.blit(dial3, (310, 550))
            dial4 = font.render('pero si tu', True, (255, 255, 255))
            self.surface.blit(dial4, (310, 570))
            dial5 = font.render('continuas, yo', True, (255, 255, 255))
            self.surface.blit(dial5, (310, 590))
            dial6 = font.render('tambien', True, (255, 255, 255))
            self.surface.blit(dial6, (310, 610))

        #4ta
        if self.textcounter == 12:
            dial1 = font.render('Sexooooo!!', True, (255, 255, 255))
            self.surface.blit(dial1, (310, 510))
            dial2 = font.render('(Consensuado))', True, (255, 255, 255))
            self.surface.blit(dial2, (310, 530))

        #5ta
        if self.textcounter == 13:
            dial1 = font.render('*Llora*', True, (255, 255, 255))
            self.surface.blit(dial1, (310, 510))

        #6ta
        if self.textcounter == 14:
            dial1 = font.render('*...', True, (255, 255, 255))
            self.surface.blit(dial1, (310, 510))

        pygame.display.flip()

    def show_main_screen(self):
        self.render_background_main()

    def run(self):
        running1 = True
        running2 = False
        running3 = False
        running4 = False
        running5 = False
        running6 = False
        running7 = False
        pause = True

        self.play_background_music('main')
        while running1:

            pygame.init()
            clock = pygame.time.Clock()

            self.show_main_screen()
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                        running1 = False
                        pause = False
                    if event.key == K_SPACE:
                        running1 = False
            clock.tick(60)

        pygame.mixer.music.pause()
        self.play_sound("crash")
        self.textcounter = 1

        while pause:

            pygame.init()
            clock = pygame.time.Clock()

            self.render_background('nolvl')
            self.display_score()
            self.guide.update()
            self.text()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.textcounter += 1
                        if self.textcounter <= 9:
                            self.play_sound("crash")
                    if event.key == K_ESCAPE:
                        self.textcounter = 10
                        running2 = False
            if self.textcounter >= 10:
                self.textcounter = 0
                pause = False
                running2 = True
            time.sleep(.2)
            clock.tick(60)

        self.play_background_music('bg1')
        pygame.mixer.music.unpause()
        while running2:

            pygame.init()
            clock = pygame.time.Clock()

            self.bgnumber = 1

            if self.snake.points == 40:
                running2 = False
                pause = True

            if self.snake.y < 0:
                self.snake.up_col()
                self.snake.move_kieto()
            if self.snake.x < 0:
                self.snake.lef_col()
                self.snake.move_kieto()
            if self.snake.y > 450:
                self.snake.dow_col()
                self.snake.move_kieto()
            if self.snake.x > 450:
                self.snake.rig_col()
                self.snake.move_kieto()

            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running2 = False

                    if event.key == K_p:
                        pygame.mixer.music.pause()
                        pause = True

                    if event.key == K_o:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT and self.snake.x >= 50:
                            self.snake.move_left()

                        if event.key == K_RIGHT and self.snake.x <= 400:
                            self.snake.move_right()

                        if event.key == K_UP and self.snake.y >= 50:
                            self.snake.move_up()

                        if event.key == K_DOWN and self.snake.y <= 400:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running2 = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_main_screen()
                pause = True
                self.reset()

            time.sleep(.2)
            clock.tick(60)

        self.play_sound("crash")
        self.textcounter = 10

        while pause:

            pygame.init()
            clock = pygame.time.Clock()

            self.render_background('lvl1')
            self.display_score()
            self.guide.update()
            self.text()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.textcounter += 1
                    if event.key == K_ESCAPE:
                        self.textcounter = 11
                        running3 = False
            if self.textcounter >= 11:
                self.textcounter = 0
                self.play_sound("scratch")
                pause = False
                running3 = True
            time.sleep(.15)
            clock.tick(60)

        self.play_background_music('bg2')
        while running3:

            pygame.init()
            clock = pygame.time.Clock()

            self.bgnumber = 2

            if self.snake.points == 70:
                running3 = False
                pause = True

            if self.snake.y < 0:
                self.snake.up_col()
                self.snake.move_kieto()
            if self.snake.x < 0:
                self.snake.lef_col()
                self.snake.move_kieto()
            if self.snake.y > 450:
                self.snake.dow_col()
                self.snake.move_kieto()
            if self.snake.x > 450:
                self.snake.rig_col()
                self.snake.move_kieto()

            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running3 = False

                    if event.key == K_p:
                        pygame.mixer.music.pause()
                        pause = True

                    if event.key == K_o:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT and self.snake.x >= 50:
                            self.snake.move_left()

                        if event.key == K_RIGHT and self.snake.x <= 400:
                            self.snake.move_right()

                        if event.key == K_UP and self.snake.y >= 50:
                            self.snake.move_up()

                        if event.key == K_DOWN and self.snake.y <= 400:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running3 = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_main_screen()
                pause = True
                self.reset()

            time.sleep(.15)
            clock.tick(60)

        self.play_sound("crash")
        self.textcounter = 11

        while pause:

            pygame.init()
            clock = pygame.time.Clock()

            self.render_background('lvl2')
            self.display_score()
            self.guide.update()
            self.text()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.textcounter += 1
                    if event.key == K_ESCAPE:
                        self.textcounter = 12
                        running4 = False
            if self.textcounter >= 12:
                self.textcounter = 0
                self.play_sound("scratch")
                pause = False
                running4 = True
            time.sleep(.1)
            clock.tick(60)

        self.play_background_music('bg3')
        while running4:

            pygame.init()
            clock = pygame.time.Clock()

            self.bgnumber = 3

            if self.snake.points == 100:
                running4 = False
                pause = True

            if self.snake.y < 0:
                self.snake.up_col()
                self.snake.move_kieto()
            if self.snake.x < 0:
                self.snake.lef_col()
                self.snake.move_kieto()
            if self.snake.y > 450:
                self.snake.dow_col()
                self.snake.move_kieto()
            if self.snake.x > 450:
                self.snake.rig_col()
                self.snake.move_kieto()

            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running4 = False

                    if event.key == K_p:
                        pygame.mixer.music.pause()
                        pause = True

                    if event.key == K_o:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT and self.snake.x >= 50:
                            self.snake.move_left()

                        if event.key == K_RIGHT and self.snake.x <= 400:
                            self.snake.move_right()

                        if event.key == K_UP and self.snake.y >= 50:
                            self.snake.move_up()

                        if event.key == K_DOWN and self.snake.y <= 400:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running4 = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_main_screen()
                pause = True
                self.reset()

            time.sleep(.1)
            clock.tick(60)

        self.play_sound("crash")
        self.textcounter = 12

        while pause:

            pygame.init()
            clock = pygame.time.Clock()

            self.render_background('lvl3')
            self.display_score()
            self.guide.update()
            self.text()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.textcounter += 1
                    if event.key == K_ESCAPE:
                        self.textcounter = 13
                        running5 = False
            if self.textcounter >= 13:
                self.textcounter = 0
                self.play_sound("scratch")
                pause = False
                running5 = True
            time.sleep(.05)
            clock.tick(60)

        self.play_background_music('bg4')
        while running5:

            pygame.init()
            clock = pygame.time.Clock()

            self.bgnumber = 4

            if self.snake.points == 130:
                running5 = False
                pause = True

            if self.snake.y < 0:
                self.snake.up_col()
                self.snake.move_kieto()
            if self.snake.x < 0:
                self.snake.lef_col()
                self.snake.move_kieto()
            if self.snake.y > 450:
                self.snake.dow_col()
                self.snake.move_kieto()
            if self.snake.x > 450:
                self.snake.rig_col()
                self.snake.move_kieto()

            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running5 = False

                    if event.key == K_p:
                        pygame.mixer.music.pause()
                        pause = True

                    if event.key == K_o:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT and self.snake.x >= 50:
                            self.snake.move_left()

                        if event.key == K_RIGHT and self.snake.x <= 400:
                            self.snake.move_right()

                        if event.key == K_UP and self.snake.y >= 50:
                            self.snake.move_up()

                        if event.key == K_DOWN and self.snake.y <= 400:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running5 = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_main_screen()
                pause = True
                self.reset()

            time.sleep(.05)
            clock.tick(60)

        self.play_sound("crying")
        self.textcounter = 13

        while pause:

            pygame.init()
            clock = pygame.time.Clock()

            self.render_background('lvl4')
            self.display_score()
            self.guide.update()
            self.text()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.textcounter += 1
                    if event.key == K_ESCAPE:
                        self.textcounter = 14
                        running6 = False
            if self.textcounter >= 14:
                self.textcounter = 0
                self.play_sound("scratch")
                pause = False
                running6 = True
            time.sleep(.05)
            clock.tick(60)

        self.play_background_music('bg5')
        while running6:

            pygame.init()
            clock = pygame.time.Clock()

            self.bgnumber = 5

            if self.snake.points == 160:
                running6 = False
                pause = True

            if self.snake.y < 0:
                self.snake.up_col()
                self.snake.move_kieto()
            if self.snake.x < 0:
                self.snake.lef_col()
                self.snake.move_kieto()
            if self.snake.y > 450:
                self.snake.dow_col()
                self.snake.move_kieto()
            if self.snake.x > 450:
                self.snake.rig_col()
                self.snake.move_kieto()

            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running6 = False

                    if event.key == K_p:
                        pygame.mixer.music.pause()
                        pause = True

                    if event.key == K_o:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT and self.snake.x >= 50:
                            self.snake.move_left()

                        if event.key == K_RIGHT and self.snake.x <= 400:
                            self.snake.move_right()

                        if event.key == K_UP and self.snake.y >= 50:
                            self.snake.move_up()

                        if event.key == K_DOWN and self.snake.y <= 400:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running6 = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_main_screen()
                pause = True
                self.reset()

            time.sleep(.05)
            clock.tick(60)

        self.textcounter = 14

        while pause:

            pygame.init()
            clock = pygame.time.Clock()

            self.render_background('lvl5')
            self.display_score()
            self.text()
            self.opaca(1)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.textcounter += 1
                    if event.key == K_ESCAPE:
                        self.textcounter = 15
                        running7 = False
            if self.textcounter >= 15:
                self.textcounter = 0
                self.play_sound("scratch")
                pause = False
                running7 = True
            time.sleep(.05)
            clock.tick(60)

        self.play_background_music('bg6')
        while running7:

            pygame.init()
            clock = pygame.time.Clock()

            self.bgnumber = 6

            if self.snake.points == 188:
                running7 = False
                pause = True

            if self.snake.y < 0:
                self.snake.up_col()
                self.snake.move_kieto()
            if self.snake.x < 0:
                self.snake.lef_col()
                self.snake.move_kieto()
            if self.snake.y > 450:
                self.snake.dow_col()
                self.snake.move_kieto()
            if self.snake.x > 450:
                self.snake.rig_col()
                self.snake.move_kieto()

            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running7 = False

                    if event.key == K_p:
                        pygame.mixer.music.pause()
                        pause = True

                    if event.key == K_o:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT and self.snake.x >= 50:
                            self.snake.move_left()

                        if event.key == K_RIGHT and self.snake.x <= 400:
                            self.snake.move_right()

                        if event.key == K_UP and self.snake.y >= 50:
                            self.snake.move_up()

                        if event.key == K_DOWN and self.snake.y <= 400:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running7 = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_main_screen()
                pause = True
                self.reset()

            time.sleep(.25)
            clock.tick(60)

        pygame.mixer.music.pause()
        while pause:

            pygame.init()
            clock = pygame.time.Clock()
            self.play_sound("scream")
            self.render_background('lvl6')
            self.display_score()
            self.guide.update()
            pygame.display.flip()
            time.sleep(.2)
            clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()