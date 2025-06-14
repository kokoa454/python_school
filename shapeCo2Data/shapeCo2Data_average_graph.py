import bs4 as bs
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import date 
from matplotlib.font_manager import FontProperties

def getCo2Data():
    # 気象庁の綾里のCO2データ
    url = "https://www.data.jma.go.jp/ghg/kanshi/obs/co2_monthave_ryo.html"

    try:
        # htmlを取得後、bsでtableタグ内のtbodyタグを取り出し、trタグをリストとして格納
        html = requests.get(url)
        soup = bs.BeautifulSoup(html.content, "html.parser")
        table = soup.find("table", {"id": "obs_data"}).tbody
        rows = table.findAll("tr")

        return rows
    except Exception as e:
        print("html parsing error")
        print(e)

def outputDataFrame(rows):
    try:
        # 最初のtdタグ行を列名として格納, その際、地名を西暦に置き換え
        columns = [row.text for row in rows[0].findAll("td")]
        placeName = columns[0]
        columns[0] = "西暦"
        
        # 列名データをpandas.DataFrameに格納
        df = pd.DataFrame(columns=columns)

        # 最初の未確定データの年を格納する変数
        firstUnregisteredYear = None

        # 列名以外のデータをpandas.DataFrameに格納
        for i in range(1, len(rows)):
            # 各行のtdタグをリストとして格納
            rowContents = [row.text for row in rows[i].findAll("td")]
            # 西暦列の年を省いてint型に変換
            rowContents[0] = int(rowContents[0].replace("年", ""))

            # リストとして格納されている西暦列以外の行のデータを個別に分解
            for j in range(1, len(rowContents)):     
                # "--"をnp.nanに置き換え       
                if rowContents[j] == "--":
                    rowContents[j] = np.nan
                # "()"を除去してfloat型に変換
                elif rowContents[j].find("(") != -1 and rowContents[j].find(")") != -1:
                    rowContents[j] = rowContents[j].replace("(", "").replace(")", "")
                    rowContents[j] = float(rowContents[j])
                    # 最初の未確定データの年を取得
                    if firstUnregisteredYear is None:
                        firstUnregisteredYear = rowContents[0]
                # 通常数値の場合はfloat型に変換
                else:
                    rowContents[j] = float(rowContents[j])
            
            # 各行のデータをpandas.DataFrameに格納
            # ignore_index=Trueを指定することでindexを自動的に振り直す
            df = pd.concat([df, pd.DataFrame([rowContents], columns=columns)], ignore_index=True)

        print(df)

        return df, placeName

    except Exception as e:
        print("pandas error")
        print(e)

def outputGraph(df, placeName):
    try:
        # matplotlibのフォント設定
        fp = FontProperties(fname=r'C:\WINDOWS\Fonts\meiryob.ttc', size=16)
        # matplotlibのグラフ設定
        lineWidth = 2

        # 各年の合計値、nan個数、平均値が追加されたDataFrame
        averageDf = (df.pipe(calcSum).pipe(calcAverage))

        print(averageDf)

        plt.plot(df["西暦"], averageDf["average"], label="average", color="blue", linewidth=lineWidth)
        plt.title("大気中二酸化炭素濃度(at " + placeName + ")", fontproperties=fp)
        plt.xlabel("year")
        plt.ylabel("CO2 (ppm)")
        plt.legend()
        plt.show()

    except Exception as e:
        print("matplotlib error")
        print(e)

def calcSum(df):
    sum = []
    nan = []
    firstYear = df["西暦"][0]
    lastYear = df["西暦"].iloc[-1]
    
    for y in range(firstYear, lastYear + 1):
        yearSum = 0
        nanCnt = 0
        for m in range(1, 13):
            # nanだった場合の処理
            if pd.isna(df.loc[df["西暦"] == y, f"{m}月"].values[0]):
                nanCnt += 1
            else:
                yearSum += df.loc[df["西暦"] == y, f"{m}月"].values[0]
        nan.append(nanCnt)
        sum.append(yearSum)    
    
    # sumカラムとnanCntカラムを追加
    df["sum"] = sum
    df["nanCnt"] = nan

    return df

def calcAverage(df):
    average = []
    
    firstYear = df["西暦"][0]
    lastYear = df["西暦"].iloc[-1]

    for y in range(firstYear, lastYear + 1):
        # 12(ヶ月)からnan個数を引き、sumで割って平均値を算出
        yearAverage = df.loc[df["西暦"] == y, "sum"].values[0] / (12 - df.loc[df["西暦"] == y, "nanCnt"].values[0])
        average.append(yearAverage)
    
    # averageカラムを追加
    df["average"] = average

    return df

def main():
    rows = getCo2Data()
    df, placeName = outputDataFrame(rows)
    outputGraph(df, placeName)
main()