import pygame
from Enermies import Enemy
from crops import DrawCrops
from functions import simulate
from gameboj import NpcObject, TileSheet
from menuui import MenuItems
from player import Player


class Level1:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.world = TileSheet('assets/main_world.png', 16, 16, 32, 32)
        self.menu = MenuItems('assets/menui.png', self.screen)
        self.player = Player()
        self.chess = NpcObject(
            self.screen, ['assets/chest.png', 16, 16, 5, 1], (4*16, 12*16), False)
        self.countdown_timer = 40
        self.font = pygame.font.Font(None, 14)
        self.remaining_time = 100000000000000000000
        self.start_count = False
        self.countdown_start_ = False
        self.countdown_start_time = pygame.time.get_ticks()
        self.enermies = [Enemy() for x in range(20)]
        self.fruits = {
            'Corn':DrawCrops('Corn'),
            'Tomatoes':DrawCrops('Tomatoes')
        }
        enemies = pygame.sprite.Group()
        self.enermycount = 0
        self.getmenudata = []
        self.plantChosen = None

    

    def update(self):
            pass

    def events(self,event):
        self.show_menu = self.player.collisionobj()
        if len(self.menu.data[0]) == 0:
            self.start_count = False
            
        else:
             
            self.start_count = True
            self.plantChosen = self.menu.data[0][5]
            self.getmenudata.append(simulate(self.menu.data[0][5], self.menu.data[0][6], self.menu.data[0][3], self.menu.data[0][4], [
                                    self.menu.data[0][0], self.menu.data[0][1], self.menu.data[0][2]]))
            
            
        self.menu.menu_events(event, self.player)


    def render(self):

        self.world.draw(self.screen)
        if self.player.show_menu:
            self.menu.render()
        else:
            self.player.draw(self.screen)
            if self.start_count :
                for  x, enermies in enumerate(self.enermies):
                    enermies.draw(self.screen)
                    enermies.update()
             
                    get_enermy = self.player.playershadow.collidelist([enermies.get_enermy_rect() for x in self.enermies])
                    if get_enermy !=-1:
                        self.enermies.pop(x)
                        self.enermycount +=1
                 
            
        
        if self.start_count:
            self.countdown()
            # if self.game_not_ended:
            self.fruits[self.menu.data[0][5]].animate(self.screen,(224, 144))
        self.player.player_movement()
        
        pygame.display.flip()

 

    def countdown(self):
        # calculate remaining time and display on screen
        #  (pygame.time.get_ticks()//1000)
        remaining_time = self.countdown_timer - \
            (pygame.time.get_ticks() - self.countdown_start_time) // 1000
        if remaining_time < 0:
            remaining_time = 0
        text = self.font.render(f'Time: {remaining_time:.1f}', True, (0, 0, 0))
        self.screen.blit(text, (16, 16))
        
        self.remaining_time = remaining_time

 