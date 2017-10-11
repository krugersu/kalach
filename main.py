
# coding: utf-8


import os
import sys
import argparse

#***************
import game
import data



def main(arguments):
    data.w_step = 0
    game.m_NewGame()
    
    while  data.w_step != 2:
        print(data.playfield)
        if data.w_step == 1:
            box = int(input('Какой номер коробочки? '))
            game.m_Move(box,data.w_step)
        else:
            game.m_analis()
            game.m_Move(0,data.w_step)
            
   # game.m_Move()
    
    #if len(data.playfield) > 0: 
      #  data.playfield[3] = 8
      #  print(data.playfield)
    

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))