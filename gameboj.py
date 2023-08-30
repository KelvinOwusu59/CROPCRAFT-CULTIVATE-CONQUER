import pygame

# A dictionary that contains the dimensions of various objects in the game
objRect = {
    'house1': [4, 6, 5, 6],
    'door': [6, 12, 1, 1],
    'house2': [3, 14, 1, 1],
    'house3': [10, 2, 3, 4],
    'farm': [14, 9, 6, 4],
    'bridge': [18, 19, 1, 6],
    'fence1': [20, 9, 1, 4],
    'fence5': [14, 8, 6, 1],
    'fence2': [13, 9, 1, 3],
    'fence3': [16, 13, 7, 4],
    'fence4': [14, 13, 3, 1],
    'water1': [1, 1, 1, 5],
    'water2': [0, 6, 1, 9],
    'water3': [0, 15, 3, 2],
    'water4': [0, 17, 1, 5],
    'water5': [0, 20, 18, 1],
    'water6': [19, 20, 4, 1],
    'water7': [22, 16, 10, 5],
    'water8': [24, 0, 8, 16],
    'water9': [3, 0, 19, 1],
}


def getCollisionRects():
    # Create an empty list to hold the rectangles
    rectobj = []
    # Get the values of all the rectangles from objRect
    rectsvalue = [x for x in objRect.values()]
    # Iterate over each rectangle in the list of rectangle values
    for rects in rectsvalue:
        # Create a pygame Rect object for the current rectangle, and multiply its dimensions by 16
        rect = pygame.Rect(rects[0]*16, rects[1]*16, rects[2]*16, rects[3]*16)
        # Add the new rectangle to the list of rectangles
        rectobj.append(rect)
    # Return the list of rectangles
    return rectobj


class TileSheet:
    def __init__(self, filename, height, width, cols, rows) -> None:
        # Load the tile sheet image and convert it to an alpha surface
        self.image = pygame.image.load(filename).convert_alpha()
        # Create an empty list to hold the tiles
        self.tile_map = []
        # Iterate over each column in the tile sheet
        for x in range(0, cols):
            # Create a new empty list to hold the tiles in the current row
            line = []
            # Add the new row list to the tile map
            self.tile_map.append(line)
            # Iterate over each row in the tile sheet
            for y in range(0, rows):
                # Calculate the rectangle for the current tile
                rect = (x*width, y*height, width, height)
                # Get the subsurface of the tile sheet for the current rectangle, and add it to the current row
                line.append(self.image.subsurface(rect))

    def gettile(self, pos):
        # Get the x and y indices of the tile from the given position
        x = pos[0]
        y = pos[1]
        # Return the tile at the specified position
        return self.tile_map[x][y]

    def draw(self, screen):
        # Iterate over each row in the tile map
        for x, row in enumerate(self.tile_map):
            # Iterate over each tile in the current row
            for y, tile in enumerate(row):
                # Draw the tile on the screen at the appropriate position
                screen.blit(tile, (x*16, y*16))

    def collisionRects(self, screen):
        # Get the values of all the rectangles from objRect
        rectsvalue = [x for x in objRect.values()]
        # Iterate over each rectangle in the list of rectangle values
        for rects in rectsvalue:
            # Draw a blue rectangle on the screen for the current rectangle, with its dimensions multiplied by 16
            pygame.draw.rect(screen, 'blue', [
                             rects[0]*16, rects[1]*16, rects[2]*16, rects[3]*16])


class NpcObject:
    def __init__(self, screen, filename_dimm, pos, iscanreact):
        # Initialize instance variables
        self.objpos = ()  # unused variable
        self.counter = 0
        self.objectsprite = TileSheet(*filename_dimm).tile_map
        self.objectsprite = [y for x in self.objectsprite for y in x]

        self.iscanreact = iscanreact
        self.pos = pos

    def animate_chest(self, screen):
        # Animate chest sprite
        if self.counter + 1 >= 12:
            self.counter = 0
        screen.blit(self.objectsprite[self.counter // 4], self.pos)
        self.counter += 1

    def animate_door(self, screen, isatdoor):
        # Animate door sprite based on whether player is at the door
        if self.counter + 1 >= 12:
            self.counter == 0  # should be assignment operator = instead of comparison operator ==
        if isatdoor:
            screen.blit(self.objectsprite[self.counter // 4], self.pos)
        else:
            screen.blit(self.objectsprite[0], self.pos)


class Slider:
    def __init__(self, sliderpos, standard) -> None:
        # Set the slider properties
        self.STANDARD = standard
        self.SLIDER_WIDTH = 8*16
        self.SLIDER_HEIGHT = 1*16
        self.SLIDER_X = sliderpos[0]
        self.SLIDER_Y = sliderpos[1]
        self.SLIDER_MIN_VALUE = 0
        self.SLIDER_MAX_VALUE = 100
        self.SLIDER_DEFAULT_VALUE = 50

        # Create the slider and knob rectangles
        self.slider_rect = pygame.Rect(
            self.SLIDER_X, self.SLIDER_Y, self.SLIDER_WIDTH, self.SLIDER_HEIGHT)
        self.knob_width = 20
        self.knob_height = 20
        self.knob_rect = pygame.Rect(self.SLIDER_X, self.SLIDER_Y - self.knob_height /
                                     2 + self.SLIDER_HEIGHT/2, self.knob_width, self.knob_height)

        # Position the knob based on the default value
        self.knob_rect.x = int((self.SLIDER_DEFAULT_VALUE / self.SLIDER_MAX_VALUE)
                               * (self.SLIDER_WIDTH - self.knob_width) + self.SLIDER_X)
        self.value = None
        self.dragging = False

    def draw_text(self, surface, text):
        # Helper function to draw the text label next to the slider
        x = self.SLIDER_X + self.SLIDER_WIDTH-32
        y = self.SLIDER_Y + 24
        font = pygame.font.Font(None, 16)
        text = font.render(text, True, 'black')
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        surface.blit(text, text_rect)

    def render(self, screen, color_s, color_kn):
        # Draw the slider and knob
        pygame.draw.rect(screen, color_s, self.slider_rect)
        pygame.draw.rect(screen, color_kn, self.knob_rect)
        self.draw_text(screen, f'{self.value}/{self.STANDARD}')

    def updateSlidder(self, event):
        # Update the slider value based on user input

        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse is clicking the knob
            if self.knob_rect.collidepoint(event.pos):
                # If so, set the self.dragging flag to true
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # If the mouse is released, set the self.dragging flag to false
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            # If the mouse is being dragged, move the knob accordingly
            if self.dragging:
                self.knob_rect.x = event.pos[0] - self.knob_width/2
                # Make sure the knob stays within the slider bounds
                if self.knob_rect.x < self.SLIDER_X:
                    self.knob_rect.x = self.SLIDER_X
                elif self.knob_rect.right > self.SLIDER_X + self.SLIDER_WIDTH:
                    self.knob_rect.right = self.SLIDER_X + self.SLIDER_WIDTH

        # Calculate the slider value based on the knob position
        self.value = round((self.knob_rect.x-self.SLIDER_X) /
                           self.SLIDER_WIDTH * self.STANDARD, 0)
        return self.value
