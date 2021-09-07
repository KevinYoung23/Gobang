# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 15:47:59 2021

@author: Kevi023
"""

import pygame
import sys
import chess
import play

def drawChessboard(screen):
    width = 2
    color_line = (0, 0, 0)
    color_board = (227, 146, 101)
    pygame.draw.rect(screen, color_board, [25, 25, 650, 650])
    for i in range(16):
        start_hor = (50, 50 + i * 40)
        end_hor = (650, 50 + i * 40)
        start_ver = (50 + i * 40, 50)
        end_ver = (50 + i * 40, 650)
        pygame.draw.line(screen, color_line, start_hor, end_hor, width)
        pygame.draw.line(screen, color_line, start_ver, end_ver, width)
        
   
def main():
    pygame.init()
    pygame.display.set_caption("Gobang Alpha")
    size = height, width = 700, 700
    screen = pygame.display.set_mode(size)
    chessboard = chess.createChessboard()
    drawChessboard(screen)
    pygame.display.flip() 
    
    player = 2
    
    #point_player = 0
    point_AI = 0
    
    count = 0
    
    xlim = 6, 8
    ylim = 6, 8
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((100, 100, 100))
        drawChessboard(screen)
        
        #player choose the position for the chess
        if player == 2:
            position = chess.getMouseClickPos()
            while not chess.updateChessboard(chessboard, player, position[0], position[1]):
                position = chess.getMouseClickPos()
                
        #AI decides the position for the chess
        else:
            print(count)
            position = play.play(xlim, ylim, count, chessboard, player, point_AI)
        count += 1
        chess.drawChess(screen, chessboard)
        
        if position[0] < 7 and position[0] < xlim[0] + 1:
            if position[0] <= 1:
                xlim = 0, xlim[1]
            else:
                xlim = position[0] - 1, xlim[1]
        elif position[0] > 7 and position[0] > xlim[1] - 1:
            if position[0] >= 13:
                xlim = xlim[0], 14
            else:
                xlim = xlim[0], position[0] + 1
        
        if position[1] < 7 and position[1] < ylim[0] + 1:
            if position[1] <= 1:
                ylim = 0, ylim[1]
            else:
                ylim = position[1] - 1, ylim[1]
        elif position[1] > 7 and position[1] > xlim[1] - 1:
            if position[1] >= 13:
                ylim = ylim[0], 14
            else:
                ylim = ylim[0], position[1] + 1
        print(xlim, ylim)
        
        if play.checkForWin(chessboard, position[0], position[1]):
            print("Game Over")
            break
        
        player = play.togglePlayer(player)
        
        pygame.display.flip()
        
    pygame.quit()

if __name__ == "__main__":
    main()            