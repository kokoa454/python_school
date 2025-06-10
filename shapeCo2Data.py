import bs4 as bs
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def getCo2Data():
    url = "https://www.data.jma.go.jp/ghg/kanshi/obs/co2_monthave_ryo.html"

    try:
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
        columns = [row.text for row in rows[0].findAll("td")]
        columns[0] = "西暦"

        df = pd.DataFrame(columns=columns)

        for i in range(1, len(rows)):
            rowContents = [row.text for row in rows[i].findAll("td")]
            rowContents[0] = int(rowContents[0].replace("年", ""))

            for j in range(1, len(rowContents)):            
                if rowContents[j] == "--":
                    rowContents[j] = np.nan
                elif rowContents[j].find("(") != -1 and rowContents[j].find(")") != -1:
                    rowContents[j] = rowContents[j].replace("(", "").replace(")", "")
                    rowContents[j] = float(rowContents[j])
                else:
                    rowContents[j] = float(rowContents[j])
                
            df = pd.concat([df, pd.DataFrame([rowContents], columns=columns)], ignore_index=True)

        print(df)

        return df

    except Exception as e:
        print("pandas error")
        print(e)

# def outputGraph(df):
#     try:
#         df.plot()
#         plt.show()

#     except Exception as e:
#         print("matplotlib error")
#         print(e)

def main():
    rows = getCo2Data()
    df = outputDataFrame(rows)
    # outputGraph(df)

main()