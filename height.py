import pandas as pd
import plotly.figure_factory as ff 


df = pd.read_csv("data.csv")

data = df["Height(Inches)"].tolist()

fig = ff.create_distplot([data],["height"])
fig.show();







