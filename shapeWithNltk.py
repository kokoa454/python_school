import re
import nltk

def no1():
    print("課題1")
    print("chapter1:")
    print("         section1-1:")
    print("                     section1-1-1:")
    print("                     section1-1-2:")
    print("chapter2:")

def no2():
    print("課題2")
    radius = input("半径を入力してください: ")
    print(f"半径{radius}の円の面積は{3.14 * float(radius) ** 2}です。")

def no3():
    print("課題3")
    radius = input("半径を入力してください: ")
    result = calcArea(radius)
    print(f"半径{radius}の円の面積は{result}です。")

def calcArea(radius):
    return 3.14 * float(radius) ** 2

def no4():
    print("課題4")
    numbers = input("空白で分離した数を入力してください: ")
    resultList = numbers.split(" ")
    print(f"List: {resultList}")
    resultTuple = tuple(resultList)
    print(f"Tuple: {resultTuple}")

def no5():
    print("課題5")
    fileName = input("ファイル名を入力してください: ")
    print(f"拡張子は{re.search(r'\.(\w+)', fileName).group(1)}です。")

def no6():
    print("課題6")
    manual = nltk.word_tokenize.__doc__ 
    pattern = r":\w+ .*"
    print(re.findall(pattern, manual))

no6()