# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:02:53 2021

@author: Kevi023
"""

import chess

class player():
    def __init__(self, color):
        self.color = color
    
    def evaluate(self):
        values = 0
        counter = 0
        for i in range (15):
            for j in range (15):
                
        
        
    def evaluateBoard(self):
        return self.evaluate(self.color) - self.evaluate(3 - self.color)
        