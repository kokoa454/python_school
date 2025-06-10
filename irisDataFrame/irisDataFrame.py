import pandas as pd 
from sklearn import datasets 

iris = datasets.load_iris() 

df = pd.DataFrame(iris.data, columns=iris.feature_names) 

try:
    with open("irisC24036.csv", "w") as f:
        df.describe().to_csv(f) 
except Exception as e:
    print("csv error")
    print(e)

# 問1 sepal length(cm), sepal width(cm), petal length(cm), petal width(cm)
# 問2 600個
