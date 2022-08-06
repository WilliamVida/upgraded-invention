import os
import pandas as pd
import plotly.express as px

d = {}
folder='./statistics/'
states_data = os.listdir(folder)
print(states_data)
i=0
for state in states_data:
    # if file.endswith(".csv"):
    # print(state[:-4])
    d["df{0}".format(state[:-4])] = pd.read_csv(folder+state)
    i=i+1



# df.iloc[:, 0]
fig = px.line()

#x = df, y=table
for x ,y in d.items():
    fig.add_scatter(x=d[x]["Year"], y=d[x]["Abortion rate (Guttmacher)"]
    ,hovertemplate="<b>"+x[2:]+"</b><br>Year: %{x}<br>Abortion rate: %{y}"
    ,
    name=x[2:]
    )
    # print()

    # print(d[x]["Year"])
    # print(x, y)

# fig.add_scatter(x=df["Year"], y=df["Abortion rate (Guttmacher)"],
#                     )
# fig.add_scatter(x=df2["Year"], y=df2["Abortion rate (Guttmacher)"],
# )
# fig.add_scatter(x=df3["Year"], y=df3["Abortion rate (Guttmacher)"],
# )

# customdata = np.stack((df['continent'], df['country']), axis=-1)

fig.update_traces(mode="markers+lines", 
                #   hovertemplate="<b>"+x[2:]+"</b><br>Year: %{x}<br>Abortion rate: %{y}",
                  )
fig.update_layout(title="Abortion rate by state (Guttmacher)",
    xaxis_title="Year",
    yaxis_title="Abortion rate",
    autotypenumbers="convert types",    legend_title="State", 
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    )
    )
fig.show()
