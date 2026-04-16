# Clase Player

# Clase Personaje

import arcade
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

class Player(arcade.Sprite):
#Constructor/atributos---------------------------------------------------------------------------------------------------------------#

    def __init__(self, path, scale = 1.0, center_x = 0.0, center_y = 0.0, angle = 0.0,):
    #Clase-Sprite--------------------------------------------------------------------------------------------------------------------#
        super().__init__(self, path_or_texture = path, scale = scale, center_x = center_x, 
                         center_y = center_y, angle = angle)
        """
        Atributos de la clase Sprite
            + self.path_or_texture: PathOrTexture | None = None
            + self.scale: float | Point2 = 1.0,
            + self.center_x: float = 0.0,
            + self.center_y: float = 0.0,
            + self.angle: float = 0.0,
            + **kwargs: Any
            + self._velocity = 0.0, 0.0
            + self.change_angle: float = 0.0
            + self.boundary_left: float | None = None
            + self.boundary_right: float | None = None
            + self.boundary_top: float | None = None
            + self.boundary_bottom: float | None = None
            + self.cur_texture_index: int = 0
            + self.textures: list[Texture] = _textures
            + self.physics_engines: list[Any] = []
            + self.guid: str | None = None
            + self._hit_box: RotatableHitBox = self._hit_box.create_rotatable(angle=self._angle)
            + self._width = self._texture.width * self._scale[0]
            + self._height = self._texture.height * self._scale[1]
        """
    
    #Coordenadas---------------------------------------------------------------------------------------------------------------------#
        self.center_x = super().center_x
        self.change_x = 0
        self.center_y = super().center_y
        self.change_y = 0
        self.pos_z = 9
        self.change_z = 0
    #--------------------------------------------------------------------------------------------------------------------------------#

    #Sprite--------------------------------------------------------------------------------------------------------------------------#
        """self.list = arcade.SpriteList()
        self.sprite.scale = 1
        self.change_scale = 0
        self.sprite.center_x = self.pos_x
        self.sprite.center_y = self.pos_y
        self.list.append(self.sprite)"""
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

    """def draw(self):
        self.list.draw()

    def on_update(self):
    #Movimiento----------------------------------------------------------------------------------------------------------------------#
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.pos_z += self.change_z
        self.sprite.scale += math.copysign(1, self.pos_z)*(self.change_scale)
        if(self.change_scale != 0): self.sprite.center_y += -(1/2)*self.sprite.height + (1/2)*self.sprite.height
        self.sprite.center_x = self.pos_x
        self.sprite.center_y = self.pos_y
    #--------------------------------------------------------------------------------------------------------------------------------#


        self.pos_z += self.change_z
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
    

class Player2(arcade.Sprite):
#Constructor/atributos---------------------------------------------------------------------------------------------------------------#

    def __init__(self, path):
    #Clase-Sprite--------------------------------------------------------------------------------------------------------------------#
        super().__init__(path)
        """
        Atributos de la clase Sprite
            + self.path_or_texture: PathOrTexture | None = None
            + self.scale: float | Point2 = 1.0,
            + self.center_x: float = 0.0,
            + self.center_y: float = 0.0,
            + self.angle: float = 0.0,
            + **kwargs: Any
            + self._velocity = 0.0, 0.0
            + self.change_angle: float = 0.0
            + self.boundary_left: float | None = None
            + self.boundary_right: float | None = None
            + self.boundary_top: float | None = None
            + self.boundary_bottom: float | None = None
            + self.cur_texture_index: int = 0
            + self.textures: list[Texture] = _textures
            + self.physics_engines: list[Any] = []
            + self.guid: str | None = None
            + self._hit_box: RotatableHitBox = self._hit_box.create_rotatable(angle=self._angle)
            + self._width = self._texture.width * self._scale[0]
            + self._height = self._texture.height * self._scale[1]
        """