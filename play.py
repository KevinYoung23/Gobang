# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:08:37 2021

@author: Kevi023
"""

import chess
import random
#return type: string
#return format: number of consecutive chesses + 两边是否能下子
#2：both sides are available
#1: only one side is available
#0: both sides are not available

#check horizontally
def check_hor(chessboard, x, y):
    color = chessboard[x][y].color
    total = 1
    available = 2
    for i in range (x + 1, 15, 1):
        if chessboard[i][y].color == color:
            total += 1
        else:
            if i == 14:
                available -= 1
            elif chessboard[i+1][y].color != 0:
                available -= 1
            break
    for i in range (x - 1, -1, -1):
        if chessboard[i][y].color == color:
            total += 1
        else:
            if i == 0:
                available -= 1
            elif chessboard[i-1][y].color != 0:
                available -= 1
            break
    return str(str(total) + str(available))

#check vertically
def check_ver(chessboard, x, y):
    color = chessboard[x][y].color
    total = 1
    available = 2
    for j in range (y + 1, 15, 1):
        if chessboard[x][j].color == color:
            total += 1
        else:
            if j == 14:
                available -= 1
            elif chessboard[x][j+1].color != 0:
                available -= 1
            break
    for j in range (y-1, -1, -1):
        if chessboard[x][j].color == color:
            total += 1
        else:
            if j == 0:
                available -= 1
            elif chessboard[x][j-1].color != 0:
                available -= 1
            break
    return str(str(total) + str(available))
  
#check diagonally y = x  
def check_dia_1(chessboard, x, y):
    color = chessboard[x][y].color
    total = 1
    curr_y = y + 1
    available = 2
    for i in range (x + 1, 15, 1):
        if curr_y >= 15:
            break
        else:
            if chessboard[i][curr_y].color == color:
                total += 1
                curr_y += 1
            else:
                if i == 14:
                    available -= 1
                elif chessboard[i+1][curr_y].color != 0:
                    available -= 1
                break
    curr_y = y - 1
    for i in range (x - 1, -1, -1):
        if curr_y <= -1:
            break
        else:
            if chessboard[i][curr_y].color == color:
                total += 1
                curr_y -= 1
            else:
                if i == 0:
                    available -= 1
                elif chessboard[i-1][curr_y].color != 0:
                    available -= 1
                break
    return str(str(total)+str(available))

#check diagonally y = -x
def check_dia_2(chessboard, x, y):
    color = chessboard[x][y].color
    total = 1
    curr_y = y - 1
    available = 2
    for i in range (x + 1, 15, 1):
        if curr_y <= -1:
            break 
        else:
            if chessboard[i][curr_y].color == color:
                total += 1
                curr_y -= 1
            else:
                if i == 14:
                    available -= 1
                elif chessboard[i+1][curr_y].color != 0:
                    available -= 1
                break
    curr_y = y + 1
    for i in range (x - 1, -1, -1):
        if curr_y >= 15:
            break
        else:
            if chessboard[i][curr_y].color == color:
                total += 1
                curr_y += 1
            else:
                if i == 0:
                    available -= 1
                elif chessboard[i-1][curr_y].color != 0:
                    available -= 1
                break
    return str(str(total) + str(available))

def checkForWin(chessboard, x, y):
    color = chessboard[x][y].color
    if color == 0:
        return False
    else:
        res = max(int(check_hor(chessboard, x, y)[0]), 
                  int(check_ver(chessboard, x, y)[0]), 
                  int(check_dia_1(chessboard, x, y)[0]), 
                  int(check_dia_2(chessboard, x, y)[0]))
        if res >= 5:
            return True
        else:
            return False

def togglePlayer(player):
    #toggle between black chess and white chess
    return 3 - player

def evaluateChessboard(chessboard, x, y, point):
    point_dict = {'50' : 1000000,
                  '51' : 1000000,
                  '52' : 1000000,
                  '40' : 0,
                  '41' : 2500,
                  '42' : 300000,
                  '30' : 0,
                  '31' : 500,
                  '32' : 3000,
                  '20' : 0,
                  '21' : 50,
                  '22' : 400,
                  '10' : 0,
                  '11' : 0,
                  '12' : 0}
    res = point
    if chessboard[x][y].color == 0:
        pass
    else:
        print('checkpoint:', x, y)
        res += int(point_dict[check_hor(chessboard, x, y)])
        res += int(point_dict[check_ver(chessboard, x, y)])
        res += int(point_dict[check_dia_1(chessboard, x, y)])
        res += int(point_dict[check_dia_2(chessboard, x, y)])
    return res

def getMaxEvaluate(xlim, ylim, chessboard, leftStep, color, point):
    #xlim ylim to limit the evaluation area to reduce the calculation
    maxPosition = column, row = -1, -1
    maxValue = 0
    for i in range (xlim[0], xlim[1]+1):
        for j in range (ylim[0], ylim[1]+1):
            #check whether the position is too far from other chesses on the board. 
            #if there is not chess near the position, then we ignore this position
            #to be added 
            if chessboard[i][j].color != 0:
                continue
            else:
                chessboard[i][j].color = color
                val = evaluateChessboard(chessboard, i, j, point)
                if val > 800000:
                    maxPosition = i,j
                    return maxPosition, val
                if leftStep > 1:
                    nextStep = getMaxEvaluate(xlim, ylim, chessboard, leftStep - 1, 3 - color, point)
                    val = -nextStep[1]
                if maxPosition == (-1, -1) or val > maxValue:
                    maxPosition = i, j
                    maxValue = val
                chessboard[i][j].color = 0
    point += evaluateChessboard(chessboard, maxPosition[0], maxPosition[1], point)
    return maxPosition, maxValue
    

def play(xlim, ylim, count, chessboard, player, point):
    color = player
    #set the chess to the center of the board if this is the first step
    if count == 0:
        chess.updateChessboard(chessboard, color, 7, 7)
        position = 7, 7
    elif count == 1:
        if chessboard[7][7].color == 0:
            chess.updateChessboard(chessboard, color, 7, 7)
            position = 7, 7
        elif random.randint(0, 1):
            chess.updateChessboard(chessboard, color, 7, 8)
            position = 7, 8
        else:
            chess.updateChessboard(chessboard, color, 8, 8)
            position = 8, 8
    else:
        result = getMaxEvaluate(xlim, ylim, chessboard, 4, color, point)
        position = result[0]
        chess.updateChessboard(chessboard, color, position[0], position[1])
    
    return position 