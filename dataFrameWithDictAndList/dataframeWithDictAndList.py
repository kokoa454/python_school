import pandas as pd

def outputDf_fromDict(dict):
    df = pd.DataFrame(dict, columns=dict.keys())
    print("df = pd.DataFrame(dict, columns=dict.keys())")
    print(df)

def outputDf_fromList(list, columns):
    df = pd.DataFrame(list, columns=columns)
    print("df = pd.DataFrame(list, columns=columns)")
    print(df)

def main():
    columns = ["A", "B", "C", "y"]

    dict = {"A": [0.05, 0.32, 0.76, 0.81], 
            "B": [0.31, 0.41, 0.61, 0.94], 
            "C": [0.51, 0.88, 0.48, 0.85], 
            "y": [0.97, 0.89, 0.11, 0.19]
            }
    
    list = [
            [0.05, 0.31, 0.51, 0.97],
            [0.32, 0.41, 0.88, 0.89], 
            [0.76, 0.61, 0.48, 0.11], 
            [0.81, 0.94, 0.85, 0.19]
            ]

    outputDf_fromDict(dict)
    outputDf_fromList(list, columns)


main()
