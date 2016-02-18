# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:39:10 2016

@author: Leonardo
"""

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)