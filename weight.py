import pandas as pd
import plotly.figure_factory as ff 


df = pd.read_csv("data.csv")

data = df["Weight(Pounds)"].tolist()

fig = ff.create_distplot([data],["weight"], show_hist = False)
fig.show();
