import csv
import plotly.express as px
import numpy as np

data = open("Student Marks vs Days Present.csv")
df = csv.DictReader(data)
p = px.scatter(df, x="Days Present", y="Marks In Percentage")
p.show()

def fetch_data_source(data_path):
    Days_Present = []
    Percentage = []

    with open(data_path) as f:
        data = csv.DictReader(f)
        for i in data:
            Days_Present.append(float(i["Days Present"]))
            Percentage.append(float(i["Marks In Percentage"]))

        return {"x": Days_Present, "y": Percentage}


def correlation(dataSource):
    correlation_data = np.corrcoef(dataSource["x"], dataSource["y"])
    print(correlation_data[0, 1])


def setup():
    data_path = "Student Marks vs Days Present.csv"
    data_source = fetch_data_source(data_path)
    correlation(data_source)

setup()
