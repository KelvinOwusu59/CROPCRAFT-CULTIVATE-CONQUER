import sys
import pygame

from gameboj import Slider


class MenuText:
    def __init__(self, xpos, y_poss, items) -> None:
        # Set properties for menu items
        self.item_font = pygame.font.Font(None, 24)
        self.item_names = items
        self.item_y_positions = y_poss
        self.xpos = xpos
        self.selected_item = None
        self.value = None

    def textEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a new item was clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i in range(len(self.item_names)):
                # Get rect for item name
                item_rect = self.item_font.render(self.item_names[i], True, (0, 0, 0)).get_rect(
                    x=self.xpos, y=self.item_y_positions[i])
                # Check if mouse collides with item rect
                if item_rect.collidepoint(mouse_x, mouse_y):
                    self.selected_item = i
                    self.value = self.item_names[i]
        return self.value

    def render(self, screen):
        for i in range(len(self.item_names)):
            # Render item name
            item_surface = self.item_font.render(
                self.item_names[i], True, (0, 0, 0))
            item_rect = item_surface.get_rect(
                x=self.xpos, y=self.item_y_positions[i])
            # Check if item is selected and draw rectangle
            if self.selected_item == i:
                pygame.draw.rect(screen, 'brown', item_rect, 2)
            # Blit item name to screen
            screen.blit(item_surface, item_rect)


class MenuItems:
    def __init__(self, filename, screen) -> None:
        # load menu image and set screen
        self.menu = pygame.image.load(filename).convert_alpha()
        menu_rect = self.menu.get_rect()
        self.screen = screen

        # initialize sliders
        self.n = Slider([17*16, 12*16], 250)
        self.p = Slider([17*16, 14*16], 250)
        self.k = Slider([17*16, 16*16], 250)
        self.soilph = Slider([17*16, 18*16], 10)
        self.water = Slider([17*16, 20*16], 10)

        # initialize text selections and mouse image
        self.mouse = pygame.image.load('assets/cursor.png').convert_alpha()
        self.mouse_rect = self.mouse.get_rect()
        self.mouse_rect.x = 200
        self.mouse_rect.y = 200
        self.fruits_texts = MenuText(
            6*16, [11*16, 13*16], ['Tomatoes', 'Corn'])
        self.season_text = MenuText(
            6*16, [17*16, 19*16, 21*16, 23*16], ['Winter', 'Summer', 'Fall', 'Spring'])

        # initialize save and close button
        self.close_b = pygame.Rect(208, 352, 48, 16)
        self.save_b = pygame.Rect(368, 368, 48, 16)
        self.data = [[]]
        self.show_menu = True

    def menu_events(self, event, player):
        # update sliders with event
        n = self.n.updateSlidder(event)
        p = self.p.updateSlidder(event)
        k = self.k.updateSlidder(event)
        soilph = self.soilph.updateSlidder(event)
        water = self.water.updateSlidder(event)
        fruits = self.fruits_texts.textEvent(event)
        season = self.season_text.textEvent(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            # check if mouse is clicked
            whocolided = self.mouse_rect.collidelist(
                [self.save_b, self.close_b])
            if whocolided != -1:
                if whocolided == 0:
                    # save button clicked
                    print('save')
                    player.show_menu = False
                    self.data.append([n, p, k, soilph, water, fruits, season])
                    if len(self.data) > 1:
                        self.data.pop(0)

                elif whocolided == 1:
                    # close button clicked
                    print('close')
                    self.data = [[]]
                    player.show_menu = False
                    if len(self.data) > 1:
                        self.data.pop(0)

    def render(self):
        # set mouse position and render menu elements
        self.mouse_rect.x, self.mouse_rect.y = pygame.mouse.get_pos()
        self.screen.blit(self.menu, (4*16, 8*16))
        self.n.render(self.screen, 'brown', 'black')
        self.p.render(self.screen, 'green', 'black')
        self.k.render(self.screen, 'blue', 'black')
        self.fruits_texts.render(self.screen)
        self.season_text.render(self.screen)
        self.soilph.render(self.screen, 'brown', 'black')
        self.water.render(self.screen, 'brown', 'black')
        self.screen.blit(self.mouse, self.mouse_rect)


class MainMenu:
    def __init__(self) -> None:

        # Load the music file
        self.musicplayer('assets/audio/Audio/8-Bit jingles/jingles_NES00.ogg')

        # load menu image
        self.img = pygame.image.load('assets/menuscreen.png').convert_alpha()
        # self.img = pygame.transform.s
        self.image_rect = self.img.get_rect()

        # self.image_rect.center = (512//2,512//2)

        self.start_button = pygame.Rect(320, 352, 64, 32)
        self.quit_button = pygame.Rect(112, 352, 64, 32)
        self.mouse = pygame.image.load('assets/cursor.png').convert_alpha()
        self.mouse_rect = self.mouse.get_rect()
        # setting game state
        self.game_state = 'menu'

    def musicplayer(self, file):
        # Load the music file
        # pygame.mixer.music.load(file)
        # Start playing the music
        # pygame.mixer.music.play()
        pass

    def main_menu_event(self, event):
        self.mouse_rect.center = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_selected = self.mouse_rect.collidelist(
                [self.start_button, self.quit_button])
            if button_selected == 0:
                print('start game')
                self.musicplayer(
                    'assets/audio/Audio/8-Bit jingles/jingles_NES14.ogg')
                self.game_state = 'start'
            elif button_selected == 1:
                self.musicplayer(
                    'assets/audio/Audio/8-Bit jingles/jingles_NES14.ogg')
                sys.exit()
            else:
                pass

    def render(self, screen):
        # render the menu items
        print('renderinng')
        screen.blit(self.img, (0, 0))
        # render the mouse
        screen.blit(self.mouse, self.mouse_rect)
        pygame.display.flip()

    def gamestate(self):
        return self.game_state
