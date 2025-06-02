import csv

headList = []
co2List = []

try:
    with open('./co2_monthave_ryo.csv', mode='r') as inputFile:
        reader = csv.reader(inputFile)
        
        try:
            with open('./co2_monthave_ryo_shaped.csv', mode='w') as outputFile:
                writer = csv.writer(outputFile)
                isTitle = True

                for row in reader:
                    if isTitle == True:
                        title = row[2]
                        headList.append(row[0])
                        headList += ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
                        writer.writerow(''.join(title).split(','))
                        writer.writerow(headList)
                        isTitle = False

                    else:
                        if row[0] not in co2List:
                            if len(co2List) != 0:
                                writer.writerow(co2List)
                                co2List = []
                            co2List.append(row[0])
                            co2List += [''] * 12
                        co2List[int(row[1])] = row[2]

        except Exception as outputFileError:
            print("outputFileError: ", str(outputFileError))

except Exception as inputFileError:
    print("inputFileError: ", str(inputFileError))

#    年     1月     2月     3月    4月  ...  8月     9月    10月    11月    12月 
# 0  1987  353.3  354.1  354.9  356.6  ...  345.7  344.9  350.1  352.9  354.7 
# 1  1988  356.1  357.0  357.7  358.7  ...  348.7  348.6  354.3  356.7  357.3 
# 2  1989  358.4  359.6  359.6  360.6  ...  348.2  351.5  355.0  357.8  358.6 
# 3  1990  360.1  360.8  362.0  361.8  ...  350.6  351.9  355.1  358.3  359.0 
# 4  1991  361.2  362.2  363.5  363.7  ...  351.3  351.5  356.6  359.1  361.3 

# 年,月,二酸化炭素濃度の月平均値(綾里)[ppm],
# 1987, 1,353.3,
# 1987, 2,354.1,
# 1987, 3,354.9,
# 1987, 4,356.6,
# 1987, 5,354.8,