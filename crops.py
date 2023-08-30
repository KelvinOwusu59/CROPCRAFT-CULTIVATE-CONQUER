import pygame


class DrawCrops:
    # dictionary mapping crop names to lists of image paths
    crops = {
        'Tomatoes': ['assets/p2seeding.png', 'assets/p2growing.png',
                     'assets/p2harvest1.png',
                     'assets/p2harvest2.png',
                     'assets/p2harvest.png',
                     ],
        'Corn': [
            'assets/seeding.png', 'assets/growing.png',
            'assets/harvest.png',
            'assets/harvest.png',
            'assets/postharvest.png',
        ]
    }

    def __init__(self, plant):
        # set frames to the corresponding list of image paths from the crops dictionary
        self.frames = self.crops[plant]
        # initialize framecount to 0
        self.framecount = 0

    def animate(self, screen, pos):
        # increment framecount and loop back to 3 once it reaches 12
        if self.framecount + 1 >= 12:
            self.framecount = 0
        # load the appropriate image from frames based on framecount and blit it to screen at pos
        load_image = pygame.image.load(self.frames[4])
        screen.blit(load_image, pos)
        self.framecount += 1
