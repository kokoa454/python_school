# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 14:34:43 2025

@author: qqnq7
"""
import random

wordList = [
    'vodka',
    'borsch',
    'sputnik',
    'kiosk',
    'gulag',
    'tundra',
    'babushka',
    'troika',
    'Russia'
    ]

def pickWord():
    listLength = len(wordList)
    wordIndex = random.randint(0, listLength - 1)
    word = wordList[wordIndex]
    # 単語リストから選ばれた単語をリターン
    return word

def makeWordStringForQuestion(word, wordLength):
    hintAlphabetPosition = random.randint(0, wordLength - 1)
    hintAlphabet = word[hintAlphabetPosition]
    wordStringForQuestion = []
    
    # 選ばれた単語からヒントアルファベット以外の箇所を'_'に変換
    for i in range(wordLength):
        if(i == hintAlphabetPosition):
            wordStringForQuestion.append(hintAlphabet)
        else:
            wordStringForQuestion.append('_')
    
    # クイズとして表示される単語の文字列をリターン
    return wordStringForQuestion
        
def main():
    word = pickWord()
    wordLength = len(word)
    trialLimit = wordLength * 2
    print(f'Guess {len(word)} characters word in your mind under {trialLimit} times:')
    wordStringForQuestion = makeWordStringForQuestion(word, wordLength)
    
    while(trialLimit):
        guessedAlphabet = input(f'{''.join(wordStringForQuestion)}:')
        
        # wordの中身とguessedAlphabetを比較して、正解だったらwordStringForQuestionに反映
        for index, item in enumerate(word): 
            if(item == guessedAlphabet):
                wordStringForQuestion[index] = guessedAlphabet
            
        # '_'がwordStringForQuestionに存在しない = すべてのアルファベットが正解ならプログラムを終了させる
        if('_' not in wordStringForQuestion):
            print((f'{''.join(wordStringForQuestion)}:'))
            print("you've gotten it.")
            break
            
        trialLimit -= 1
    
    # 試行回数が上限を超えたら表示
    if(trialLimit == 0):
        print('Exceed trial limits.')
    
main()