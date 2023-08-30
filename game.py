import random
import pygame
import sys
from Enermies import Enemy
from crops import DrawCrops
import fruits
from functions import simulate
from gameboj import NpcObject, TileSheet
from graph import plot_graph
from level import Level1
from menuui import MainMenu, MenuItems
from player import Player



class Game:
    def __init__(self) -> None:
        pygame.init()
        # game state
        # initialize menu
        self.clock = pygame.time.Clock()
        # set screen dimensions and initialize pygame
        SCREENWIDTH = 512
        SCREENHEIGHT = 512
        self.screen = pygame.display.set_mode((SCREENHEIGHT, SCREENWIDTH))
        self.game_state = 'menu'
        self.level1 = Level1(self.screen) 
        self.main_menu = MainMenu()


        # self.enemy = Enemy(512, 512, 400, 300)  # create a new enemy at position (100, 100) moving towards (400, 300)

    def game_state_event(self):
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               sys.exit()
           if self.game_state == 'menu':
                self.main_menu.main_menu_event(event)
           if self.game_state == 'start':
                self.level1.events(event)
                self.level1.update()


    def play_song(self,song_path):
        # Initialize Pygame and the mixer module
        # Load the song file into the mixer module
        pygame.mixer.init()
        pygame.mixer.music.load(song_path)
        # pygame.mixer.music.load(file)
        # Play the song
        pygame.mixer.music.play(-1, 0.0)
        # Wait for the song to finish playing

    def render(self):
        if self.game_state == 'menu':
            self.main_menu.render(self.screen)
            self.game_state = self.main_menu.game_state
            # self.play_song('assets/audio/Track_#4.wav')
            pass
        if self.game_state == 'start':
            self.level1.render()
                # update the position of the enemy
            # self.play_song('assets/audio/cave_theme_1.wav')
        if self.level1.remaining_time == 0:
            # self.play_song('assets/audio/Game_Over_1.wav')
            self.game_state = 'graph'
            print(self.level1.getmenudata)
            plot_graph(self.screen,self.level1.getmenudata,'time','data',self.level1.plantChosen,self.level1.enermycount)
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.level1.countdown_start_time =pygame.time.get_ticks()
                self.game_state = 'start'
    


    def update(self):
        self.play_song('assets/audio/cave_theme_1.wav')
        while True:
            self.game_state_event()
            self.render()
 
            self.clock.tick(12)
            pass


if __name__ == '__main__':
    Game().update()