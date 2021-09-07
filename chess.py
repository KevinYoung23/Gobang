# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 14:26:27 2021

@author: Kevi023
"""

import pygame

class chess():
    def __init__(self, color, x_coor_re, y_coor_re):
        self.color = color #0 for null, 1 for white, 2 for black
        self.xr = x_coor_re
        self.yr = y_coor_re
        self.xd = 70 + x_coor_re * 40
        self.yd = 70 + y_coor_re * 40
        

def createChessboard():
    chessboard = [['.' for i in range (15)] for j in range(15)]
    for i in range (15):
        for j in range (15):
            chessboard[i][j] = chess(0, i, j)
    return chessboard

def updateChessboard(chessboard, color, x_coor_re, y_coor_re):
    if x_coor_re < 0 or x_coor_re >= 15 or y_coor_re < 0 or y_coor_re >= 15:
        return False
    else:        
        if chessboard[x_coor_re][y_coor_re].color == 0:
            chessboard[x_coor_re][y_coor_re].color = color
            return True
        else:
            return False
  
def drawChess(screen, chessboard):
    color_list = [(227, 146, 101), (255, 255, 255), (0, 0, 0)]
    radius = 10
    width = 10
    for i in range(15):
        for j in range(15):
            color = color_list[chessboard[i][j].color]
            center = x, y = chessboard[i][j].xd, chessboard[i][j].yd
            pygame.draw.circle(screen, color, center, radius, width)
    pygame.display.flip()
    
def getMouseClickPos():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x > 50 and x < 650 and y > 50 and y < 650:
                    x_ch = (x - 50) // 40
                    y_ch = (y - 50) // 40
                    position = x_ch, y_ch
                return position
