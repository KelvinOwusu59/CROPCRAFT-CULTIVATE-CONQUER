import pygame
from gameboj import NpcObject, TileSheet, getCollisionRects


class Player:
    def __init__(self):
        self.player_sprite = TileSheet('assets/player.png', 16, 16, 4, 4)
        self.movement = {
            'down': self.player_sprite.tile_map[0],
            'up': self.player_sprite.tile_map[1],
            'left': self.player_sprite.tile_map[2],
            'right': self.player_sprite.tile_map[3]
        }
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.standing = True
        self.playerpos_x = 144
        self.playerpos_y = 140
        self.speed = 5
        self.walkcount = 0
        self.playershadow = pygame.Rect(self.playerpos_x, self.playerpos_y, 16, 16)
        self.show_menu = False


    def player_movement(self):
        keys = pygame.key.get_pressed()

        # Move left
        if keys[pygame.K_LEFT]:
            self.left = True
            self.playerpos_x -= self.speed

        # Move right
        elif keys[pygame.K_RIGHT]:
            self.right = True
            self.playerpos_x += self.speed

        # Move up
        elif keys[pygame.K_UP]:
            self.up = True
            self.playerpos_y -= self.speed

        # Move down
        elif keys[pygame.K_DOWN]:
            self.down = True
            self.playerpos_y += self.speed

        # Player is not moving
        else:
            self.left = False
            self.right = False
            self.up = False
            self.down = False
            self.standing = True

    def draw(self, screen):
        if self.walkcount + 1 > 12:
            self.walkcount = 0

        # Draw player facing left
        if self.left:
            left_frame = self.movement['left']
            screen.blit(left_frame[self.walkcount//4], (self.playerpos_x, self.playerpos_y))

        # Draw player facing right
        elif self.right:
            right_frame = self.movement['right']
            screen.blit(right_frame[self.walkcount//4], (self.playerpos_x, self.playerpos_y))

        # Draw player facing up
        elif self.up:
            up_frame = self.movement['up']
            screen.blit(up_frame[self.walkcount//4], (self.playerpos_x, self.playerpos_y))

        # Draw player facing down
        elif self.down:
            down_frame = self.movement['down']
            screen.blit(down_frame[self.walkcount//4], (self.playerpos_x, self.playerpos_y))

        # Draw player standing still
        elif self.standing:
            screen.blit(self.movement['down'][0], (self.playerpos_x, self.playerpos_y))

        self.walkcount += 1
        self.playershadow.x = self.playerpos_x
        self.playershadow.y = self.playerpos_y

    def collisionobj(self):
        noncoliding_bodies = [2, 3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        door = [1]
        bridge = [5]
        farm = [4]

        # Get collision rectangles
        rects = getCollisionRects()

        # Check if player is colliding with any object
        iscollide = self.playershadow.collidelist(rects)

        if iscollide != -1:
            # Check for non-colliding objects
            if noncoliding_bodies.count(iscollide) > 0:
                self.playerpos_x = 184
                self.playerpos_y = 240
                return 'sea'

            if door.count(iscollide) > 0:
                # self.playerpos_x -= 10
                # self.playerpos_y -= 10
                return 'door'

            if farm.count(iscollide) > 0:
                self.playerpos_x = 184
                self.playerpos_y = 240
                self.show_menu = True
                return 'farm'
            else:
                return ''
        else:
            NpcObject('self.screen', [
                      'assets/door_close.png', 16, 16, 4, 1], (6*16, 11*16), 0)

            return ''