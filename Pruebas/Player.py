# Clase Personaje

import arcade
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

class Player(arcade.Sprite):
#Constructor/atributos---------------------------------------------------------------------------------------------------------------#

    def __init__(self):
        super().__init__(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk4.png")
    #Coordenadas---------------------------------------------------------------------------------------------------------------------#
        super.center_x = 0
        self.change_x = 0
        self.center_y_y = 0
        self.change_y = 0
        self.pos_z = 9
        self.change_z = 0
    #--------------------------------------------------------------------------------------------------------------------------------#

    #Sprite--------------------------------------------------------------------------------------------------------------------------#
        self.list = arcade.SpriteList()
        self.sprite.scale = 1
        self.change_scale = 0
        self.sprite.center_x = self.pos_x
        self.sprite.center_y = self.pos_y
        self.list.append(self.sprite)
    #--------------------------------------------------------------------------------------------------------------------------------#

     #Sprite--------------------------------------------------------------------------------------------------------------------------#
        """self.score = 0
        self.change_scale = change_scale
        self.max_left = max_left
        self.max_right = max_right
        self.max_far = max_far
        self.max_near = max_near"""
     #-------------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------------------#

    def draw(self):
        self.list.draw()

    def on_update(self):
    #Movimiento----------------------------------------------------------------------------------------------------------------------#
        center_x += self.change_x
        center_y += self.change_y
        self.pos_z += self.change_z
        self.sprite.scale += math.copysign(1, self.pos_z)*(self.change_scale)
        if(self.change_scale != 0): self.sprite.center_y += -(1/2)*self.sprite.height + (1/2)*self.sprite.height
        self.sprite.center_x = self.pos_x
        self.sprite.center_y = self.pos_y
    #--------------------------------------------------------------------------------------------------------------------------------#


        """self.pos_z += self.change_z
        height = self.sprite.height
        self.sprite.scale = list(self.sprite.scale)[0] + self.change_scale
        if(self.max_far <= self.pos_z <= self.max_near):
        #if(self.change_z != 0): self.change_y += list(self.sprite.scale)[0]*self.sprite.height*(-1) // (list(self.sprite.scale)[0]*(self.sprite.height/2)*(-1))*self.change_z
            self.sprite.center_y += -(1/2)*height + (1/2)*self.sprite.height
        elif(self.pos_z < self.max_far):
            self.sprite.scale = list(self.sprite.scale)[0] - self.change_scale
        elif(self.pos_z > self.max_near):
            self.sprite.scale = list(self.sprite.scale)[0] - self.change_scale
        self.sprite.center_x += self.change_x
        #print(f'X = {self.sprite.center_x} Y = {self.sprite.center_y}, Scale = {self.sprite.scale}')

        if self.sprite.center_x  > self.max_right:
            self.sprite.center_x = self.max_right
            #self.change_x *= -1

        if self.sprite.center_y > SCREEN_HEIGHT:
            self.sprite.center_y = SCREEN_HEIGHT
            self.change_y *= -1
        
        if self.sprite.center_x < self.max_left:
            self.sprite.center_x = self.max_left
            #self.change_x *= -1

        if self.sprite.center_y < 0:
            self.sprite.center_y = 0
            self.change_y *= -1"""