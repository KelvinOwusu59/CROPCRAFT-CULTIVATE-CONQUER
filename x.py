import random
import pygame
import sys
from crops import DrawCrops
import fruits
from functions import simulate
from gameboj import NpcObject, TileSheet
from graph import plot_graph
from menuui import MainMenu, MenuItems
from player import Player



class Game:
    def __init__(self) -> None:
        pygame.init()
        # game state
        # initialize menu

        # set screen dimensions and initialize pygame
        SCREENWIDTH = 512
        SCREENHEIGHT = 512
        self.screen = pygame.display.set_mode((SCREENHEIGHT, SCREENWIDTH))
        self.clock = pygame.time.Clock()
        self.game_state = 'start'
        
        self.main_menu = MainMenu()
        # load assets
        self.world = TileSheet('assets/new_world2.png', 16, 16, 32, 32)
        self.counter = 0
        self.menu = MenuItems('assets/menui.png', self.screen)
        countdown_time = 30  # seconds
        self.countdown_timer = pygame.time.get_ticks() + countdown_time * 1000
        self.font = pygame.font.Font(None, 18)

        # create player and npc objects
        self.player = Player()
        self.chess = NpcObject(
            self.screen, ['assets/chest.png', 16, 16, 5, 1], (4*16, 12*16), False)
        self.farmpop = []
        self.show_menu = None
        self.timer = 0
        self.icanfarm = 'planting'
        self.harvest_time = False
        
        # create crop objects
        self.tomatoes = DrawCrops('Tomatoes')
        self.corn = DrawCrops('Corn')
        
        # create food basket
        self.food_basket = {
            'Tomatoes': [],
            'corn': []
        }
        
        # create graph data structure
        self.graph = []

    def countdown(self):
        # calculate remaining time and display on screen
        remaining_time = (self.countdown_timer -
                          pygame.time.get_ticks()) / 1000
        if remaining_time < 0:
            remaining_time = 0
        text = self.font.render(f'Time: {remaining_time:.1f}', True, (0, 0, 0))
        self.screen.blit(text, (10, 10))
        return remaining_time

    def event(self):
            # Handling events
            self.player.player_movement()
            self.show_menu = self.player.collisionobj()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.show = True

                self.menu.menu_events(event)
                print(self.menu.data)
            
            # Detecting whether user can plant or harvest
            if len(self.menu.data[0]) > 2:
                if self.menu.data[0][5] != None or self.menu.data[0][6] != None:
                    self.icanfarm = 'harvest'
                else:
                    self.icanfarm = 'planting'

    def render(self):
        # Rendering the game objects
        self.world.draw(self.screen)
        self.player.draw(self.screen)
        progress = pygame.image.load('assets/progress.png')
        self.screen.blit(progress, (28*16, 0))
        self.chess.animate_chest(self.screen)
        print(self.show_menu)
        self.timer = self.countdown()

        # Displaying menus and crops during appropriate times
        if (self.timer) != 0:
            if self.show_menu == 'farm':
                if self.icanfarm == 'planting':
                    self.menu.render()
            elif self.icanfarm == 'harvest':
                if self.menu.data[0].count('Tomatoes') == 1:
                    self.tomatoes.animate(self.screen, (224, 144))
                if self.menu.data[0].count('Corn') == 1:
                    self.corn.animate(self.screen, (224, 144))

                # Adding the simulated growth to the graph
                self.graph.append(simulate(self.menu.data[0][5], self.menu.data[0][6], self.menu.data[0][3], self.menu.data[0][4], [
                                    self.menu.data[0][0], self.menu.data[0][1], self.menu.data[0][2]]))

        else:
            print(self.graph)
            plot_graph(self.graph, 'days', 'fruits', self.menu.data[0][5])
            # reseetting all the data
            self.timer = 35
            self.menu.data.clear()
            self.farmpop = []
            self.show_menu = None
            self.timer = 0
            self.icanfarm = 'planting'
            self.harvest_time = False
            self.tomatoes = DrawCrops('Tomatoes')
            self.corn = DrawCrops('Corn')
            self.food_basket = {
                'Tomatoes': [],
                'corn': []
            }

        pygame.display.flip()

    def update(self):
        while True:
            self.main_menu.main_menu_event()
            self.main_menu.render(self.screen)
            if self.game_state == 'menu':
                pass
            elif self.game_state == 'start':
                self.event()
                self.render()
            self.clock.tick(12)
            pass


if __name__ == '__main__':
    Game().update()
