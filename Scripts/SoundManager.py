from Globals import *

class SoundManager:
    def __init__(self):
        self.sounds = [row.strip('\n') for row in open("./sounds.txt" , 'r').readlines()]
        #self.sound = [row.strip('\n') for row in open(self.sounds[0], 'r').readlines()]

        
