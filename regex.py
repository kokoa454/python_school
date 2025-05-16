import re

# 指定した文字集合の要素以外の文字を含む文字列 
def printStringWithoutSpecifiedChars():
    print("問1: 指定した文字集合の要素以外の文字を含む文字列")
    print("--------------------------------------------------")
    inputString = input("文字列を入力: ")
    specifiedChars = input("除きたい文字を入力: ")
    pattern = f"[^{specifiedChars}]+"
    matches = re.findall(pattern, inputString)
    if matches:
        print("除きたい文字を含まない文字列: ", *matches)
    else:
        print("除きたい文字を含まない文字列は見つかりませんでした")

# 先頭の文字がaでその後ろに0個あるいは複数のbを持つ文字列 
def printFirstAWithZeroOrMoreB():
    print("問2: 先頭の文字がaでその後ろに0個あるいは複数のbを持つ文字列")
    print("--------------------------------------------------")
    inputString = input("文字列を入力: ")
    pattern = r"^ab*\b"
    matches = re.findall(pattern, inputString)
    if matches:
        print("先頭の文字がaでその後ろに0個あるいは複数のbを持つ文字列です")
    else:
        print("先頭の文字がaでその後ろに0個あるいは複数のbを持つ文字列ではありません")
    
# aの後ろに0個あるいは複数のbが続く文字列  
def AWithZeroOrMoreB():
    print("問3: aの後ろに0個あるいは複数のbが続く文字列")
    print("--------------------------------------------------")
    inputString = input("文字列を入力: ")
    pattern = r"\bab*\b"
    matches = re.findall(pattern, inputString)
    if matches:
        print("aの後ろに0個あるいは複数のbが続く文字列です")
    else:
        print("aの後ろに0個あるいは複数のbが続く文字列ではありません")

# aの後ろに3つのbが続く文字列 
def printAWithThreeB():
    print("問4: aの後ろに3つのbが続く文字列")
    print("--------------------------------------------------")
    inputString = input("文字列を入力: ")
    pattern = r"\bab{3}\b"
    matches = re.findall(pattern, inputString)
    if matches:
        print("aの後ろに3つのbが続く文字列です")
    else:
        print("aの後ろに3つのbが続く文字列ではありません")

# aの後ろに2つ、3つ、あるいは4つのbが続く文字列 
def printAWithTwoThreeOrFourB():
    print("問5: aの後ろに2つ、3つ、あるいは4つのbが続く文字列")
    print("--------------------------------------------------")
    inputString = input("文字列を入力: ")
    pattern = r"\bab{2,4}\b"
    matches = re.findall(pattern, inputString)
    if matches:
        print("aの後ろに2つ、3つ、あるいは4つのbが続く文字列です")
    else:
        print("aの後ろに2つ、3つ、あるいは4つのbが続く文字列ではありません")

# 小文字からなる文字数が４の英語の文字列２つをアンダースコア「_」で結合している文字列 
def printTwoStringsWithUnderscore():
    print("問6: 小文字からなる文字数が4の英語の文字列2つをアンダースコア「_」で結合している文字列")
    print("--------------------------------------------------")
    inputString = input("文字列を入力: ")
    pattern = r"\b[a-z]{4}_[a-z]{4}\b"
    matches = re.findall(pattern, inputString)
    if matches:
        print("小文字からなる文字数が4の英語の文字列2つをアンダースコア「_」で結合している文字列です")
    else:
        print("小文字からなる文字数が4の英語の文字列2つをアンダースコア「_」で結合している文字列ではありません")

# 文字aに続き最後の文字がbで終わる英語文字列 
def printAWithBAtEnd():
    print("問7: 文字aに続き最後の文字がbで終わる英語文字列")
    print("--------------------------------------------------")
    inputString = input("文字列を入力: ")
    pattern = r"\ba\w*\W*b$"
    matches = re.findall(pattern, inputString)
    if matches:
        print("文字aに続き最後の文字がbで終わる英語文字列です")
    else:
        print("文字aに続き最後の文字がbで終わる英語文字列ではありません")

def main():
    printStringWithoutSpecifiedChars()
    print("\n")
    printFirstAWithZeroOrMoreB()
    print("\n")
    AWithZeroOrMoreB()
    print("\n")
    printAWithThreeB()
    print("\n")
    printAWithTwoThreeOrFourB()
    print("\n")
    printTwoStringsWithUnderscore()
    print("\n")
    printAWithBAtEnd()
    
main()