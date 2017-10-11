# coding: utf-8

import data

#v_repeat_stroke = False

#n_h_Kalach = 13 # номер в массиве Калах человека
#n_m_Kalach = 6  # номер в массиве Калах машины

#h_Kalach = data.playfield[13] # Калах человека
#m_Kalach = data.playfield[6]  # Калах машины


def m_NewGame():
    data.playfield = [6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0] #Игровое поле
    print(data.playfield)
    
    
#v_box -  Номер коробочки с которой начинается ход
#h_g   -  Чей ход 0 - машины  1 - человека 
def m_Move(v_box,h_g):
    
    v_stone = data.playfield[v_box] # Количество комней в коробочке 
    print(v_stone)
    data.playfield[v_box] = 0 # Забрали все камни из коробочки
    
    # Раскладывание камней
    while v_stone != 0:
        v_box += 1
        if v_box == 14:
            v_box = 0
        data.playfield[v_box] += 1
        v_stone -= 1
        
    data.v_repeat_stroke = v_box == data.n_m_Kalach or v_box == data.n_h_Kalach # Повтор хода
    
    if not data.v_repeat_stroke and v_box < 7: # Закончили в своей коробочке
        # Проверка на то, что закончили в пустой коробочке
        if  data.playfield[v_box] == 1 and h_g == 0 and data.playfield[data.map_box[v_box]] != 0:
            data.playfield[data.n_m_Kalach] = data.playfield[data.n_m_Kalach] + 1 + data.playfield[data.map_box[v_box]]
            data.playfield[v_box] = 0
    data.w_step = 1        
    

def m_HumanMove(n_Box):
    pass

def m_FirstMove():
    pass

def m_analis(): 
    pass
