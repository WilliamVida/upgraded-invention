import os
import pandas as pd
import plotly.express as px

os.chdir("./statistics/all states")
folder = "./statistics/all states"
file = "All States Abortion Rate.csv"
df = pd.read_csv(file)
df.set_index("State")

fig = px.line(df, title="Abortion Rate by State (Guttmacher)", x="Year",
              y="Abortion rate (Guttmacher)", color="State", text=df["State"])

fig.update_yaxes(rangemode="tozero")
fig.update_traces(mode="markers+lines+text", textposition="middle right",
                  marker=dict(size=8, line=dict(
                      width=1,
                      color="DarkSlateGrey")),
                hovertemplate="<b>%{text}</b><br>Abortion Rate: %{y}<br>Year: %{x}<br><extra></extra>",   
                  )
fig.update_layout(autotypenumbers="convert types", legend_title="State",
                  hoverlabel=dict(
                      bgcolor="white",
                      font_size=16,
                      font_family="Rockwell"
                  )
                  )
fig.show()
