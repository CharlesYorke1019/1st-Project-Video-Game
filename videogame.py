import pygame
import sys

import random

from pygame import MOUSEBUTTONDOWN

from support import import_folder

pygame.init()

screen_width = 1200
screen_height = 704
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

#### IMAGES ####

fire_ball = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/fireball.png')
fire_ball_rect = fire_ball.get_rect(topleft=(700, 650))

flip_fire_ball = pygame.transform.flip(fire_ball, True, False)
flip_fire_ball_rect = flip_fire_ball.get_rect(topleft=(700, 650))

rasengan = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/rasengan.png')
rasengan_rect_new = rasengan.get_rect(topleft=(700, 650))

flip_rasengan = pygame.transform.flip(rasengan, True, False)
flip_rasengan_rect = flip_rasengan.get_rect(topleft=(700, 650))

background = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/BG1.png')
background2 = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/BG2.png')

n_special1 = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/n_special.png')
n_special1_rect = n_special1.get_rect(topleft=(700, 650))
n_special2 = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/n_special2.png')
n_special2_rect = n_special2.get_rect(topleft=(700, 650))

s_special1 = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/s_special1.png')
s_special1_rect = s_special1.get_rect(topleft=(750, 650))
s_special2 = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/s_special2.png')
s_special2_rect = s_special2.get_rect(topleft=(750, 650))
s_special3 = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/s_special3.png')
s_special3_rect = s_special3.get_rect(topleft=(750, 650))

s_special4 = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/s_special4.png')
s_special4_rect = s_special4.get_rect(topleft=(100, 0))
s_special4_rect2 = s_special4.get_rect(topleft=(500, 0))
s_special4_rect3 = s_special4.get_rect(topleft=(900, 0))

s_special5 = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/s_special5.png')
s_special5_rect = s_special5.get_rect(topleft=(750, 650))

s_special6 = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/s_special6.png')

s_special7 = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/s_special7.png')

s_special8 = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/s_special8.png')

rinnegan = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/rinnegan.png')

shuriken = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/shuriken.png')
shuriken_rect = shuriken.get_rect(topleft=(700, 650))
flip_shuriken = pygame.transform.flip(shuriken, True, True)
flip_shuriken_rect = flip_shuriken.get_rect(topleft=(700, 650))

clone = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/clone.png')
clone_rect = clone.get_rect(topleft=(700, 650))
flip_clone = pygame.transform.flip(clone, True, False)
flip_clone_rect = flip_clone.get_rect(topleft=(700, 650))

smoke1 = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/smoke1.png')
smoke1_rect = smoke1.get_rect(topleft=(700, 650))
smoke2 = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/smoke2.png')
smoke2_rect = smoke2.get_rect(topleft=(700, 650))

flip_smoke1 = pygame.transform.flip(smoke1, True, False)
flip_smoke1_rect = flip_smoke1.get_rect(topleft=(700, 650))
flip_smoke2 = pygame.transform.flip(smoke2, True, False)
flip_smoke2_rect = flip_smoke2.get_rect(topleft=(700, 650))

start_image = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/startlogo.png')
settings_image = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/settingslogo.png')
exit_image = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/exitlogo.png')
back_image = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/back.png')
pause_image = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/pauselogo.png')
menu_image = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/menulogo.png')
return_image = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/returnlogo.png')
startagain = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/playagain.png')
fight_symobl = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/fight.png')
menu = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/mainmenubutton.png')
map_select_screen = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/selectmap.png')
mp1 = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/map1.png')
mp2 = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/map2.png')
title = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/title.png')
control_image = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/controlslogo.png')
game_logic_image = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/gamelogic.png')
controls_page_image = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/controlspage.png')
special_available = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/special_available.png')
ko = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/KnockOut.png')
hitcount = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/hitcount.png')

mm1 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm1.png').convert_alpha()
mm2 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm2.png').convert_alpha()
mm3 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm3.png').convert_alpha()
mm4 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm4.png').convert_alpha()
mm5 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm5.png').convert_alpha()
mm6 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm6.png').convert_alpha()
mm7 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm7.png').convert_alpha()
mm8 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm8.png').convert_alpha()
mm9 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm9.png').convert_alpha()
mm10 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm10.png').convert_alpha()
mm11 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm11.png').convert_alpha()
mm12 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm12.png').convert_alpha()
mm13 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm13.png').convert_alpha()
mm14 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm14.png').convert_alpha()
mm15 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm15.png').convert_alpha()
mm16 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm16.png').convert_alpha()
mm17 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm17.png').convert_alpha()
mm18 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm18.png').convert_alpha()
mm19 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm19.png').convert_alpha()
mm20 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm20.png').convert_alpha()
mm21 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm21.png').convert_alpha()
mm22 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm22.png').convert_alpha()
mm23 = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mm23.png').convert_alpha()

mmbg = pygame.image.load('/Users/charlieyorke/ace/imgs/mmbackground/mmbg.png').convert_alpha()

load1 = pygame.image.load('/Users/charlieyorke/ace/imgs/loading/loading1.png')
load2 = pygame.image.load('/Users/charlieyorke/ace/imgs/loading/loading2.png')
load3 = pygame.image.load('/Users/charlieyorke/ace/imgs/loading/loading3.png')
load4 = pygame.image.load('/Users/charlieyorke/ace/imgs/loading/loading4.png')
load5 = pygame.image.load('/Users/charlieyorke/ace/imgs/loading/loading5.png')
load6 = pygame.image.load('/Users/charlieyorke/ace/imgs/loading/loading6.png')

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, name, pos):
        pygame.sprite.Sprite.__init__(self)
        self.import_character_assets()

        #### STATE ####

        self.name = name
        self.frame_index = 0
        self.animation_speed = 0.12
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.status = 'idle'

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 12
        self.gravity = 1.2
        self.jump_speed = -25

        self.facing_right = True
        self.on_ground = True
        self.on_ceiling = False

        self.max_health = 410
        self.level = 1
        self.charge = 0
        self.charging = True

        self.on_screen = True

        #### ATTACKS ####

        self.rasengan = False
        self.rasengan_count = 0

        self.special = False
        self.special_activate = False
        self.special_successful = False
        self.special_count = 0
        self.special_available = False
        self.special_available_count = 0

        self.h2h_count = 0
        self.b4_attack = True
        self.b4_attack_count = 0
        self.move = True

        self.attack1right = False
        self.attack1 = False
        self.attack2 = False
        self.initiate_attack_count = 0

        self.random = 1

        self.allowed_attack1 = True

        self.attack3 = False
        self.attack3right = False
        self.attack3count = 0
        self.attack3allowed = True
        self.attack3_allowed_count = 0

        self.clone_movement = False
        self.clone = False
        self.clone_on_screen = False
        self.clone_count = 0
        self.shuriken = False
        self.shuriken_movement = False
        self.clone_test = False

        self.limit_attack = False
        self.limited_attack_count = 0
        self.limited_attack_amount = 3

        self.flip_clone_movement = False
        self.flip_clone = False
        self.flip_clone_on_screen = False
        self.flip_clone_count = 0
        self.flip_shuriken = False
        self.flip_shuriken_movement = False
        self.flip_clone_test = False

        #### TELEPORT ####

        self.teleporting = False
        self.teleport_count = 0

        #### GUARD ####

        self.guard_count = 0
        self.guard = True
        self.guard_active = False
        self.guard_active_count = 0
        self.guard_successful = False
        self.guarded_combo = False
        self.guarded_combo_count = 0

        self.stall = False
        self.stall2 = False

        #### TAKING DAMAGE ####

        self.taking_damage1 = False
        self.taking_damage2 = False

        self.initiate_damage_state = False
        self.initiate_damage_count = 0

        self.during_combo = False
        self.during_combo2 = False
        self.combo_count = 0
        self.combo_count2 = 0
        self.after_combo = False
        self.after_combo_count = 0
        self.after_combo2 = False
        self.after_combo_count2 = 0

        self.b4_damage = False

        self.idle_hit = False

        self.damagecount = 0

        self.damagecombo1 = False

        self.while_hit2 = False

        #### COMBOS ####

        self.hit1 = False
        self.hit2 = True

        self.random = 1

        self.spamcount1 = 0 
        self.spamcount2 = 0

        self.in_combo = False
        self.combo_timer = 0
        self.hit_count = 0
        self.in_air = False

        #### POSITION ####

        self.out_of_bounds = False

        self.in_range = False
        self.in_range2 = False

        self.stopped = False

    def import_character_assets(self):
        character_path = '/Users/charlieyorke/ace/imgs/Naruto/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'guardstall': [], 'b4special': [], 'special': [], 'combotwo': [], 'combothree': [], 'combofour': [], 'combofive': [], 'combosix': [], 'guardfireball': [], 'b4fireball': [], 'aftercombo': [], 'aftercombo2': [], 'whilehit2': [], 'stallhit': [], 'b4attack': [], 'attack1': [], 'attack1after': [], 'attack2': [], 'attack3': [], 'charge': [], 'combo': [], 'teleport': [], 'guard': [], 'guardattack2': [], 'hitfireball': [], 'hitchidori': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

        if self.on_ceiling:
            self.rect = self.image.get_rect(bottom = self.rect.bottom)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        else:
            self.rect = self.image.get_rect(center = self.rect.center)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if self.on_screen == True and self.status != 'b4fireball' and self.status != 'hitfireball' and self.status != 'hitchidori' and self.after_combo == False and self.after_combo2 == False:
            if keys[pygame.K_d] and self.rect.x < 1150 and self.stall == False and self.stall2 == False and self.stopped == False:
                self.direction.x = 1.2
                self.facing_right = True
                
            elif keys[pygame.K_a] and self.rect.x > 1 and self.stall == False and self.stall2 == False and self.stopped == False:
                self.direction.x = -1.2
                self.facing_right = False
        
            else:
                self.direction.x = 0

        if self.in_air == True:
            self.direction.y = -1

        if self.on_screen == False:
            self.direction.x = 0
        if self.status == 'hitfireball':
            self.direction.x = 0

        if keys[pygame.K_w] and self.on_ground == True:
            if self.rect.bottom <= 698:
                self.on_ground = False
                self.jump()

    def get_status(self):

        keys = pygame.key.get_pressed()

        if self.direction.y < 0:
            self.status = 'jump'
            self.animation_speed = .20
        
        else:
            if self.direction.x != 0:
                self.status = 'run'
                self.animation_speed = .20
            else:
                self.status = 'idle'
                self.animation_speed = .20

        if keys[pygame.K_f]:
            self.hit1 = True

        if self.hit1 == True:           
            if self.random == 1:
                self.status = 'combo'
                self.animation_speed = 0.25
            if self.random == 2:
                self.status = 'combotwo'
                self.animation_speed = 0.25
            if self.random == 3:
                self.status = 'combothree'
                self.animation_speed = 0.25
            if self.random == 4:
                self.status = 'combofour'
                self.animation_speed = 0.25
            if self.random == 5:
                self.status = 'combofive'
                self.animation_speed = 0.25
            if self.random == 6:
                self.status = 'combosix'
                self.animation_speed = 0.25
            if self.on_ground == True:
                self.direction.y = 0
            if self.on_ground == False:
                self.direction.y = -1
            self.spamcount1 += 1
                #print(self.spamcount1)
            if self.spamcount1 in range(13, 100) and self.status == 'combo':
                self.hit1 = False
                self.spamcount1 = 0
                self.random = 2
            if self.spamcount1 in range(15, 100) and self.status == 'combotwo':
                self.hit1 = False
                self.spamcount1 = 0
                self.random = 3
            if self.spamcount1 in range(15, 100) and self.status == 'combothree':
                self.hit1 = False
                self.spamcount1 = 0
                self.random = 4
            if self.spamcount1 in range(15, 100) and self.status == 'combofour':
                self.hit1 = False
                self.spamcount1 = 0
                self.random = 5
            if self.spamcount1 in range(15, 100) and self.status == 'combofive':
                self.hit1 = False
                self.spamcount1 = 0
                self.random = 6
            if self.spamcount1 in range(15, 100) and self.status == 'combosix':
                self.hit1 = False
                self.spamcount1 = 0
                self.random = 1

        if self.allowed_attack1 == True:
            if keys[pygame.K_x]:
                self.status = 'attack1'
                self.animation_speed = 0.30
                self.direction.x = 0
                if self.on_ground == True:
                    self.direction.y = 0

        if self.b4_attack == True and self.on_screen == True and self.taking_damage2 == False and self.taking_damage1 == False:
            if keys[pygame.K_c]:
                self.status = 'b4attack'
                self.animation_speed = 0.25
                self.direction.x = 0
                if self.on_ground == True:
                    self.direction.y = 0
                self.b4_attack_count += 1
                if self.b4_attack_count in range(50, 100):
                    self.attack2 = True
                    self.b4_attack = False

            if not keys[pygame.K_c]:
                self.attack2 = False
                self.b4_attack_count = 0 

        if self.attack2 == True and self.b4_attack == False and self.on_screen == True and self.taking_damage2 == False and self.taking_damage1 == False:

            if keys[pygame.K_c]:
                self.status = 'attack2'
                self.animation_speed = 0.20
                self.direction.x = 0
                self.h2h_count += 1
                if self.on_ground == True:
                    self.direction.y = 0
                if self.move == True and self.while_hit2 == False:
                    if self.facing_right == True:
                        self.rect.x += 40
                    if self.facing_right == False:
                        self.rect.x -= 40
                if self.rect.x < 20 and self.facing_right == False:
                    self.attack2 = False
                if self.rect.x > 1075 and self.facing_right == True:
                    self.attack2 = False
        if not keys[pygame.K_c]:
            self.h2h_count = 0

        if self.limited_attack_amount > 0:
            if keys[pygame.K_TAB]:
                self.status = 'attack3'
                self.animation_speed = 0.15
                self.direction.x = 0
                if self.on_ground == True:
                    self.direction.y = 0
            
        if self.on_screen == True and self.charging == True and self.on_ground == True:
            if keys[pygame.K_s]:
                self.status = 'charge'
                self.animation_speed = .45
                self.direction.x = 0
                if self.on_ground == True:
                    self.direction.y = 0
                #self.charge += 1
            if not keys[pygame.K_s]:
                self.charging = False

        if self.teleport_count in range(4, 90) and self.taking_damage1 == False:
            self.teleport_count = 0
            if self.facing_right == True:
                self.rect.x += 225
            if self.facing_right == False:
                self.rect.x -= 225
            self.teleporting = False
        if keys[pygame.K_t]:
            if self.teleporting == True and self.b4_damage == False:
                self.status = 'teleport'
                self.animation_speed = .05
                self.teleport_count += 1
                if self.on_ground == True:
                    self.direction.y = 0
        if not keys[pygame.K_t]:
            self.teleport_count = 0
            self.teleporting = True

        if self.guard == True and self.on_screen == True and self.during_combo == False and self.during_combo2 == False:
            if keys[pygame.K_e]:
                self.status = 'guard'
                self.animation_speed = .10
                self.direction.x = 0
                if self.on_ground == True:
                    self.direction.y = 0
                self.guard_count += 1
            if self.guard_count in range(25, 100):
                self.guard_count = 0
                self.guard = False
        if not keys[pygame.K_e]:
            self.guard_count = 0
            self.guard = True

        if self.taking_damage1 == True:
            self.status = 'hitfireball'
            self.animation_speed = 0.25
            self.damagecount += 1
            if self.on_ground == True:
                self.direction.y = 0
            if self.facing_right == True:
                if self.damagecount in range(1, 28):
                    self.rect.x -= 12
            if self.facing_right == False:
                if self.damagecount in range(1, 28):
                    self.rect.x += 12
        if self.taking_damage1 == False:
            self.damagecount = 0
        
        if self.taking_damage1 == False:
            self.damagecount = 0 
        
        if self.taking_damage2 == True:
            self.status = 'hitchidori'
            self.allowed_attack1 = False
            self.direction.x = 0
            self.animation_speed = 0.20
            if self.on_ground == True:
                self.direction.y = 0
            if self.on_ground == False:
                self.direction.y = -1
        if self.taking_damage2 == False:
            self.speed = 10
            self.allowed_attack1 = True

        if self.while_hit2 == True:
            if self.b4_attack == False:
                if keys[pygame.K_c]:
                    self.status = 'whilehit2'
                    self.animation_speed = 0.15
                    self.direction.x = 0
                    self.move = False
                    if self.on_ground == True:
                        self.direction.y = 0

        if self.after_combo == True and self.taking_damage2 == False:
            self.status = 'aftercombo'
            self.animation_speed = 0.10
            self.direction.x = 0
            if self.on_ground == True:
                self.direction.y = 0
            if self.on_ground == False:
                self.direction.y = -1
            self.after_combo_count += 1
            if self.facing_right == True:
                if self.after_combo_count in range(1, 5) and self.out_of_bounds == False:
                    self.rect.x -= 5
            if self.facing_right == False:
                if self.after_combo_count in range(1, 5) and self.out_of_bounds == False:
                    self.rect.x += 5
            if self.after_combo_count in range(6, 100):
                self.after_combo = False
                self.after_combo_count = 0

        if self.after_combo2 == True and self.taking_damage2 == False:
            self.status = 'aftercombo2'
            self.animation_speed = 0.10
            self.direction.x = 0
            if self.on_ground == True:
                self.direction.y = 0
            if self.on_ground == False:
                self.direction.y = -1
            self.after_combo_count2 += 1
            if self.facing_right == True:
                if self.after_combo_count2 in range(1, 5) and self.out_of_bounds == False:
                    self.rect.x -= 5
            if self.facing_right == False:
                if self.after_combo_count2 in range(1, 5) and self.out_of_bounds == False:
                    self.rect.x += 5
            if self.after_combo_count2 in range(6, 100):
                self.after_combo2 = False
                self.after_combo_count2 = 0

        if self.b4_damage == True:
            self.status = 'b4fireball'
            self.animation_speed = 0.25
            self.direction.x = 0
            if self.on_ground == True:
                self.direction.y = 0
            if self.on_ground == False:
                self.direction.y = -1

        if self.guard_active == True:
            self.status = 'guardfireball'
            self.animation_speed = 0.15
            self.direction.x = 0
            if self.on_ground == True:
                self.direction.y = 0
            if self.on_ground == False:
                self.direction.y = -1

        if self.special == True:
            if keys[pygame.K_r]:
                self.status = 'b4special'
                self.animation_speed = 0.20
                self.direction.x = 0 
                if self.on_ground == True:
                    self.direction.y = 0
                self.special_count += 1
                #print(self.special_count)
                if self.special_count in range(60, 100):
                    self.special = False
                    self.special_activate = True
    
            if not keys[pygame.K_r]:
                self.special_count = 0
                self.special_activate = False

        if self.special_activate == True and self.special == False:
            if keys[pygame.K_r]:
                self.status = 'special'
                self.animation_speed = 0.10
                self.direction.x = 0
                if self.on_ground == True:
                    self.direction.y = 0
                          
            if not keys[pygame.K_r]:
                self.special = True
                self.special_activate = False

        if self.guarded_combo == True:
            self.status = 'guardstall'
            self.animation_speed = 0.10
            self.guarded_combo_count += 1
            self.direction.x = 0
            if self.on_ground == True:
                self.direction.y = 0
            if self.facing_right == True:
                if self.guarded_combo_count in range(1, 30) and self.out_of_bounds == False:
                    self.rect.x -= 6
            if self.facing_right == False:
                if self.guarded_combo_count in range(1, 30) and self.out_of_bounds == False:
                    self.rect.x += 6
            if self.guarded_combo_count in range(31, 100):
                self.guarded_combo = False
                self.guarded_combo_count = 0
        
    def apply_gravity(self):
        if self.on_ground == False:
            self.direction.y += self.gravity
            self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def super_charge(self):

        if self.status == 'charge':
            self.charge += 1

        if self.charge >= 275 and self.level == 1:
            self.charge = 0
            self.level += 1
        if self.charge >= 275 and self.level == 2:
            self.charge = 0
            self.level += 1
        if self.charge >= 275 and self.level == 3:
            self.charge = 0
            self.level += 1
        if self.charge >= 275 and self.level == 4:
            self.charge = 0
            self.level -= 3

        if self.level == 3 and self.charge >= 274 and self.special_activate == False:
            self.charging = False
            self.special = True
            self.special_available = True
            self.level = 3
        else:
            self.special = False
            self.charging = True
            self.special_available = False

    def health(self, damage):
        self.damage = damage
        if self.max_health > 0: 
            if self.status == 'attack':
                self.max_health += 0
            if self.status == 'attack2':
                self.max_health += 0
            if self.status == 'guardattack2':
                self.max_health += 0
            else:
                self.max_health -= self.damage

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()

        self.super_charge()

