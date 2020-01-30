# Importing packages
import plotly.express as px
import pandas as pd

# Importing dataset
df = pd.read_csv("~/Desktop/rstat/final.csv")

# Plotting figure
fig = px.bar(df, x="Province/State", y="Confirmed",
  animation_frame="Date last updated", animation_group= "Province/State", range_y=[0,4000])

# Adding legends and axis label
fig.update_layout(title='Number of Confirmed cases from 24 Jan 2020 to 28 Jan 2020')


fig.show()




