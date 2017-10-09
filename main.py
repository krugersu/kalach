
# coding: utf-8


import os
import sys
import argparse

#***************
import game
import data





def main(arguments):
    
    game.m_NewGame()
   # game.m_Move()
    print(data.playfield)
    if len(data.playfield) > 0: 
        data.playfield[3] = 8
      #  print(data.playfield)
    

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))