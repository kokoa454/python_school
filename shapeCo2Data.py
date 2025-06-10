import bs4 as bs
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import date 

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
        columns[0] = "西暦"

        # 列名データをpandas.DataFrameに格納
        df = pd.DataFrame(columns=columns)

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
                # 通常数値の場合はfloat型に変換
                else:
                    rowContents[j] = float(rowContents[j])
            
            # 各行のデータをpandas.DataFrameに格納
            # ignore_index=Trueを指定することでindexを自動的に振り直す
            df = pd.concat([df, pd.DataFrame([rowContents], columns=columns)], ignore_index=True)

        print(df)

        return df

    except Exception as e:
        print("pandas error")
        print(e)

def outputGraph(df):
    try:
        # 初年度と最終年度をDataFrameから取得
        firstYear = df["西暦"][0] 
        lastYear = df["西暦"].iloc[-1] 
        # 月を年・月・1日として日付型に変換
        measuredMonth = [date(y, m, 1) for y in range(firstYear, lastYear + 1) for m in range(1, 13)]
        # 各月のCO2データをリストとして格納
        # 例: df.loc[df["西暦"] == 2010, "1月"], その際、df[f"{m}月"]だとm月列すべてのデータを取得してしまうため間違い
        measuredData = [df.loc[df["西暦"] == y, f"{m}月"] for y in range(firstYear, lastYear + 1) for m in range(1, 13)]

        # matplotlibを使ってグラフを描画
        plt.plot(measuredMonth, measuredData)
        plt.show()


    except Exception as e:
        print("matplotlib error")
        print(e)

def main():
    rows = getCo2Data()
    df = outputDataFrame(rows)
    outputGraph(df)

main()