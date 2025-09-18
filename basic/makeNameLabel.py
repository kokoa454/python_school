# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 14:20:53 2025

@author: Takahiro Suzuki
"""

def printLabel(name, padding):
    sentence = "Hello! " + name
    height = padding * 2 + 1 + 2 #paddingと文章行分とアスタリスク行分
    width = padding * 2 + len(sentence) + 2 #paddingと文章の文字分とアスタリスク分
    sentence_point = (height)  // 2 #文章行の位置を決める
    
    for i in range(height):
        if(i == 0 or i == height - 1):
            printAsteriskLine(width)
        elif(i == sentence_point):
            printSentenceLine(padding, sentence)
        else:  
            printSpaceLine(width - 2)
    
def printAsteriskLine(cnt):
    while(cnt > 0):
        print("*", end="")
        cnt -= 1
    print("")
    
def printSpaceLine(cnt):
    print("*", end="")
    while(cnt > 0):
        print(" ", end="")
        cnt -= 1
    print("*")
    
def printSentenceLine(cnt, sentence):
    print("*", end="")
    left_padding = cnt 
    while(left_padding > 0):
        print(" ", end="")
        left_padding -= 1
    print(sentence, end="")
    right_padding = cnt
    while(right_padding > 0):
        print(" ", end="")
        right_padding -= 1
    print("*")
        
def main():
    name = str(input("Type your name: "))
    print("\n")
    printLabel(name, padding = 1)
    
    
main()