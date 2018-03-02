#########################################################################
# Basic engine                                                          #
#                                                                       #
#                                                                       #
#                                                                       #
#                                                                       #
#                                                                       #
#########################################################################
from Engine import *
debug = False
if debug == True:
    file = open("version.txt")
    for lines in file.readlines():
        print(lines)
Engine.update()
#########################################################################
# This is the base                                                      #
# for the game engine                                                   #
# that im creating in python                                            #
# and pygame                                                            #
#                                                                       #
#                                                                       #
#########################################################################