class Player2(pygame.sprite.Sprite):
    def __init__(self, name, pos):
        pygame.sprite.Sprite.__init__(self)
        self.import_character_assets()

        #### STATE ####

        self.name = name
        self.frame_index = 0
        self.animation_speed = 0.12
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 12
        self.gravity = 1.2
        self.jump_speed = -25

        self.status = 'idle'
        self.facing_right = False
        self.running = False
        self.on_ground = True
        self.on_ceiling = False
        self.on_right = False
        self.on_left = False

        self.level = 1
        self.charge = 275

        self.max_health = 0

        #### ATTACKS ####

        self.attack1 = True
        self.b4_attack_count = 0
        self.b4_attack = True
        self.initiate_attack_count = 0
        self.initiate_damage_state = False
        self.initiate_damage_count = 0 
        self.hitb4 = False

        self.special = False
        self.special_activate = False
        self.special_available = False
        self.special_available_count = 0
        self.charging = True
        self.special_count = 0
        self.in_special_count = 0
        self.special_successful = False

        self.attack2 = False
        self.attack2right = False

        self.fireball = False
        self.fireball_count = 0

        self.activate = False
        self.allowed_attack2 = True

        self.move = True

        self.h2h_count = 0

        self.animation_state = True

        self.attack2count = 0
        self.attackcount = 0

        self.attack3 = True
        self.attack3right = True
        self.attack3count = 0
        self.attack3allowed = False
        self.attack3_allowed_count = 0

        self.limit_attack = False
        self.limited_attack_count = 0
        self.limited_attack_amount = 3

        #### TELEPORT ####

        self.teleporting = False  
        self.teleport_count = 0 

        #### GUARD ####

        self.guard_count = 0
        self.guard = True
        self.guard_active = False
        self.guard_active_count = 0
        self.guard_successful = False
        self.guarded_combo = False
        self.guarded_combo_count = 0

        #### TAKING DAMAGE ####

        self.hit_by_special = False
        self.hit_special_count = 0
        self.hit_special_activate = False
        self.hit_activate_count = 0

        self.taking_damage1 = False
        self.taking_damage2 = False

        self.during_combo = False
        self.during_combo2 = False
        self.combo_count = 0
        self.combo_count2 = 0
        self.after_combo = False
        self.after_combo2 = False
        self.after_combo_count = 0
        self.after_combo_count2 = 0

        self.taking_damage1 = False

        self.damagecount = 0

        self.b4_damage = False

        #### COMBOS ####

        self.spamcount1 = 0
        self.spamcount2 = 0

        self.count = 0
        self.count2 = 0
        
        self.hit1 = False
        self.hit2 = True

        self.hit_count = 0
        self.in_combo = False
        self.combo_timer = 0
        self.add_combo_count = False
        self.in_air = False

        self.random = 1

        #### POSITIONING ####

        self.stopped = False

        self.on_screen = True

        self.in_range = False
        self.in_range2 = False

        self.out_of_bounds = False

        self.stall = False
        self.stall2 = False

        self.state1 = False
        self.state2 = False

    def import_character_assets(self):
        character_path = '/Users/charlieyorke/ace/imgs/Sasuke/'
        self.animations = {'idle': [], 'run': [], 'guardstall': [], 'combotwo': [], 'combothree': [], 'combofour': [], 'combofive': [], 'combosix': [], 'jump': [], 'special': [], 'b4special': [], 'hitspecial': [], 'guardrasengan': [], 'b4rasengan': [], 'newcombo1': [], 'aftercombo': [], 'aftercombo2': [], 'hitb4': [], 'b4attack1': [], 'attack1': [], 'attack2': [], 'attack3': [], 'charge': [], 'flinch': [], 'combo': [], 'guard': [], 'teleport': [], 'hitrasengan': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

        if self.on_ceiling:
            self.rect = self.image.get_rect(bottom = self.rect.bottom)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        else:
            self.rect = self.image.get_rect(center = self.rect.center)
    
    def get_input(self):
        keys = pygame.key.get_pressed()

        if self.on_screen == True and self.status != 'b4rasengan' and self.status != 'hitrasengan' and self.status != 'combo' and self.status != 'combotwo' and self.after_combo == False and  self.after_combo2 == False and self.b4_damage == False:
            if keys[pygame.K_RIGHT] and self.rect.x < 1150 and self.stall == False and self.stall2 == False and self.stopped == False:
                self.direction.x = 1.0
                self.facing_right = True

            elif keys[pygame.K_LEFT] and self.rect.x > 1 and self.stall == False and self.stall2 == False and self.stopped == False:
                self.direction.x = -1.0
                self.facing_right = False
            
            else:
                self.direction.x = 0

        if self.on_screen == False:
            self.direction.x = 0
        if self.status == 'hitrasengan':
            self.direction.x = 0

        if self.in_air == True:
            self.direction.y = -1
        if self.move == False:
            self.direction.x = 0
        
        if keys[pygame.K_UP] and self.on_ground == True:
            if self.rect.bottom <= 698:
                self.on_ground = False
                self.jump()

    def get_status(self):

        keys = pygame.key.get_pressed()

        if self.direction.y < 0:
            self.status = 'jump'
            self.animation_speed = .20
        
        else:
            if self.direction.x != 0:
                self.status = 'run'
                self.animation_speed = .20
            else:
                self.status = 'idle'
                self.animation_speed = 0.20

        if keys[pygame.K_RSHIFT]:
            self.hit1 = True

        if self.hit1 == True:           
            if self.random == 1:
                self.status = 'combo'
                self.animation_speed = 0.25
            if self.random == 2:
                self.status = 'combotwo'
                self.animation_speed = 0.25
            if self.random == 3:
                self.status = 'combothree'
                self.animation_speed = 0.25
            if self.random == 4:
                self.status = 'combofour'
                self.animation_speed = 0.25
            if self.random == 5:
                self.status = 'combofive'
                self.animation_speed = 0.25
            if self.random == 6:
                self.status = 'combosix'
                self.animation_speed = 0.25
            if self.on_ground == True:
                self.direction.y = 0
            if self.on_ground == False:
                self.direction.y = -1
            self.spamcount1 += 1
                #print(self.spamcount1)
            if self.spamcount1 in range(13, 100) and self.status == 'combo':
                self.hit1 = False
                self.spamcount1 = 0
                self.random = 2
            if self.spamcount1 in range(15, 100) and self.status == 'combotwo':
                self.hit1 = False
                self.spamcount1 = 0
                self.random = 3
            if self.spamcount1 in range(15, 100) and self.status == 'combothree':
                self.hit1 = False
                self.spamcount1 = 0
                self.random = 4
            if self.spamcount1 in range(15, 100) and self.status == 'combofour':
                self.hit1 = False
                self.spamcount1 = 0
                self.random = 5
            if self.spamcount1 in range(15, 100) and self.status == 'combofive':
                self.hit1 = False
                self.spamcount1 = 0
                self.random = 6
            if self.spamcount1 in range(15, 100) and self.status == 'combosix':
                self.hit1 = False
                self.spamcount1 = 0
                self.random = 1

        if self.b4_attack == True and self.on_screen == True and self.b4_damage == False and self.taking_damage1 == False and self.hitb4 == False:

            if keys[pygame.K_SLASH]:
                self.status = 'b4attack1'
                self.animation_speed = 0.25
                self.allowed_attack2 = False
                self.attack1 = False
                self.direction.x = 0
                if self.on_ground == True:
                    self.direction.y = 0
                self.b4_attack_count += 1
                if self.b4_attack_count in range(50, 100):
                    self.attack1 = True
                    self.b4_attack = False

            if not keys[pygame.K_SLASH]:
                self.attack1 = False
                self.b4_attack_count = 0 
                self.allowed_attack2 = True

        if self.attack1 == True and self.b4_attack == False and self.on_screen == True and self.b4_damage == False and self.taking_damage1 == False and self.hitb4 == False:

            if keys[pygame.K_SLASH]:
                self.status = 'attack1'
                self.animation_speed = 0.15
                self.allowed_attack2 = False
                self.attackcount += 1
                self.h2h_count += 1
                if self.on_ground == True:
                    self.direction.y = 0
                if self.move == True and self.stopped == False:
                    if self.facing_right == True:
                        self.rect.x += 40
                    if self.facing_right == False:
                        self.rect.x -= 40
                if self.move == False:
                    self.direction.x = 0
                if self.rect.x < 20 and self.facing_right == False:
                    self.attack1 = False
                if self.rect.x > 1075 and self.facing_right == True:
                    self.attack1 = False
        if not keys[pygame.K_SLASH]:
            self.h2h_count = 0
            self.allowed_attack2 = True

        if self.allowed_attack2 == True and self.animation_state == True:
            if keys[pygame.K_PERIOD]:
                self.status = 'attack2'
                self.animation_speed = 0.30
                if self.on_ground == True:
                    self.direction.y = 0
                self.attack2count += 1

        if self.attack3 == True and self.limited_attack_amount > 0:
            if keys[pygame.K_QUOTE]:
                self.status = 'attack3'
                self.animation_speed = 0.20
                self.direction.x = 0
                if self.on_ground == True:
                    self.direction.y = 0
        if not keys[pygame.K_QUOTE]:
            self.attack3count = 0
            self.attack3 = True
            
        if self.on_screen == True and self.charging == True and self.on_ground == True:
            if keys[pygame.K_DOWN]:
                self.status = 'charge'
                self.animation_speed = .45
                self.direction.x = 0
                if self.on_ground == True:
                    self.direction.y = 0
                #self.charge -= 1
                #print(self.charge)
        
        if self.teleport_count in range(4, 90):
            self.teleport_count = 0
            if self.facing_right == True:
                self.rect.x += 225
            if self.facing_right == False:
                self.rect.x -= 225
            self.teleporting = False
        if keys[pygame.K_COMMA]:
            if self.teleporting == True:
                self.status = 'teleport'
                self.animation_speed = 0.10
                self.teleport_count += 1
                if self.on_ground == True:
                    self.direction.y = 0
        if not keys[pygame.K_COMMA]:
            self.teleport_count = 0
            self.teleporting = True

        if self.guard == True and self.on_screen == True:
            if keys[pygame.K_SEMICOLON]:
                self.status = 'guard'
                self.animation_speed = 0.10
                self.direction.x = 0
                if self.on_ground == True:
                    self.direction.y = 0
                self.guard_count += 1 
            if self.guard_count in range(31, 100):
                self.guard_count = 0
                self.guard = False
        if not keys[pygame.K_SEMICOLON]:
            self.guard_count = 0
            self.guard = True

        if self.taking_damage1 == True:
            self.status = 'hitrasengan'
            self.animation_speed = 0.25
            self.allowed_attack2 = False
            self.damagecount += 1
            self.charging = False
            if self.on_ground == True:
                self.direction.y = 0
            if self.facing_right == True:
                if self.damagecount in range(1, 28):
                    self.rect.x -= 12
            if self.facing_right == False:
                if self.damagecount in range(1, 28):
                    self.rect.x += 12
        if self.taking_damage1 == False:
            self.damagecount = 0
            self.allowed_attack2 = True

        if self.hitb4 == True:
            self.status = 'hitb4'
            self.animation_speed = 0.15
            self.direction.x = 0
            if self.on_ground == True:
                self.direction.y = 0

        if self.after_combo == True:
            self.status = 'aftercombo'
            self.animation_speed = 0.10
            self.direction.x = 0
            self.charging = False
            if self.on_ground == True:
                self.direction.y = 0
            self.after_combo_count += 1
            if self.facing_right == True:
                if self.after_combo_count in range(1, 5):
                    self.rect.x -= 5
            if self.facing_right == False:
                if self.after_combo_count in range(1, 5):
                    self.rect.x += 5
            if self.after_combo_count in range(6, 100):
                self.after_combo = False
                self.after_combo_count = 0

        if self.after_combo2 == True:
            self.status = 'aftercombo2'
            self.animation_speed = 0.10
            self.direction.x = 0
            self.charging = False
            if self.on_ground == True:
                self.direction.y = 0
            self.after_combo_count2 += 1
            if self.facing_right == True:
                if self.after_combo_count2 in range(1, 5):
                    self.rect.x -= 7
            if self.facing_right == False:
                if self.after_combo_count2 in range(1, 5):
                    self.rect.x += 7
            if self.after_combo_count2 in range(6, 100):
                self.after_combo2 = False
                self.after_combo_count2 = 0

        if self.b4_damage == True:
            self.status = 'b4rasengan'
            self.animation_speed = 0.30
            self.attack1 = False
            self.direction.x = 0
            self.charging = False
            if self.on_ground == True:
                self.direction.y = 0
            if self.on_ground == False:
                self.direction.y = -1

        if self.guard_active == True:
            self.status = 'guardrasengan'
            self.animation_speed = 0.40
            self.direction.x = 0 
            self.charging = False
            if self.on_ground == True:
                self.direction.y = 0
            if self.on_ground == False:
                self.direction.y = -1 

        if self.hit_by_special == True:
            self.status = 'hitspecial'
            self.animation_speed = 0.30
            self.direction.x = 0
            self.charging = False
            if self.on_ground == True:
                self.direction.y = 0
            self.hit_special_count += 1

        if self.special == True:
            if keys[pygame.K_i]:
                self.status = 'b4special'
                self.animation_speed = 0.20
                self.direction.x = 0
                if self.on_ground == True:
                    self.direction.y = 0
                self.special_count += 1
                if self.special_count in range(60, 100):
                    self.special = False
                    self.special_activate = True
            if not keys[pygame.K_i]:
                self.special_count = 0
                self.special_activate = False

        if self.special_activate == True and self.special == False:
            if keys[pygame.K_i]:
                self.status = 'special'
                self.animation_speed = 0.20
                self.direction.x = 0
                if self.on_ground == True:
                    self.direction.y = 0

        if self.guarded_combo == True:
            self.status = 'guardstall'
            self.animation_speed = 0.10
            self.guarded_combo_count += 1
            self.direction.x = 0
            if self.on_ground == True:
                self.direction.y = 0
            if self.facing_right == True:
                if self.guarded_combo_count in range(1, 30) and self.out_of_bounds == False:
                    self.rect.x -= 6
            if self.facing_right == False:
                if self.guarded_combo_count in range(1, 30) and self.out_of_bounds == False:
                    self.rect.x += 6
            if self.guarded_combo_count in range(31, 100):
                self.guarded_combo = False
                self.guarded_combo_count = 0

    def apply_gravity(self):
        if self.on_ground == False:
            self.direction.y += self.gravity
            self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def super_charge(self):

        if self.status == 'charge':
            self.charge -= 1
        
        if self.status != 'comboscene1' and self.status != 'comboscene2' and self.status != 'comboscene3' and self.status != 'combo2scene1' and self.status != 'combo2scene2' and self.status != 'combo2scene3':   
            if self.charge <= 0 and self.level == 1:
                self.charge = 275
                self.level += 1
                self.special = False
                self.special_available = False
                #print(self.level)
            if self.charge <= 0 and self.level == 2:
                self.charge = 275
                self.level += 1
                self.special = False
                self.special_available = False
            if self.charge <= 0 and self.level == 3:
                self.charge = 275
                self.level -= 2

        if self.level == 3 and self.charge <= 1 and self.special_activate == False:
            self.charging = False
            self.special = True
            self.special_available = True
            self.level = 3
        else:
            self.special = False
            self.charging = True
            self.special_available = False
        
    def health(self, damage):
        self.damage = damage
        if self.max_health < 410:
            if self.status == 'attack':
                self.max_health += 0
            if self.status == 'attack2':
                self.max_health += 0
            else:
                self.max_health += self.damage

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()

        self.super_charge()

class Level:
    def __init__(self, surface):
        # level setup
        self.display_surface = surface
        self.setup_level()
        self.world_shift = 0
        self.running = True
        self.p1_winner = False
        self.p2_winner = False
        self.gameover = False
        self.map1 = False
        self.map2 = False
        self.speed_increase = False

    def setup_level(self):
        n_x = 100
        n_y = 200

        s_x = 1050
        s_y = 200
        #print(y)

        self.player = pygame.sprite.GroupSingle()
        self.player2 = pygame.sprite.GroupSingle()
       
        player_sprite = Player('Naruto', (n_x, n_y))
        player2_sprite = Player2('Sasuke', (s_x, s_y))
        
        self.player.add(player_sprite)
        self.player2.add(player2_sprite)

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        player2 = self.player2.sprite
        player2.rect.x += player2.direction.x * player2.speed

    def vertical_movement_collision(self):
        player = self.player.sprite
        player2 = self.player2.sprite

        #print(player.rect.bottom)

        #### PLAYER 1 ####
        if player.direction.y == 0:
            player.on_ground = True
            player.rect.bottom = 698

        elif player.rect.bottom <= 698:
            player.apply_gravity()
        
        else:
            player.on_ground = True
            player.rect.bottom = 698
            #player.direction.y = 0

        #### PLAYER 2 ####
        if player2.direction.y == 0:
            player2.on_ground = True
            player2.rect.bottom = 698

        elif player2.rect.bottom <= 698:
            player2.apply_gravity()
        
        else:
            player2.on_ground = True
            player2.rect.bottom = 698
                  
    def adding_attacks(self):
        player = self.player.sprite
        player2 = self.player2.sprite

        keys = pygame.key.get_pressed()

        #### PLAYER 2 ####

        if player2.status == 'attack2' and player2.facing_right == False:

            player2.attack2 = True

        if player2.status == 'attack2' and player2.facing_right == True:

            player2.attack2right = True

        if player2.attack2 == True and player2.allowed_attack2 == True:

            screen.blit(fire_ball, (fire_ball_rect))
           
            fire_ball_rect.x -= 30
        
        if player2.attack2 == False:

            fire_ball_rect.topleft = (player2.rect.x - 10, player2.rect.y + 10)

        if player2.attack2right == True:
            
            screen.blit(flip_fire_ball, (flip_fire_ball_rect))

            flip_fire_ball_rect.x += 30

        if player2.attack2right == False:

            flip_fire_ball_rect.topleft = (player2.rect.x + 20, player2.rect.y + 10)

        #### PLAYER 1 ####

        if player.status == 'attack1' and player.facing_right == False:

            player.attack1 = True

        if player.status == 'attack1' and player.facing_right == True:

            player.attack1right = True

        if player.attack1 == True and player.allowed_attack1 == True:

            screen.blit(flip_rasengan, (flip_rasengan_rect))

            flip_rasengan_rect.x -= 30

        if player.attack1 == False:

            flip_rasengan_rect.topleft = (player.rect.x - 10, player.rect.y - 15)

        if player.attack1right == True:

            screen.blit(rasengan, (rasengan_rect_new))

            rasengan_rect_new.x += 30

        if player.attack1right == False:

            rasengan_rect_new.topleft = (player.rect.x + 10, player.rect.y - 15)
        
    def collisions(self):
        player = self.player.sprite
        player2 = self.player2.sprite

        keys = pygame.key.get_pressed()

        if pygame.sprite.collide_mask(player, player2) and keys[pygame.K_PERIOD] and player.status != 'guardattack2' and player.status != 'guard' and player.status != 'teleport':
            player.taking_damage1 = True

            #player.health(25)

        else:
            player.taking_damage1 = False


        if pygame.sprite.collide_mask(player, player2) and keys[pygame.K_x]:
            player2.taking_damage1 = True

        else:
            player2.taking_damage1 = False

    def player_ranged_attacks(self):
        player = self.player.sprite
        player2 = self.player2.sprite

        keys = pygame.key.get_pressed()

        if pygame.Rect.colliderect(player.rect, fire_ball_rect) and player2.attack2 == True and player.status != 'teleport' and player.status != 'attack2' and player.status != 'guard' and player.status != 'guardfireball':
            player2.attack2 = False
            fire_ball_rect.topleft = (player2.rect.x - 10, player2.rect.y + 40)
            player.taking_damage1 = True
            player2.fireball = True
            player2.allowed_attack2 = False
            player.facing_right = True
            if player.status == 'b4attack':
                player.attack2 = False
                player.move = False
                player.b4_attack = False
                player2.fireball = True

        if pygame.Rect.colliderect(player.rect, flip_fire_ball_rect) and player2.attack2right == True and player.status != 'teleport' and player.status != 'guard':
            player2.attack2right = False
            flip_fire_ball_rect.topleft = (player2.rect.x + 20, player2.rect.y + 40)
            player.taking_damage1 = True
            player2.fireball = True
            player.facing_right = False

        if player2.fireball == True:
            player2.fireball_count += 1
        if player2.fireball_count in range(1, 16):
            player2.fireball = True
            player2.allowed_attack2 = False
            player.b4_damage = True
        if player2.fireball_count in range(17, 104):
            player2.allowed_attack2 = False
            player.b4_damage = False
            player.taking_damage1 = True
            player2.fireball_count += 1
        if player2.fireball_count >= 104:
            player2.fireball_count = 0
            player2.allowed_attack2 = True
            player2.fireball = False

        if player2.fireball == False:
            player.taking_damage1 = False

        if fire_ball_rect.x < 10:
            player2.attack2 = False
            if keys[pygame.K_PERIOD]:
                player2.animation_state = False
        if not keys[pygame.K_PERIOD]:
            player2.animation_state = True
        if flip_fire_ball_rect.x > 1150:
            player2.attack2right = False
            if keys[pygame.K_PERIOD]:
                player2.animation_state = False
        if not keys[pygame.K_PERIOD]:
            player2.animation_state = True

        ###################################################################################

        if pygame.Rect.colliderect(player2.rect, rasengan_rect_new) and player.attack1right == True and player2.status != 'teleport' and player2.status != 'attack1' and player2.status != 'guard':
            player.attack1right = False
            rasengan_rect_new.topleft = (player.rect.x + 10, player.rect.y - 15)
            player.allowed_attack1 = False
            player2.facing_right = False
            player.rasengan = True
            player2.taking_damage1 = True
            player2.health(5)

        if pygame.Rect.colliderect(player2.rect, flip_rasengan_rect) and player.attack1 == True and player2.status != 'teleport' and player2.status != 'attack1' and player2.status != 'guard':
            player.attack1 = False
            rasengan_rect_new.topleft = (player.rect.x - 10, player.rect.y - 15)
            player.allowed_attack1 = False
            player2.facing_right = True
            player.rasengan = True
            player2.taking_damage1 = True
            player2.health(5)

        if player.rasengan == True:
            player.rasengan_count += 1
        if player.rasengan_count in range(1, 25):
            player.rasengan = True
            player.allowed_attack1 = False
            player2.b4_damage = True
        if player.rasengan_count in range(26, 114):
            player2.b4_damage = False
            player2.taking_damage1 = True
            player.rasengan_count += 1
        if player.rasengan_count >= 114:
            player.rasengan_count = 0
            player.allowed_attack1 = True
            player.rasengan = False
            player.attack3right = False
            player.clone_movement = False
            player.clone = True
            player.shuriken = False
        
        if flip_rasengan_rect.x < 10:
            player.attack1 = False
        if rasengan_rect_new.x > 1150:
            player.attack1right = False

        ###################################################################################
       
        if pygame.Rect.colliderect(player.rect, fire_ball_rect) and player.status == 'guard':
            if fire_ball_rect.x == player2.rect.x - 10:
                player.guard_successful = False
                player.guard_active_count = 0
                player.guard_active = False
            else:
                player2.attack2 = False
                player2.allowed_attack2 = False
                player.guard_successful = True
                fire_ball_rect.topleft = (player2.rect.x - 10, player2.rect.y + 40)
                if player2.facing_right == False:
                    if player.facing_right == False:
                        player.guard_successful = False
                        player2.fireball = True
                        player.facing_right = True

        if pygame.Rect.colliderect(player.rect, flip_fire_ball_rect) and player.status == 'guard':
            if flip_fire_ball_rect.x == player2.rect.x + 20:
                player.guard_successful = False
                player.guard_active_count = 0
                player.guard_active = False
            else:
                player2.attack2right = False
                player2.allowed_attack2 = False
                player.guard_successful = True
                flip_fire_ball_rect.topleft = (player2.rect.x + 20, player2.rect.y + 40)
                if player2.facing_right == True:
                    if player.facing_right == True:
                        player.guard_successful = False
                        player2.fireball = True
                        player.facing_right = False

        if player.guard_successful == True:
            player.guard_active_count += 1

        if player.guard_active_count in range(1, 16):
            player2.allowed_attack2 = False
            player.guard_successful = True
            player.guard_active = True
        if player.guard_active_count in range(17, 50):
            player.guard_successful = True
            player.guard_active = False
        if player.guard_active_count >= 50:
            player.guard_successful = False
            player.guard_active_count = 0
            player.guard_active = False
            player2.allowed_attack2 = True

        ###################################################################################

        if pygame.Rect.colliderect(player2.rect, rasengan_rect_new) and player2.status == 'guard':
            if rasengan_rect_new.x == player.rect.x + 10:
                player2.guard_successful = False
                player2.guard_active_count = 0
                player2.guard_active = False
            else:
                player.attack1right = False
                player2.guard_successful = True
                rasengan_rect_new.topleft = (player.rect.x + 10, player.rect.y - 15)
                if player.facing_right == True:
                    if player2.facing_right == True:
                        player2.guard_successful = False
                        player.rasengan = True
                        player2.facing_right = False

        if pygame.Rect.colliderect(player2.rect, flip_rasengan_rect) and player2.status == 'guard':
            if flip_rasengan_rect.x == player.rect.x - 10:
                player2.guard_successful = False
                player2.guard_active_count = 0
                player2.guard_active = False
            else:
                player.attack1 = False
                player2.guard_successful = True
                flip_rasengan_rect.topleft = (player.rect.x - 10, player.rect.y - 15)
                if player.facing_right == False:
                    if player2.facing_right == False:
                        player2.guard_successful = False
                        player.rasengan = True
                        player2.facing_right = True

        if player2.guard_successful == True:
            player2.guard_active_count += 1

        if player2.guard_active_count in range(1, 16):
            player.allowed_attack1 = False
            player2.guard_successful = True
            player2.guard_active = True
        if player2.guard_active_count in range(17, 50):
            player2.guard_successful = True
            player2.guard_active = False
            player2.guard = False
        if player2.guard_active_count >= 50:
            player2.guard_successful = False
            player2.guard_active_count = 0
            player2.guard_active = False
            player.allowed_attack1 = True

        ###################################################################################

        if pygame.Rect.colliderect(rasengan_rect_new, fire_ball_rect) and player.attack1right == True and player2.attack2 == True and player2.status != 'guard' and player2.status != 'guardrasengan':
            player.attack1right = False
            player2.attack2 = False
    
    def player_after_combo_state(self):
        player = self.player.sprite
        player2 = self.player2.sprite

        keys = pygame.key.get_pressed()
        
        if player2.during_combo == True:
            player2.combo_count += 1

        if player2.combo_count in range(1, 30):
            player2.after_combo = True
        if player2.combo_count in range(31, 100):
            player2.during_combo = False
            player2.after_combo = False
            player2.combo_count = 0

        if player2.during_combo2 == True:
            player2.combo_count2 += 1

        if player2.combo_count2 in range(1, 30):
            player2.after_combo2 = True
        if player2.combo_count2 in range(31, 100):
            player2.during_combo2 = False
            player2.after_combo2 = False
            player2.combo_count2 = 0
        
        if player.during_combo == True:
            player.combo_count += 1
            #print(player.combo_count)

        if player.combo_count in range(1, 30):
            player.after_combo = True
        if player.combo_count in range(31, 100):
            player.during_combo = False
            player.after_combo = False
            player.combo_count = 0

        if player.during_combo2 == True:
            player.combo_count2 += 1 

        if player.combo_count2 in range(1, 30):
            player.after_combo2 = True
        if player.combo_count2 in range(31, 100):
            player.during_combo2 = False
            player.after_combo2 = False
            player.combo_count2 = 0 

        ###################################################################################

        if player2.rect.centerx < player.rect.centerx and player2.teleporting == False:
            player2.in_range = True
            player2.in_range2 = False
        if player2.rect.centerx > player.rect.centerx and player2.teleporting == False:
            player2.in_range2 = True
            player2.in_range = False

        if player2.in_range == True:
            if player.rect.x in range(player2.rect.x + 700) and player2.teleporting == False:
                if player2.facing_right == False:
                    player2.rect.x = player.rect.x - 65
                    player2.facing_right = True
        if player2.in_range2 == True:
            if player.rect.x in range(player2.rect.x + 700) and player2.teleporting == False:
                if player2.facing_right == True:
                    player2.rect.x = player.rect.x + 65
                    player2.facing_right = False

        if player.rect.centerx < player2.rect.centerx and player.teleporting == False:
            player.in_range = True
            player.in_range2 = False
        if player.rect.centerx > player2.rect.centerx and player.teleporting == False:
            player.in_range2 = True
            player.in_range = False

        if player.in_range == True:
            if player2.rect.x in range(player.rect.x + 700) and player.teleporting == False:
                if player.facing_right == False:
                    player.rect.x = player.rect.x - 10
                    player.facing_right = True
        if player.in_range2 == True:
            if player2.rect.x in range(player.rect.x + 700) and player.teleporting == False:
                if player.facing_right == True:
                    player.rect.x = player.rect.x + 10
                    player.facing_right = False

    def player_special_attacks(self):
        player = self.player.sprite
        player2 = self.player2.sprite

        if player.status == 'special':
            player.special_successful = True

        if player.special_successful == False:
            n_special1_rect.topleft = (player.rect.x - 15, player.rect.y - 45)

        if player.special_successful == True:
            if player.facing_right == True:
                screen.blit(n_special1, (n_special1_rect))
                n_special1_rect.x += 25
            if player.facing_right == False:
                screen.blit(n_special2, (n_special2_rect))
                n_special2_rect.x -= 25
    
        if pygame.Rect.colliderect(player2.rect, n_special1_rect) and player.special_successful == True:
            player.special_successful = False
            player.special_active = False
            player2.hit_special_activate = True

        if player2.hit_special_activate == True:
            player2.hit_activate_count += 1

        if player2.hit_activate_count >= 1:
            player2.hit_special_activate = True
        if player2.hit_activate_count in range(1, 25):
            player2.hit_by_special = True
            player.special_successful = False
            player.special_active = False
        if player2.hit_activate_count in range(26, 76):
            player2.taking_damage1 = True
            player2.hit_by_special = False
            player.special_successful = False
            player.special_active = False
        if player2.hit_activate_count >= 76:
            player2.hit_special_activate = False
            player2.hit_activate_count = 0
            player2.taking_damage1 = False
            player.level = 1
            player.charge = 0

        ###################################################################################

        if player2.status == 'special' and player2.special_activate == True:
            player2.special_successful = True

        if player2.special_successful == True:
            player2.in_special_count += 1

        if player2.in_special_count >= 1:
            player2.special_successful = True

        if player2.special_successful == True:
            if player2.in_special_count in range(1, 5):
                s_special1_rect.center = (100, 0)
                screen.blit(s_special1, (100, 0))
                screen.blit(s_special1, (500, 0))
                screen.blit(s_special1, (900, 0))
            if player2.in_special_count in range(6, 10):
                screen.blit(s_special2, (100, 0))
                screen.blit(s_special2, (500, 0))
                screen.blit(s_special2, (900, 0))
            if player2.in_special_count in range(11, 15):
                screen.blit(s_special3, (100, 0))
                screen.blit(s_special3, (500, 0))
                screen.blit(s_special3, (900, 0))
            if player2.in_special_count in range(16, 20):
                screen.blit(s_special4, (s_special4_rect))
                screen.blit(s_special4, (s_special4_rect2))
                screen.blit(s_special4, (s_special4_rect3))
            if player2.in_special_count in range(21, 25):
                screen.blit(s_special5, (100, 0))
                screen.blit(s_special5, (500, 0))
                screen.blit(s_special5, (900, 0))
            if player2.in_special_count in range(26, 30):
                screen.blit(s_special6, (100, 0))
                screen.blit(s_special6, (500, 0))
                screen.blit(s_special6, (900, 0))
            if player2.in_special_count in range(31, 35):
                screen.blit(s_special7, (100, 0))
                screen.blit(s_special7, (500, 0))
                screen.blit(s_special7, (900, 0))
            if player2.in_special_count in range(36, 40):
                screen.blit(s_special8, (100, 0))
                screen.blit(s_special8, (500, 0))
                screen.blit(s_special8, (900, 0))
            if player2.in_special_count >= 40:
                player2.special_available = False
                player2.special_successful = False
                player2.in_special_count = 0
                player2.special = False
                player2.special_activate = False
                player2.level = 1
                player2.charge = 234
                player2.special_available_count = 0
       
    def combos(self):
        player = self.player.sprite
        player2 = self.player2.sprite

        keys = pygame.key.get_pressed()

        # PLAYER 2 COMBOS #
        ###################################################################################

        if player.combo_count in range(1, 25):
            player2.stall = True
        else:
            player2.stall = False
        
        if player.combo_count2 in range(1, 25):
            player2.stall2 = True
        else:
            player2.stall2 = False

        if pygame.sprite.collide_mask(player2, player):
            if player2.status == 'combo' or player2.status == 'combotwo' or player2.status == 'combothree' or player2.status == 'combofour' or player2.status == 'combofive' or player2.status == 'combosix':
                if player.status != 'guard':
                    if player2.facing_right == False:
                        player.facing_right = True
                    if player2.facing_right == True:
                        player.facing_right = False

        if player.guarded_combo == True:
            player2.stopped = True
        if player.guarded_combo == False:
            player2.stopped = False

        if pygame.sprite.collide_mask(player2, player) and player2.status == 'combo': 
            if player.status == 'guard':
                if player.facing_right == True and player2.facing_right == False:
                    player.during_combo2 = False
                    player.guarded_combo = True
                    player2.direction.x = 0
                if player.facing_right == False and player2.facing_right == True:
                    player.during_combo2 = False
                    player.guarded_combo = True
                    player2.direction.x = 0
                if player.facing_right == False and player2.facing_right == False:
                    player.during_combo2 = True
                    player.facing_right = True
                if player.facing_right == True and player2.facing_right == True:
                    player.during_combo2 = True
                    player.facing_right = False
            if player.status == 'attack2':
                player.during_combo2 = False
                player.move = False
            if player.status == 'b4attack':
                player.b4_attack = False
                player.b4_attack_count = 0
                player.attack2 = False
            else:
                player.during_combo2 = True
                player2.direction.x = 0
                if player2.rect.x in range(player.rect.x + 60):
                    player2.stall = True
                    if player2.facing_right == True:
                        player.rect.x = player.rect.x + 2
                    if player2.facing_right == False:
                        player.rect.x = player.rect.x - 2
                if keys[pygame.K_RSHIFT]:
                    player2.direction.x = 0

        if pygame.sprite.collide_mask(player2, player) and player2.status == 'combotwo':
            player.during_combo = True
            if player.status == 'guard':
                if player.facing_right == True and player2.facing_right == False:
                    player.during_combo = False
                    player.guarded_combo = True
                    player2.direction.x = 0
                if player.facing_right == False and player2.facing_right == True:
                    player.during_combo = False
                    player.guarded_combo = True
                    player2.direction.x = 0
                if player.facing_right == False and player2.facing_right == False:
                    player.during_combo = True
                    player.facing_right = True
                if player.facing_right == True and player2.facing_right == True:
                    player.during_combo = True
                    player.facing_right = False
            if player.status == 'attack2':
                player.during_combo = False
                player.move = False
            if player.status == 'b4attack':
                player.b4_attack = False
                player.b4_attack_count = 0
                player.attack2 = False
            else:
                player.during_combo = True
                player2.direction.x = 0
                if player2.rect.x in range(player.rect.x + 60):
                    player2.stall = True
                    if player2.facing_right == True:
                        player.rect.x = player.rect.x + 2
                    if player2.facing_right == False:
                        player.rect.x = player.rect.x - 2
                if keys[pygame.K_RSHIFT]:
                    player2.direction.x = 0

        if pygame.sprite.collide_mask(player2, player) and player2.status == 'combothree':
            if player.status == 'guard':
                if player.facing_right == True and player2.facing_right == False:
                    player.during_combo2 = False
                    player.guarded_combo = True
                    player2.direction.x = 0
                if player.facing_right == False and player2.facing_right == True:
                    player.during_combo2 = False
                    player.guarded_combo = True
                    player2.direction.x = 0
                if player.facing_right == False and player2.facing_right == False:
                    player.during_combo2 = True
                    player.facing_right = True
                if player.facing_right == True and player2.facing_right == True:
                    player.during_combo2 = True
                    player.facing_right = False
            if player.status == 'attack2':
                player.during_combo2 = False
                player.move = False
            if player.status == 'b4attack':
                player.b4_attack = False
                player.b4_attack_count = 0
                player.attack2 = False
            else:
                player.during_combo2 = True
                player2.direction.x = 0
                if player2.rect.x in range(player.rect.x + 60):
                    player2.stall = True
                    if player2.facing_right == True:
                        player.rect.x = player.rect.x + 2
                    if player2.facing_right == False:
                        player.rect.x = player.rect.x - 2
                if keys[pygame.K_RSHIFT]:
                    player2.direction.x = 0
                    
        if pygame.sprite.collide_mask(player2, player) and player2.status == 'combofour':
            if player.status == 'guard':
                if player.facing_right == True and player2.facing_right == False:
                    player.during_combo2 = False
                    player.guarded_combo = True
                    player2.direction.x = 0
                if player.facing_right == False and player2.facing_right == True:
                    player.during_combo2 = False
                    player.guarded_combo = True
                    player2.direction.x = 0
                if player.facing_right == False and player2.facing_right == False:
                    player.during_combo2 = True
                    player.facing_right = True
                if player.facing_right == True and player2.facing_right == True:
                    player.during_combo2 = True
                    player.facing_right = False
            if player.status == 'attack2':
                player.during_combo = False
                player.move = False
            if player.status == 'b4attack':
                player.b4_attack = False
                player.b4_attack_count = 0
                player.attack2 = False
            else:
                player.during_combo = True
                player2.direction.x = 0
                if player2.rect.x in range(player.rect.x + 60):
                    player2.stall = True
                    if player2.facing_right == True:
                        player.rect.x = player.rect.x + 2
                    if player2.facing_right == False:
                        player.rect.x = player.rect.x - 2
                if keys[pygame.K_RSHIFT]:
                    player2.direction.x = 0

        if pygame.sprite.collide_mask(player2, player) and player2.status == 'combofive':
            if player.status == 'guard':
                if player.facing_right == True and player2.facing_right == False:
                    player.during_combo2 = False
                    player.guarded_combo = True
                    player2.direction.x = 0
                if player.facing_right == False and player2.facing_right == True:
                    player.during_combo2 = False
                    player.guarded_combo = True
                    player2.direction.x = 0
                if player.facing_right == False and player2.facing_right == False:
                    player.during_combo2 = True
                    player.facing_right = True
                if player.facing_right == True and player2.facing_right == True:
                    player.during_combo2 = True
                    player.facing_right = False
            if player.status == 'attack2':
                player.during_combo2 = False
                player.move = False
            if player.status == 'b4attack':
                player.b4_attack = False
                player.b4_attack_count = 0
                player.attack2 = False
            else:
                player.during_combo2 = True
                player2.direction.x = 0
                if player2.rect.x in range(player.rect.x + 60):
                    player2.stall = True
                    if player2.facing_right == True:
                        player.rect.x = player.rect.x + 2
                    if player2.facing_right == False:
                        player.rect.x = player.rect.x - 2
                if keys[pygame.K_RSHIFT]:
                    player2.direction.x = 0

        if pygame.sprite.collide_mask(player2, player) and player2.status == 'combosix':
            if player.status == 'guard':
                if player.facing_right == True and player2.facing_right == False:
                    player.during_combo2 = False
                    player.guarded_combo = True
                    player2.direction.x = 0
                if player.facing_right == False and player2.facing_right == True:
                    player.during_combo2 = False
                    player.guarded_combo = True
                    player2.direction.x = 0
                if player.facing_right == False and player2.facing_right == False:
                    player.during_combo2 = True
                    player.facing_right = True
                if player.facing_right == True and player2.facing_right == True:
                    player.during_combo2 = True
                    player.facing_right = False
            if player.status == 'attack2':
                player.during_combo = False
                player.move = False
            if player.status == 'b4attack':
                player.b4_attack = False
                player.b4_attack_count = 0
                player.attack2 = False
            else:
                player.during_combo = True
                player2.direction.x = 0
                if player2.rect.x in range(player.rect.x + 60):
                    player2.stall = True
                    if player2.facing_right == True:
                        player.rect.x = player.rect.x + 2
                    if player2.facing_right == False:
                        player.rect.x = player.rect.x - 2
                if keys[pygame.K_RSHIFT]:
                    player2.direction.x = 0

        # PLAYER 1 COMBOS #
        ###################################################################################

        if player2.combo_count in range(1, 25):
            player.stall = True
        else:
            player.stall = False
        
        if player2.combo_count2 in range(1, 25):
            player.stall2 = True
        else:
            player.stall2 = False

        if pygame.sprite.collide_mask(player2, player):
            if player.status == 'combo' or player.status == 'combotwo' or player.status == 'combothree' or player.status == 'combofour' or player.status == 'combofive' or player.status == 'combosix':
                if player2.status != 'guard':
                    if player.facing_right == False:
                        player2.facing_right = True
                    if player.facing_right == True:
                        player2.facing_right = False
        
        if player2.guarded_combo == True:
            player.stopped = True
        if player2.guarded_combo == False:
            player.stopped = False

        if pygame.sprite.collide_mask(player2, player) and player.status == 'combo':
            if player2.status == 'guard':
                if player.facing_right == True and player2.facing_right == False:
                    player2.during_combo = False
                    player2.guarded_combo = True
                    player.direction.x = 0
                if player.facing_right == False and player2.facing_right == True:
                    player2.during_combo = False
                    player2.guarded_combo = True
                    player.direction.x = 0
                if player.facing_right == False and player2.facing_right == False:
                    player2.during_combo = True
                    player2.facing_right = True
                if player.facing_right == True and player2.facing_right == True:
                    player2.during_combo = True
                    player2.facing_right = False
            if player2.status == 'attack1':
                player2.during_combo = False
                player2.move = False
            if player2.status == 'b4attack1':
                player2.b4_attack = False
                player2.b4_attack_count = 0
                player2.attack1 = False
            else:
                player2.during_combo = True
                player.direction.x = 0
                if player.rect.x in range(player2.rect.x + 30):
                    player.stall = True
                    if player.facing_right == True:
                        player2.rect.x = player2.rect.x + 2
                    if player.facing_right == False:
                        player2.rect.x = player2.rect.x - 2
                if keys[pygame.K_z]:
                    player2.direction.x = 0

        if pygame.sprite.collide_mask(player2, player) and player.status == 'combotwo':
            if player2.status == 'guard':
                if player.facing_right == True and player2.facing_right == False:
                    player2.during_combo2 = False
                    player2.guarded_combo = True
                    player.direction.x = 0
                if player.facing_right == False and player2.facing_right == True:
                    player2.during_combo2 = False
                    player2.guarded_combo = True
                    player.direction.x = 0
                if player.facing_right == False and player2.facing_right == False:
                    player2.during_combo2 = True
                    player2.facing_right = True
                if player.facing_right == True and player2.facing_right == True:
                    player2.during_combo2 = True
                    player2.facing_right = False
            if player2.status == 'attack1':
                player2.during_combo2 = False
                player2.move = False
            if player2.status == 'b4attack1':
                player2.b4_attack = False
                player2.b4_attack_count = 0
                player2.attack1 = False
            else:
                player2.during_combo2 = True
                player.direction.x = 0
                if player.rect.x in range(player2.rect.x + 20):
                    player.stall = True
                    if player.facing_right == True:
                        player2.rect.x = player2.rect.x + 2
                    if player.facing_right == False:
                        player2.rect.x = player2.rect.x - 2
                if keys[pygame.K_z]:
                    player2.direction.x = 0

        if pygame.sprite.collide_mask(player2, player) and player.status == 'combothree':
            if player2.status == 'guard':
                if player.facing_right == True and player2.facing_right == False:
                    player2.during_combo = False
                    player2.guarded_combo = True
                    player.direction.x = 0
                if player.facing_right == False and player2.facing_right == True:
                    player2.during_combo = False
                    player2.guarded_combo = True
                    player.direction.x = 0
                if player.facing_right == False and player2.facing_right == False:
                    player2.during_combo = True
                    player2.facing_right = True
                if player.facing_right == True and player2.facing_right == True:
                    player2.during_combo = True
                    player2.facing_right = False
            if player2.status == 'attack1':
                player2.during_combo = False
                player2.move = False
            if player2.status == 'b4attack1':
                player2.b4_attack = False
                player2.b4_attack_count = 0
                player2.attack1 = False
            else:
                player2.during_combo = True
                player.direction.x = 0
                if player.rect.x in range(player2.rect.x + 10):
                    player.stall = True
                    if player.facing_right == True:
                        player2.rect.x = player2.rect.x + 2
                    if player.facing_right == False:
                        player2.rect.x = player2.rect.x - 2
                if keys[pygame.K_z]:
                    player2.direction.x = 0

        if pygame.sprite.collide_mask(player2, player) and player.status == 'combofour':
            if player2.status == 'guard':
                if player.facing_right == True and player2.facing_right == False:
                    player2.during_combo2 = False
                    player2.guarded_combo = True
                    player.direction.x = 0
                if player.facing_right == False and player2.facing_right == True:
                    player2.during_combo2 = False
                    player2.guarded_combo = True
                    player.direction.x = 0
                if player.facing_right == False and player2.facing_right == False:
                    player2.during_combo2 = True
                    player2.facing_right = True
                if player.facing_right == True and player2.facing_right == True:
                    player2.during_combo2 = True
                    player2.facing_right = False
            if player2.status == 'attack1':
                player2.during_combo2 = False
                player2.move = False
            if player2.status == 'b4attack1':
                player2.b4_attack = False
                player2.b4_attack_count = 0
                player2.attack1 = False
            else:
                player2.during_combo2 = True
                player.direction.x = 0
                if player.rect.x in range(player2.rect.x + 25):
                    player.stall = True
                    if player.facing_right == True:
                        player2.rect.x = player2.rect.x + 2
                    if player.facing_right == False:
                        player2.rect.x = player2.rect.x - 2
                if keys[pygame.K_z]:
                    player2.direction.x = 0

        if pygame.sprite.collide_mask(player2, player) and player.status == 'combofive':
            if player2.status == 'guard':
                if player.facing_right == True and player2.facing_right == False:
                    player2.during_combo = False
                    player2.guarded_combo = True
                    player.direction.x = 0
                if player.facing_right == False and player2.facing_right == True:
                    player2.during_combo = False
                    player2.guarded_combo = True
                    player.direction.x = 0
                if player.facing_right == False and player2.facing_right == False:
                    player2.during_combo = True
                    player2.facing_right = True
                if player.facing_right == True and player2.facing_right == True:
                    player2.during_combo = True
                    player2.facing_right = False
            if player2.status == 'attack1':
                player2.during_combo = False
                player2.move = False
            if player2.status == 'b4attack1':
                player2.b4_attack = False
                player2.b4_attack_count = 0
                player2.attack1 = False
            else:
                player2.during_combo = True
                player.direction.x = 0
                if player.rect.x in range(player2.rect.x + 30):
                    player.stall = True
                    if player.facing_right == True:
                        player2.rect.x = player2.rect.x + 2
                    if player.facing_right == False:
                        player2.rect.x = player2.rect.x - 2
                if keys[pygame.K_z]:
                    player2.direction.x = 0

        if pygame.sprite.collide_mask(player2, player) and player.status == 'combosix':
            if player2.status == 'guard':
                if player.facing_right == True and player2.facing_right == False:
                    player2.during_combo2 = False
                    player2.guarded_combo = True
                    player.direction.x = 0
                if player.facing_right == False and player2.facing_right == True:
                    player2.during_combo2 = False
                    player2.guarded_combo = True
                    player.direction.x = 0
                if player.facing_right == False and player2.facing_right == False:
                    player2.during_combo2 = True
                    player2.facing_right = True
                if player.facing_right == True and player2.facing_right == True:
                    player2.during_combo2 = True
                    player2.facing_right = False
            if player2.status == 'attack1':
                player2.during_combo2 = False
                player2.move = False
            if player2.status == 'b4attack1':
                player2.b4_attack = False
                player2.b4_attack_count = 0
                player2.attack1 = False
            else:
                player2.during_combo2 = True
                player.direction.x = 0
                if player.rect.x in range(player2.rect.x + 20):
                    player.stall = True
                    if player.facing_right == True:
                        player2.rect.x = player2.rect.x + 2
                    if player.facing_right == False:
                        player2.rect.x = player2.rect.x - 2
                if keys[pygame.K_z]:
                    player2.direction.x = 0

        ###################################################################################

        if pygame.sprite.collide_mask(player2, player):
            if player2.status == 'combo' or player2.status == 'combotwo' or player2.status == 'combothree' or player2.status == 'combofour' or player2.status == 'combofive' or player2.status == 'combosix':
                if player.status == 'attack2':
                    player.during_combo = False
                    player.during_combo2 = False

        if pygame.sprite.collide_mask(player2, player):
            if player.status == 'combo' or player.status == 'combotwo' or player.status == 'combothree' or player.status == 'combofour' or player.status == 'combofive' or player.status == 'combosix':
                if player2.status == 'attack1':
                    player2.during_combo = False
                    player2.during_combo2 = False

    def setting_combo(self):
        player = self.player.sprite
        player2 = self.player2.sprite

        keys = pygame.key.get_pressed()

        if player.during_combo == True:
            player2.in_combo = True
        elif player.during_combo2 == True:
            player2.in_combo = True
        else:
            player2.in_combo = False

        if player2.in_combo == True:
            player2.combo_timer += 1

        if player2.add_combo_count == True:
            player2.hit_count += 1
        
        if player2.combo_timer >= 1:
            player2.in_combo = True
        if player2.combo_timer in range(1, 90):
            player2.combo_timer += 1 
            if pygame.sprite.collide_mask(player2, player):
                if player2.status == 'combo' or player2.status == 'combotwo' or player2.status == 'combothree' or player2.status == 'combofour' or player2.status == 'combofive' or player2.status == 'combosix':
                    player2.combo_timer = 1
                if player.status == 'guard':
                    player2.hit_count -= 1
            if player2.combo_timer == 3 and player.status != 'guard':
                player2.hit_count += 1
        if player2.combo_timer >= 90:
            player2.combo_timer = 0
            player2.in_combo = False
            player2.hit_count = 0

        ###################################################################################

        if player2.during_combo == True:
            player.in_combo = True
        elif player2.during_combo2 == True:
            player.in_combo = True
        else:
            player.in_combo = False

        if player.in_combo == True:
            player.combo_timer += 1

        if player.combo_timer >= 1:
            player.in_combo = True
        if player.combo_timer in range(1, 120):
            player.combo_timer += 1
            if pygame.sprite.collide_mask(player2, player):
                if player.status == 'combo' or player.status == 'combotwo' or player.status == 'combothree' or player.status == 'combofour' or player.status == 'combofive' or player.status == 'combosix':
                    player.combo_timer = 1
                if player2.status == 'guard':
                    player.hit_count -= 1
            if player.combo_timer == 3 and player2.status != 'guard':
                player.hit_count += 1
        if player.combo_timer >= 120:
            player.combo_timer = 0
            player.in_combo = False
            player.hit_count = 0

    def player_close_range_attacks(self):
        player = self.player.sprite
        player2 = self.player2.sprite

        keys = pygame.key.get_pressed()

        ###############################################################################

        if player.hit_count > 9:
            if keys[pygame.K_c]:
                player.b4_attack = False
                player.attack2 = True
                if player2.initiate_damage_state == True:
                    player.attack2 = False

        if pygame.sprite.collide_mask(player, player2) and keys[pygame.K_c] and player.b4_attack == False and player.h2h_count > player2.h2h_count:
            if player.facing_right == True:
                player.move = False
                player.initiate_attack_count += 1
                if player2.facing_right == True:
                    player2.facing_right = False
            if player.facing_right == False:
                player.move = False
                player.initiate_attack_count += 1
                if player2.facing_right == False:
                    player2.facing_right = True    
        else:
            player.move = True
            player.initiate_attack_count = 0

        if player.move == False:
            if player.initiate_attack_count in range(1, 24):
                player2.hitb4 = True
                player.while_hit2 = True
                if player2.facing_right == False:
                    player2.rect.x = player2.rect.x + 4
                if player2.facing_right == True:
                    player2.rect.x = player2.rect.x - 4
            if player.initiate_attack_count in range(25, 100):
                player.while_hit2 = False
                player.initiate_attack_count = 0
                player.attack2 = False
                player.b4_attack = False
                player2.initiate_damage_state = True
                player2.hitb4 = False

        if not keys[pygame.K_c]:
            player.attack2 = True
            player.move = True
            player.b4_attack = True
            player2.hitb4 = False
            player.while_hit2 = False

        if player.initiate_attack_count in range(1, 100) and not keys[pygame.K_c]:
            player2.initiate_damage_state = True
        
        if player2.initiate_damage_state  == True:
            player2.initiate_damage_count += 1
            
        if player2.initiate_damage_count >= 1:
            player2.initiate_damage_state  = True
            player2.initiate_damage_count += 1
            player2.taking_damage1 = True
        if player2.initiate_damage_count in range(87, 150):
            player2.initiate_damage_state  = False
            player2.initiate_damage_count = 0

        ###############################################################################

        if player2.hit_count > 9:
            if keys[pygame.K_SLASH]:
                player2.b4_attack = False
                player2.attack1 = True
                if player.initiate_damage_state == True:
                    player2.attack1 = False

        if pygame.sprite.collide_mask(player, player2) and keys[pygame.K_SLASH] and player2.status == 'attack1' and player2.stopped == False and player2.h2h_count > player.h2h_count:
            if player2.facing_right == False:
                player2.move = False
                player2.initiate_attack_count += 1
                if player.facing_right == False:
                    player.facing_right = True
            if player2.facing_right == True:
                player2.move = False
                player2.initiate_attack_count += 1
                if player.facing_right == True:
                    player.facing_right = False
        else:
            player2.move = True
            player2.initiate_attack_count = 0

        if player2.move == False:
            if player2.initiate_attack_count in range(1, 23):
                #player.idle_hit = True
                player.taking_damage2 = True
            if player2.initiate_attack_count in range(24, 100):
                #player.idle_hit = False
                player.taking_damage2 = False
                player2.initiate_attack_count = 0
                player2.attack1 = False
                player.initiate_damage_state = True
                player2.b4_attack = False

        if not keys[pygame.K_SLASH]:
            player2.attack1 = True
            player2.move = True
            player.taking_damage2 = False
            player2.b4_attack = True

        if player2.initiate_attack_count in range(1, 100) and not keys[pygame.K_SLASH]:
            player.initiate_damage_state = True

        if player.initiate_damage_state == True:
            player.initiate_damage_count += 1

        if player.initiate_damage_count >= 1:
            player.initiate_damage_state = True
            player.initiate_damage_count += 1
            player.taking_damage1 = True
        if player.initiate_damage_count in range(87, 150):
            player.initiate_damage_state = False
            player.initiate_damage_count = 0
                          
    def player_additional_attack(self):
        player = self.player.sprite
        player2 = self.player2.sprite

        keys = pygame.key.get_pressed()

        if player2.attack2 == True and player2.status == 'attack3':
            position = player2.rect.x
            if fire_ball_rect.x != player2.rect.x - 10:
                player2.rect.x = fire_ball_rect.x
            if fire_ball_rect.x == player2.rect.x:
                fire_ball_rect.x = position
            if fire_ball_rect.x == position:
                player2.attack3 = False
        if player2.attack2right == True and player2.status == 'attack3':
            position = player2.rect.x
            if flip_fire_ball_rect.x != player2.rect.x + 20:
                player2.rect.x = flip_fire_ball_rect.x
            if flip_fire_ball_rect.x == player2.rect.x:
                flip_fire_ball_rect.x = position
                player2.attack3 = False
            if flip_fire_ball_rect == position:
                player2.attack3 = False

        if fire_ball_rect.x != player2.rect.x - 10:
            if player2.status == 'attack3':
                player2.limited_attack_amount -= 1

        if player2.limited_attack_amount != 3:
            if player2.charge <= 1:
                player2.limited_attack_amount = 3

        ###################################################################################

        s_hitbox = (player2.rect.x - 10, player2.rect.y - 10, 65, 75)

        if player.status == 'attack3' and player.facing_right == True:
            player.attack3right = True

        if player.attack3right == True:
            if player.clone_on_screen == False:
                screen.blit(shuriken, (shuriken_rect))
            if player.shuriken == False:
                shuriken_rect.x += 20

        if player.attack3right == False:
            shuriken_rect.topleft = (player.rect.x + 10, player.rect.y - 15)

        if shuriken_rect.x != player.rect.x + 10:
            if shuriken_rect.x > player2.rect.x - 300 and shuriken_rect.x < player2.rect.x + 300 and player.clone_test == False:
                player.clone = True
                player.clone_on_screen = True
        if shuriken_rect.x == player.rect.x + 10:
            player.clone = False
    
        if player.attack3right == True:
            if player.clone == True:
                player.clone_count += 1
                smoke1_rect.x = shuriken_rect.x
                smoke1_rect.y = shuriken_rect.y - 5
                smoke2_rect.x = shuriken_rect.x
                smoke2_rect.y = shuriken_rect.y - 5
                clone_rect.x = smoke2_rect.x 
                clone_rect.y = smoke2_rect.y - 5
            if player.clone_count >= 1:
                player.clone == True
            if player.clone_count in range(1, 10):
                screen.blit(smoke1, (smoke1_rect))
                smoke1_rect.x = shuriken_rect.x
                smoke1_rect.y = shuriken_rect.y - 5
                clone_rect.x = smoke1_rect.x 
                clone_rect.y = smoke1_rect.y - 5
                player.shuriken = True
            if player.clone_count in range(11, 20):
                screen.blit(clone, (clone_rect))
                screen.blit(smoke2, (smoke2_rect))
                smoke2_rect.x = shuriken_rect.x
                smoke2_rect.y = shuriken_rect.y - 5
                clone_rect.x = smoke2_rect.x 
                clone_rect.y = smoke2_rect.y - 5
                player.shuriken = True
            if player.clone_count in range(20, 100):
                player.clone = False
                player.clone_movement = True
                player.clone_count = 0

        if player.attack3right == True:
            if player.clone_movement == True:
                screen.blit(clone, (clone_rect))
                position_s = smoke2_rect.x
                position_sy = smoke2_rect.y
                clone_rect.x = position_s
                clone_rect.y = position_sy - 5
                if clone_rect.x == position_s:
                    player.clone_test = True
                    
        if player.attack3right == True:
            if player.clone_test == True:
                player.clone = False
                smoke2_rect.x += 20

        if pygame.Rect.colliderect(clone_rect, s_hitbox) and player.clone_movement == True:
            player.rasengan = True
            player.clone = False
            player.clone_movement = False
            player.attack3right = False
            player.shuriken = False
            player.clone_on_screen = False
            player.clone_test = False
            if player2.facing_right == True:
                player2.facing_right = False

        if clone_rect.x > 1150 and player.clone_movement == True:
            player.attack3right = False
            player.clone = False
            player.clone_movement = False
            player.shuriken = False
            player.clone_on_screen = False
            player.clone_test = False
       
        #### FACING LEFT ####   

        if player.status == 'attack3' and player.facing_right == False:
            player.attack3 = True

        if player.attack3 == True:
            if player.flip_clone_on_screen == False:
                screen.blit(flip_shuriken, (flip_shuriken_rect))
            if player.flip_shuriken == False:
                flip_shuriken_rect.x -= 20

        if player.attack3 == False:
            flip_shuriken_rect.topleft = (player.rect.x - 40, player.rect.y - 15)

        if flip_shuriken_rect.x != player.rect.x - 40:
             if flip_shuriken_rect.x > player2.rect.x - 300 and flip_shuriken_rect.x < player2.rect.x + 300 and player.flip_clone_test == False:
                player.flip_clone = True
                player.flip_clone_on_screen = True
        if flip_shuriken_rect.x == player.rect.x - 40:
            player.flip_clone = False

        if player.attack3 == True:
            if player.flip_clone == True:
                player.flip_clone_count += 1
                flip_smoke1_rect.x = flip_shuriken_rect.x
                flip_smoke1_rect.y = flip_shuriken_rect.y - 5
                flip_smoke2_rect.x = flip_shuriken_rect.x
                flip_smoke2_rect.y = flip_shuriken_rect.y - 5
                flip_clone_rect.x = flip_smoke2_rect.x 
                flip_clone_rect.y = flip_smoke2_rect.y - 5
            if player.flip_clone_count >= 1:
                player.flip_clone == True
            if player.flip_clone_count in range(1, 10):
                screen.blit(flip_smoke1, (flip_smoke1_rect))
                flip_smoke1_rect.x = flip_shuriken_rect.x
                flip_smoke1_rect.y = flip_shuriken_rect.y - 5
                flip_clone_rect.x = flip_smoke1_rect.x 
                flip_clone_rect.y = flip_smoke1_rect.y - 5
                player.flip_shuriken = True
            if player.flip_clone_count in range(11, 20):
                screen.blit(flip_clone, (flip_clone_rect))
                screen.blit(flip_smoke2, (flip_smoke2_rect))
                flip_smoke2_rect.x = flip_shuriken_rect.x
                flip_smoke2_rect.y = flip_shuriken_rect.y - 5
                flip_clone_rect.x = flip_smoke2_rect.x 
                flip_clone_rect.y = flip_smoke2_rect.y - 5
                player.flip_shuriken = True
            if player.flip_clone_count in range(20, 100):
                player.flip_clone = False
                player.flip_clone_movement = True
                player.flip_clone_count = 0

        if player.attack3 == True:
            if player.flip_clone_movement == True:
                screen.blit(flip_clone, (flip_clone_rect))
                position_ss = flip_smoke2_rect.x
                position_sys = flip_smoke2_rect.y
                flip_clone_rect.x = position_ss
                flip_clone_rect.y = position_sys - 5
                if flip_clone_rect.x == position_ss:
                    player.flip_clone_test = True

        if player.attack3 == True:
            if player.flip_clone_test == True:
                player.flip_clone = False
                flip_smoke2_rect.x -= 20

        if pygame.Rect.colliderect(flip_clone_rect, s_hitbox) and player.flip_clone_movement == True:
            player.rasengan = True
            player.flip_clone = False
            player.flip_clone_movement = False
            player.attack3 = False
            player.flip_shuriken = False
            player.flip_clone_on_screen = False
            player.flip_clone_test = False
            if player2.facing_right == False:
                player2.facing_right = True

        if flip_clone_rect.x < 0 and player.flip_clone_movement == True:
            player.attack3 = False
            player.flip_clone = False
            player.flip_clone_movement = False
            player.flip_shuriken = False
            player.flip_clone_on_screen = False
            player.flip_clone_test = False

        #################################################################

        if player.attack3right == True or player.attack3 == True:
            player.limited_attack_count += 1
        else:
            player.limited_attack_count = 0

        if player.limited_attack_amount == 3:
            if player.limited_attack_count == 15:
                player.limited_attack_amount -= 1
        if player.limited_attack_amount == 2:
            if player.limited_attack_count == 13:
                player.limited_attack_amount -= 1
        if player.limited_attack_amount == 1:
            if player.limited_attack_count == 11:
                player.limited_attack_amount -= 1

        #if player.level == 2:
            #if player.limited_attack_amount != 3:
                #if player.charge == 1:
                    #player.limited_attack_amount = 3
        #if player.level == 3:
            #if player.limited_attack_amount != 3:
                #if player.charge == 1:
                    #player.limited_attack_amount = 3

        if player.limited_attack_amount != 3:
            if player.charge >= 274:
                player.limited_attack_amount = 3
        
    def teleporting(self):
        player = self.player.sprite
        player2 = self.player2.sprite

        if player.status == 'hitfireball':
            player.teleporting = False
        if player.status == 'guardfireball':
            player.teleporting = False
        if player.status == 'aftercombo':
            player.teleporting = False
        if player.status == 'aftercombo2':
            player.teleporting = False
        if player.status == 'hitchidori':
            player.teleporting = False
        if player.status == 'whilehit2':
            player.teleporting = False

        if player2.status == 'hitrasengan':
            player2.teleporting = False
        if player2.status == 'hitb4':
            player2.teleporting = False
        if player2.status == 'aftercombo':
            player2.teleporting = False
        if player2.status == 'aftercombo2':
            player2.teleporting = False
        if player2.status == 'b4rasengan':
            player2.teleporting = False
        if player2.status == 'guardrasengan':
            player2.teleporting = False
        if player2.status == 'hitspecial':
            player2.teleporting = False

    def player_health_attacks(self):
        player = self.player.sprite
        player2 = self.player2.sprite

        ########## PLAYER 1 ##########

        if player2.level == 1:
            if player.status == 'b4fireball':
                player.health(0.50)
                player2.charge -= 0.65
            if player.status == 'hitchidori':
                player.health(0.55)
                player2.charge -= 0.70
            if player.during_combo == True:
                player.health(0.15)
                player2.charge -= 0.25
            if player.during_combo2 == True:
                player.health(0.15)
                player2.charge -= 0.25
        if player2.level == 2:
            if player.status == 'b4fireball':
                player.health(0.65)
                player2.charge -= 0.65
            if player.status == 'hitchidori':
                player.health(0.70)
                player2.charge -= 0.70
            if player.during_combo == True:
                player.health(0.25)
                player2.charge -= 0.25
            if player.during_combo2 == True:
                player.health(0.25)
                player2.charge -= 0.25
        if player2.level == 3:
            if player.status == 'b4fireball':
                player.health(0.80)
                if player2.charge > 1:
                    player2.charge -= 0.65
            if player.status == 'hitchidori':
                player.health(0.85)
                if player2.charging == True:
                    player2.charge -= 0.70
            if player.during_combo == True:
                player.health(0.35)
                if player2.charge > 1:
                    player2.charge -= 0.25
            if player.during_combo2 == True:
                player.health(0.35)
                if player2.charge > 1:
                    player2.charge -= 0.25

        if player.level == 1:
            if player2.status == 'b4rasengan':
                player2.health(0.50)
                player.charge += 0.65
            if player2.status == 'hitb4':
                player2.health(0.55)
                player.charge += 0.70
            if player2.during_combo == True:
                player2.health(0.15)
                player.charge += 0.2
            if player2.during_combo2 == True:
                player2.health(0.15)
                player.charge += 0.2
        if player.level == 2:
            if player2.status == 'b4rasengan':
                player2.health(0.65)
                player.charge += 0.65
            if player2.status == 'hitb4':
                player2.health(0.70)
                player.charge += 0.70
            if player2.during_combo == True:
                player2.health(0.25)
                player.charge += 0.2
            if player2.during_combo2 == True:
                player2.health(0.25)
                player.charge += 0.2
        if player.level == 3:
            if player2.status == 'b4rasengan':
                player2.health(0.80)
                if player.charge < 274:
                    player.charge += 0.65
            if player2.status == 'hitb4':
                player2.health(0.85)
                if player.charge < 274:
                    player.charge += 0.70
            if player2.during_combo == True:
                player2.health(0.35)
                if player.charge < 274:
                    player.charge += 0.2
            if player2.during_combo2 == True:
                player2.health(0.35)
                if player.charge < 274:
                    player.charge += 0.2

        if player2.status == 'hitspecial':
            player2.health(10)

        if pygame.Rect.colliderect(player.rect, s_special4_rect) and player2.in_special_count in range(16, 20):
            player.health(100)
            player.initiate_damage_state = True

        if pygame.Rect.colliderect(player.rect, s_special4_rect2) and player2.in_special_count in range(16, 20):
            player.health(100)
            player.initiate_damage_state = True

        if pygame.Rect.colliderect(player.rect, s_special4_rect3) and player2.in_special_count in range(16, 20):
            player.health(100)
            player.initiate_damage_state = True

    def player_screen_state(self):
        player = self.player.sprite
        player2 = self.player2.sprite

        if player2.on_screen == True:
            self.player2.draw(self.display_surface)
        if player.on_screen == True:
            self.player.draw(self.display_surface)

        if player2.status == 'combo' or player2.status == 'combotwo' or player2.status == 'combothree' or player2.status == 'combofour' or player2.status == 'combofive' or player2.status == 'combosix':
            self.player.draw(self.display_surface)
            self.player2.draw(self.display_surface)

    def image_imports(self):
        player = self.player.sprite
        player2 = self.player2.sprite

        font = pygame.font.Font('/Users/charlieyorke/ace/imgs/plaguard-font/Plaguard-ZVnjx.otf', 24)
        font2 = pygame.font.Font('/Users/charlieyorke/ace/imgs/plaguard-font/Plaguard-ZVnjx.otf', 32)
        special_font = font.render('SPECIAL', 1, (0, 0, 0))
        combo_count = font2.render(f'{player2.hit_count}', 1, (0, 0, 0))
        combo_count_1 = font2.render(f'{player.hit_count}', 1, (0, 0, 0))

        if player2.in_combo == True:
            screen.blit(hitcount, (900, 300))
            screen.blit(combo_count, (910, 300))
        if player.in_combo == True:
            screen.blit(hitcount, (150, 300))
            screen.blit(combo_count_1, (160, 300))

        if player2.attack3allowed == True:
            screen.blit(rinnegan, (player2.rect.x, player2.rect.x - 20))
        else:
            pass

        # player 1 health bar 
        pygame.draw.rect(screen, (0, 0, 0), (150, 45, 412, 34), 4)
        pygame.draw.rect(screen, (255, 0, 0), (150, 45, 410, 32))
        pygame.draw.rect(screen, (255, 255, 0), (150, 45, player.max_health, 32))

        # player 2 health bar 
        pygame.draw.rect(screen, (0, 0, 0), (630, 45, 412, 34), 4)
        pygame.draw.rect(screen, (255, 255, 0), (630, 45, 410, 32))
        pygame.draw.rect(screen, (255, 0, 0), (630, 45, player2.max_health, 32))

        # player 1 level bar 
        pygame.draw.rect(screen, (0, 0, 0), (151, 90, 277, 12), 4)
        pygame.draw.rect(screen, (255, 128, 0), (151, 90, 275, 10))
        pygame.draw.rect(screen, (0, 0, 255), (151, 90, player.charge, 10))

        if player.special_available == True:
            player.special_available_count += 1

        if player.special_available_count in range(1, 20):
            player.special_available_count += 1
        if player.special_available_count in range(21, 50):
            player.special_available_count += 1
            pygame.draw.rect(screen, (128, 0, 128), (153, 90, 275, 10))
            #screen.blit(special_font, (215, 90))
        if player.special_available_count >= 50:
            player.special_available_count = 0

        # player 2 level bar
        pygame.draw.rect(screen, (0, 0, 0), (762, 90, 277, 12), 4)
        pygame.draw.rect(screen, (0, 0, 255), (762, 90, 275, 10))
        pygame.draw.rect(screen, (255, 128, 0), (762, 90, player2.charge, 10))

        if player2.special_available == True:
            player2.special_available_count += 1

        if player2.special_available_count in range(1, 20):
            player2.special_available_count += 1
        if player2.special_available_count in range(21, 50):
            pygame.draw.rect(screen, (128, 0, 128), (760, 90, 275, 10))
            #screen.blit(special_font, (850, 90))
        if player2.special_available_count >= 50:
            player2.special_available_count = 0

        bar_covers = pygame.transform.scale(pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/healthbarcover.png'), (450, 100)).convert_alpha()

        flipped_bar_covers = pygame.transform.flip(bar_covers, True, False)

        #screen.blit(bar_covers, (120, 30))

        #screen.blit(flipped_bar_covers, (620, 30))

        font = pygame.font.Font('/Users/charlieyorke/ace/imgs/pokemon-gb-font.tff/pokemonfont.ttf', 15)

        p1_level_font = font.render(f'Level:{player.level}', 1, (255, 255, 255))

        screen.blit(p1_level_font, (152, 112))

        p2_level_font = font.render(f'Level:{player2.level}', 1, (255, 255, 255))

        screen.blit(p2_level_font, (935, 112))

        n_pfp = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/n_hedshot.png')

        s_pfp = pygame.image.load('/Users/charlieyorke/ace/imgs/ingameimgs/s_hedshot.png')

        screen.blit(n_pfp, (-20, -70))

        screen.blit(s_pfp, (1010, -70))

        #### PLAYER 1 LIMITED ATTACK ####

        pygame.draw.rect(screen, (0, 0, 0), (270, 115, 35, 10), 3)

        pygame.draw.rect(screen, (0, 0, 0), (310, 115, 35, 10), 3)

        pygame.draw.rect(screen, (0, 0, 0), (350, 115, 35, 10), 3)

        if player.limited_attack_amount == 3:
            pygame.draw.rect(screen, (0, 0, 255), (270, 115, 33, 8), 0)
            pygame.draw.rect(screen, (0, 0, 255), (310, 115, 33, 8), 0)
            pygame.draw.rect(screen, (0, 0, 255), (350, 115, 33, 8), 0)
        if player.limited_attack_amount == 2:
            pygame.draw.rect(screen, (0, 0, 255), (270, 115, 33, 8), 0)
            pygame.draw.rect(screen, (0, 0, 255), (310, 115, 33, 8), 0)
        if player.limited_attack_amount == 1:
            pygame.draw.rect(screen, (0, 0, 255), (270, 115, 33, 8), 0)

        #### PLAYER 2 LIMITED ATTACK ####

        pygame.draw.rect(screen, (0, 0, 0), (885, 115, 35, 10), 3)

        pygame.draw.rect(screen, (0, 0, 0), (845, 115, 35, 10), 3)

        pygame.draw.rect(screen, (0, 0, 0), (805, 115, 35, 10), 3)

        if player2.limited_attack_amount == 3:
            pygame.draw.rect(screen, (0, 0, 255), (885, 115, 33, 8), 0)
            pygame.draw.rect(screen, (0, 0, 255), (845, 115, 33, 8), 0)
            pygame.draw.rect(screen, (0, 0, 255), (805, 115, 33, 8), 0)
        if player2.limited_attack_amount == 2:
            pygame.draw.rect(screen, (0, 0, 255), (885, 115, 33, 8), 0)
            pygame.draw.rect(screen, (0, 0, 255), (845, 115, 33, 8), 0)
        if player2.limited_attack_amount == 1:
            pygame.draw.rect(screen, (0, 0, 255), (885, 115, 33, 8), 0)

    def out_of_bounds(self):
        player = self.player.sprite
        player2 = self.player2.sprite

        if player2.rect.x < 0:
            player2.out_of_bounds = True
        if player2.rect.x > 1140:
            player2.out_of_bounds = True
        if player2.rect.x in range(1, 1139):
            player2.out_of_bounds = False

        if player2.out_of_bounds == True:
            player2.damagecount += 100

        if player.rect.x < -13:
            player.out_of_bounds = True
            if player.status != 'run':
                player.rect.x = -10
        if player.rect.x > 1140:
            player.out_of_bounds = True
            if player.status != 'run':
                player.rect.x = 1166
        if player.rect.x in range(-12, 1139):
            player.out_of_bounds = False

        if player.out_of_bounds == True:
            player.damagecount += 100
            
    def loss(self):
        player = self.player.sprite
        player2 = self.player2.sprite

        if player.max_health < 1:
            self.p2_winner = True
            player2.frame_index = 1
        if player2.max_health > 410:
            self.p1_winner = True
            player.frame_index = 1

        if self.p1_winner == True or self.p2_winner == True:
            self.running = False
            self.gameover = True

        if self.running == True:
            self.p1_winner = False
            self.p2_winner = False
            self.gameover = False

    def run(self):

        pygame.display.init()

        if self.running == True:

            self.player.update()
            self.player2.update()
            self.horizontal_movement_collision()
            self.vertical_movement_collision()

            self.combos()

            self.setting_combo()

            self.adding_attacks()

            self.collisions()

            self.player_ranged_attacks()

            self.player_health_attacks()

            self.player_special_attacks()

            self.player_after_combo_state()

            self.player_close_range_attacks()

            self.player_additional_attack()

            self.player_screen_state()

            self.out_of_bounds()

            self.teleporting()

        self.image_imports()

        self.loss()

        if self.running == False and self.gameover == True:
            self.player.update()
            self.player2.update()
            self.vertical_movement_collision()

            self.adding_attacks()

            self.collisions()

            self.player_ranged_attacks()

            self.player_health_attacks()

            self.player_special_attacks()

            self.player_screen_state()

            self.player_after_combo_state()

            self.player_close_range_attacks()

            self.out_of_bounds()

    def reset(self):
        player = self.player.sprite
        player2 = self.player2.sprite

        self.running = True
        self.p1_winner = False
        self.p2_winner = False

        player.rect.x = 50 
        player.rect.y = 640
        player.max_health = 410
        player.level = 1
        player.charge = 0
        player.status = 'idle'
        player.limited_attack_amount = 3
        player.special_available = False

        player2.rect.x = 1050
        player2.rect.y = 640
        player2.max_health = 0
        player2.level = 1
        player2.charge = 275
        player2.status = 'idle'
        player2.limited_attack_amount = 3
        player2.special_available = False

        main()

level = Level(screen)

class StartButton:
    def __init__(self, x, y, fontimage):
        self.fontimage = fontimage

        self.start_rect = self.fontimage.get_rect()
        self.start_rect.center = (x, y)

        self.clicked = False
    
    def draw(self):

        action = False

        pos = pygame.mouse.get_pos()

        screen.blit(self.fontimage, (self.start_rect.x, self.start_rect.y))

        if self.start_rect.collidepoint(pos):
            pygame.draw.rect(screen, (255, 0, 0), (279, 608.5, 82, 34), 3)
            #self.clicked = True
            
            if pygame.mouse.get_pressed()[0] == 1 or pygame.mouse.get_pressed()[0] == 3 and self.clicked == False:
                self.clicked = True
                action = True
            else:
                self.clicked = False

        return action
class ControlsButton:
    def __init__(self, x, y, fontimage):
        self.fontimage = fontimage

        self.start_rect = self.fontimage.get_rect()
        self.start_rect.center = (x, y)

        self.clicked = False
    
    def draw(self):

        action = False

        pos = pygame.mouse.get_pos()

        screen.blit(self.fontimage, (self.start_rect.x, self.start_rect.y))

        if self.start_rect.collidepoint(pos):
            pygame.draw.rect(screen, (255, 0, 0), (645, 606, 129, 37), 3)
            #self.clicked = True
            
            if pygame.mouse.get_pressed()[0] == 1 or pygame.mouse.get_pressed()[0] == 3 and self.clicked == False:
                self.clicked = True
                action = True
            else:
                self.clicked = False

        return action
class ExitButton:
    def __init__(self, x, y, image):
        self.image = image

        self.exit_rect = self.image.get_rect()
        self.exit_rect.center = (x, y)

        self.clicked = False

    def draw(self):

        action = False
        
        pos = pygame.mouse.get_pos()

        screen.blit(self.image, (self.exit_rect.x, self.exit_rect.y))

        if self.exit_rect.collidepoint(pos) and self.clicked == False:
            pygame.draw.rect(screen, (255, 0, 0), (866, 609, 69, 31), 3)
            self.clicked = True

            if pygame.mouse.get_pressed()[0] == 1 or pygame.mouse.get_pressed()[0] == 3:
                self.clicked = True
                action = True
            else:
                self.clicked = False

        return action
class SettingsButton:
    def __init__(self, x, y, image):
        self.image = image

        self.settings_rect = self.image.get_rect()
        self.settings_rect.center = (x, y)

        self.clicked = False

    def draw(self):

        action = False

        pos = pygame.mouse.get_pos()

        screen.blit(self.image, (self.settings_rect.x, self.settings_rect.y))

        if self.settings_rect.collidepoint(pos):
            pygame.draw.rect(screen, (255, 0, 0), (441, 608, 118, 35), 3)
            #self.clicked = True

            if pygame.mouse.get_pressed()[0] == 1 or pygame.mouse.get_pressed()[0] == 3 and self.clicked == False:
                self.clicked = True
                action = True
            else:
                self.clicked = False

        return action
class BackButton:
    def __init__(self, x, y, image):
        self.image = image

        self.back_rect = self.image.get_rect()
        self.back_rect.center = (x, y)

        self.clicked = False

    def draw(self):

        action = False

        pos = pygame.mouse.get_pos()

        screen.blit(self.image, (self.back_rect.x, self.back_rect.y))

        if self.back_rect.collidepoint(pos):
            pygame.draw.rect(screen, (255, 0, 0), (5, 10, 90, 35), 3)
            #self.clicked = True

            if pygame.mouse.get_pressed()[0] == 1 or pygame.mouse.get_pressed()[0] == 3 and self.clicked == False:
                self.clicked = True
                action = True
            else:
                self.clicked = False

        return action
class InGamePauseButton:
    def __init__(self, x, y, image):
        self.image = image

        self.pause_rect = self.image.get_rect()
        self.pause_rect.center = (x, y)

        self.clicked = False

    def draw(self):

        action = False

        pos = pygame.mouse.get_pos()

        screen.blit(self.image, (self.pause_rect.x, self.pause_rect.y))

        if self.pause_rect.collidepoint(pos):
            #pygame.draw.rect(screen, (255, 0, 0), (1100, 30, 50, 40), 3)
            #self.clicked = True

            if pygame.mouse.get_pressed()[0] == 1 or pygame.mouse.get_pressed()[0] == 3 and self.clicked == False:
                self.clicked = True
                action = True
            else:
                self.clicked = False

        return action
class MenuButton:
    def __init__(self, x, y, image):
        self.image = image

        self.menu_rect = self.image.get_rect()
        self.menu_rect.center = (x, y)

        self.clicked = False

    def draw(self):

        action = False

        pos = pygame.mouse.get_pos()

        screen.blit(self.image, (self.menu_rect.x, self.menu_rect.y))

        if self.menu_rect.collidepoint(pos):
            #pygame.draw.rect(screen, (255, 0, 0), (5, 30, 90, 35), 3)
            #self.clicked = True

            if pygame.mouse.get_pressed()[0] == 1 or pygame.mouse.get_pressed()[0] == 3 and self.clicked == False:
                self.clicked = True
                action = True
            else:
                self.clicked = False

        return action
class ReturnButton:
    def __init__(self, x, y, image):
        self.image = image

        self.return_rect = self.image.get_rect()
        self.return_rect.center = (x, y)

        self.clicked = False

    def draw(self):

        action = False

        pos = pygame.mouse.get_pos()

        screen.blit(self.image, (self.return_rect.x, self.return_rect.y))

        if self.return_rect.collidepoint(pos):
            #pygame.draw.rect(screen, (255, 0, 0), (5, 30, 90, 35), 3)
            #self.clicked = True

            if pygame.mouse.get_pressed()[0] == 1 or pygame.mouse.get_pressed()[0] == 3 and self.clicked == False:
                self.clicked = True
                action = True
            else:
                self.clicked = False

        return action
class PlayAgain:
    def __init__(self, x, y, image):
        self.image = image

        self.return_rect = self.image.get_rect()
        self.return_rect.center = (x, y)

        self.clicked = False

    def draw(self):

        action = False

        pos = pygame.mouse.get_pos()

        screen.blit(self.image, (self.return_rect.x, self.return_rect.y))

        if self.return_rect.collidepoint(pos):
            pygame.draw.rect(screen, (255, 0, 0), (300, 325, 200, 50), 3)
            self.clicked = True

            if pygame.mouse.get_pressed()[0] == 1 or pygame.mouse.get_pressed()[0] == 3 and self.clicked == False:
                self.clicked = True
                action = True
            else:
                self.clicked = False

        return action
class AfterGameMenu:
    def __init__(self, x, y, image):
        self.image = image

        self.return_rect = self.image.get_rect()
        self.return_rect.center = (x, y)

        self.clicked = False

    def draw(self):

        action = False

        pos = pygame.mouse.get_pos()

        screen.blit(self.image, (self.return_rect.x, self.return_rect.y))

        if self.return_rect.collidepoint(pos):
            pygame.draw.rect(screen, (255, 0, 0), (650, 325, 200, 50), 3)
            self.clicked = True

            if pygame.mouse.get_pressed()[0] == 1 or pygame.mouse.get_pressed()[0] == 3 and self.clicked == False:
                self.clicked = True
                action = True
            else:
                self.clicked = False

        return action

start_button = StartButton(320, 625, start_image)
control_button = ControlsButton(710, 625, control_image)
exit_button = ExitButton(900, 625, exit_image)
settings_button = SettingsButton(500, 625, settings_image)
back_button = BackButton(50, 30, back_image)
pause_button = InGamePauseButton(593, 30, pause_image)
menu_button = MenuButton(600, 250, menu_image)
return_button = ReturnButton(600, 400, return_image)
playagain_button = PlayAgain(400, 350, startagain)
aftergamemenu_button = AfterGameMenu(750, 350, menu)

def main():
    game_count = 0
    win_count = 0
    fight_count = 0
    count = 0
    FPS = 200
    run = True
    while run:

        clock.tick(75)
        pygame.display.update()

        fight_count += 1 
        count += 1  
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit

            if event.type == MOUSEBUTTONDOWN and playagain_button.draw():
                level.reset()
            if event.type == MOUSEBUTTONDOWN and aftergamemenu_button.draw():
                main_menu()

        game_count += 1
      
        if game_count in range(1, 8):
            screen.blit(background, (0, 0))
        if game_count in range(9, 16):
            screen.blit(background2, (0, 0))
        if game_count > 17:
            game_count = 0
        
    
        win_font = pygame.font.Font('/Users/charlieyorke/ace/imgs/pokemon-gb-font.tff/pokemonfont.ttf', 50)
        win_font_n = win_font.render('WINNER: NARUTO', 1, (0, 0, 0))
        win_font_s = win_font.render('WINNER: SASUKE', 1, (0, 0, 0))

        if level.p1_winner == True:
            win_count += 1
            #print(win_count)
            if win_count < 200:
                screen.blit(ko, (400, 150))
            if win_count > 201:
                playagain_button.draw()
                aftergamemenu_button.draw()
        if level.p2_winner == True:
            win_count += 1
            #print(win_count)
            if win_count < 200:
                screen.blit(ko, (400, 150))
            if win_count > 201:
                playagain_button.draw()
                aftergamemenu_button.draw()
        
        if fight_count < 100:
            screen.blit(fight_symobl, (350, 250))
            level.running = False
        if fight_count in range(101, 150):
            level.running = True

        pygame.display.init()
        
        level.run()

def control_page():
    run = True
    while run:
        screen.fill('black')
        screen.blit(controls_page_image, (0, 0))
        back_button.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and back_button.draw():
                main_menu()

def game_logic():
    run = True
    while run:
        screen.fill('black')
        screen.blit(game_logic_image, (0, 0))
        back_button.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and back_button.draw():
                main_menu()
            
def pause():
    
    paused = True

    font = pygame.font.SysFont("Comicsans", 40)

    #menu_button.draw()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if menu_button.draw():
                main_menu()

            elif return_button.draw():
                paused = False
        
        pygame.draw.rect(screen, (255, 255, 255), (300, 176, 600, 352))
        menu_button.draw()
        return_button.draw()
        pygame.display.update()

def main_menu():
    run = True
    count = 0
    count2 = 0
    FPS = 75
    while run:
        count += 1
        count2 += 1
        #print(count)
        level.running = False
        level.p1_winner = False
        level.p2_winner = False
        screen.blit(title, (450, -20))
        screen.blit(mm23, (0, 0))
        if count2 >= 1:
            start_button.draw()
            settings_button.draw()
            exit_button.draw()
            control_button.draw()
            screen.blit(title, (450, -20))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and start_button.draw():
                level.reset()
            if event.type == pygame.MOUSEBUTTONDOWN and control_button.draw():
                control_page()
            if event.type == pygame.MOUSEBUTTONDOWN and settings_button.draw():
                game_logic()
            if event.type == pygame.MOUSEBUTTONDOWN and exit_button.draw():
                sys.exit()

    pygame.quit()

def intro():
    run = True
    count = 0
    while run:
        count += 1
        pygame.display.update()
        if count in range(1, 20):
            screen.blit(mm1, (0, 0))
        if count in range(21, 40):
            screen.blit(mm2, (0, 0))
        if count in range(41, 60):
            screen.blit(mm3, (0, 0))
        if count in range(61, 80):
            screen.blit(mm4, (0, 0))
        if count in range(81, 100):
            screen.blit(mm5, (0, 0))
        if count in range(101, 120):
            screen.blit(mm6, (0, 0))
        if count in range(121, 140):
            screen.blit(mm7, (0, 0))
        if count in range(141, 160):
            screen.blit(mm8, (0, 0))
        if count in range(161, 180):
            screen.blit(mm9, (0, 0))
        if count in range(181, 200):
            screen.blit(mm10, (0, 0))
        if count in range(201, 220):
            screen.blit(mm11, (0, 0))
        if count in range(221, 240):
            screen.blit(mm12, (0, 0))
        if count in range(241, 260):
            screen.blit(mm13, (0, 0))
        if count in range(261, 280):
            screen.blit(mm14, (0, 0))
        if count in range(281, 300):
            screen.blit(mm15, (0, 0))
        if count in range(301, 320):
            screen.blit(mm16, (0, 0))
        if count in range(321, 340):
            screen.blit(mm17, (0, 0))
        if count in range(341, 360):
            screen.blit(mm18, (0, 0))
        if count in range(361, 380):
            screen.blit(mm19, (0, 0))
        if count in range(381, 440):
            screen.blit(mm20, (0, 0))
        if count in range(441, 500):
            screen.blit(mm21, (0, 0))
        if count in range(501, 560):
            screen.blit(mm22, (0, 0))
        if count >= 560:
            screen.blit(mm23, (0, 0))
            main_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

def loading_screen():
    run = True
    count = 0
    load_font = pygame.font.Font('/Users/charlieyorke/ace/imgs/plaguard-font/Plaguard-ZVnjx.otf', 18)
    load_font_1 = load_font.render('LOADING.', 1, (255, 255, 255))
    load_font_2 = load_font.render('LOADING..', 1, (255, 255, 255))
    load_font_3 = load_font.render('LOADING...', 1, (255, 255, 255))
    while run:
        pygame.display.update()
        count += 1
        if count in range(1, 15):
            screen.blit(load1, (0, 0))
            screen.blit(load_font_1, (567, 326))
        if count in range(16, 30):
            screen.blit(load1, (0, 0))
            screen.blit(load_font_2, (567, 326))
        if count in range(31, 45):
            screen.blit(load2, (0, 0))
            screen.blit(load_font_3, (567, 326))
        if count in range(46, 60):
            screen.blit(load2, (0, 0))
            screen.blit(load_font_1, (567, 326))
        if count in range(61, 75):
            screen.blit(load3, (0, 0))
            screen.blit(load_font_2, (567, 326))
        if count in range(76, 90):
            screen.blit(load3, (0, 0))
            screen.blit(load_font_3, (567, 326))
        if count in range(91, 105):
            screen.blit(load4, (0, 0))
            screen.blit(load_font_1, (567, 326))
        if count in range(106, 120):
            screen.blit(load4, (0, 0))
            screen.blit(load_font_2, (567, 326))
        if count in range(121, 135):
            screen.blit(load5, (0, 0))
            screen.blit(load_font_3, (567, 326))
        if count in range(136, 150):
            screen.blit(load5, (0, 0))
            screen.blit(load_font_1, (567, 326))
        if count in range(151, 165):
            screen.blit(load6, (0, 0))
            screen.blit(load_font_2, (567, 326))
        if count in range(166, 180):
            screen.blit(load6, (0, 0))
            screen.blit(load_font_3, (567, 326))
        if count in range(181, 195):
            screen.blit(load6, (0, 0))
            screen.blit(load_font_1, (567, 326))
        if count in range(196, 210):
            screen.blit(load6, (0, 0))
            screen.blit(load_font_2, (567, 326))
        if count in range(211, 225):
            screen.blit(load6, (0, 0))
            screen.blit(load_font_3, (567, 326))
        if count >= 225:
            intro()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

loading_screen()