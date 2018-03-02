from Globals import *

class GameStateManager:
    def __init__(self):
        self.currentState = "game"

    def startState(self, state):
        if self.currentState == "pause" and self.currentState != "pause":
            self.currentState = "pause"
        if self.currentState == "game" and self.currentState != "game":
            self.currentState = "game"
    def getCurrentState(self):
        return self.currentState
    def update(self):
        #this is going to be the place where all the update functions are called once every frame, all i have to do is move the functions from engine.py
        #I think it's going to be a lot of work but its good not to have one giant file, and spread the code evenly throughout the program.
        #Maybe I can add all sprites into a single sprite manager class, and i would be able to update it all with a single function.

        if self.currentState == "pause":
            self.startState("game")
            #add update methods and call for when the player is in the pause menu
        if self.currentState == "game":
            pass
            #add update methods and calls for when the player is in the game update state
