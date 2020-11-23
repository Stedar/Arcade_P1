
import pygame
from pygame.sprite import Sprite
from enum import Enum
import os
import time

class CharacterStates(Enum):
    IDLE = 0
    MOVE = 1
    ATTACK = 2
    DEAD = 3
    DEFENCE = 4
    JUMP = 5

class GameObjectTypes(Enum):
    STATIC_OBJECT = 0
    MOVING_OBJECT = 1
    ENEMY = 2
    DARK_ANGEL = 3
    OTHER = 4

class Position():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class GameObject(Sprite):
    def __init__(self, x,y, name="noname"):
        Sprite.__init__(self)
        self.pos = Position(x,y)
        self.name = name
        self.current_frame_set = None
        self.frames = []      #
        self.current_frame = 0       # 
        self.image =  None #
        self.rect = None   # 
        self.hidden = False
        self.type = GameObjectTypes.OTHER
        self.f_elapsed_time = 0.0
        self.f_delay_time = 0.15

    def load_frames(self):
        pass
    def update_frame(self,current_time):
        pass

class GameCharacter(GameObject):
    def __init__(self, x,y, name="noname"):
        super().__init__(x,y,name)
        self.name+=name
        self.health = 10
        self.cur_health = 10
        self.type  = GameObjectTypes.DARK_ANGEL
        self.current_state = CharacterStates.IDLE



class CharachterDarkAngel(GameCharacter):
    def __init__(self, x,y, name="Angle1"):
        super().__init__(x,y,name)
        self.name+=name
        self.type = GameObjectTypes.DARK_ANGEL
        self.frames_running = []
        self.frames_idle = []
        self.f_delay_time =0.07 
        self.current_frame_sequence = None
   
        self.frames_running = load_sequence(os.path.normpath("data/FallenAngel/Running/0_Fallen_Angels_Running_"), "png", 12, 3, 0)
        self.current_frame_sequence = self.frames_running
        self.image = self.current_frame_sequence[self.current_frame]
       
    def update_frame(self,current_time):
       if current_time - self.f_elapsed_time >= self.f_delay_time:
           if self.current_frame<len(self.current_frame_sequence)-1:
               self.current_frame+=1
           else:
               self.current_frame = 0
           self.image = self.current_frame_sequence[self.current_frame] 
           self.f_elapsed_time = current_time
  
       print(self.current_frame,len(self.current_frame_sequence),self.f_elapsed_time,current_time)
 
   

class Render:
    def __init__(self, width, height, caption, game_object_list):
        # initialize the pygame module
        pygame.init()
        pygame.display.set_caption(caption)
        self.player = None
        self.game_object_list = game_object_list
     
      # create a surface on screen that has the size of width x height
        self.screen = pygame.display.set_mode((width,height))
     
        pygame.display.flip()
    
    def update_screen(self):
        cur_time = time.time()
        self.screen.fill([0,0,0])

        #game objects
        for i in self.game_object_list:
            i.update_frame(time.time())
            self.screen.blit(i.image,(0,0))    
            pygame.display.flip()


class GameLogic():
    def __init__(self):
        self.game_object_list = []
    
    def create_game_object(self,type, x,y, name ="noname"):
        if type == GameObjectTypes.DARK_ANGEL:
                DarkAngel = CharachterDarkAngel(x,y,name);
                self.game_object_list.append(DarkAngel)




def load_sequence(basename, ext, num, num_digits=1, offset=0,optimize=True):
    frames = []
    # format string basename+zero_padded_number+.+ext
    format = "%s%0"+str(num_digits)+"d.%s"
    for i in range(offset, num):
        print("df")
        name = format % (basename, i,ext);
        print(name)
        image = pygame.image.load(name) # not optimized
        image = pygame.transform.scale(image, (200, 200))
        if optimize:
            if image.get_alpha() is not None:
                image = image.convert_alpha()
            else:
                image = image.convert()
        frames.append(image)    
    return frames



def main():
    # initialize
    print("...is loading") 

    AGameLogic = GameLogic()
    AGameRender = Render(800,600,"Arcade_P1",AGameLogic.game_object_list)
    AGameLogic.create_game_object(GameObjectTypes.DARK_ANGEL,0,0, "My Angel")
        
#    DarkAngel = CharachterDarkAngel();

    #main loop
    running = True
    elapsed_time = 0
    while (running):
        AGameRender.update_screen()
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event if of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
    #graphic update

if __name__=="__main__":
# call the main function
    main()





