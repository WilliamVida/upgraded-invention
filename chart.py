# import pandas as pd
# import plotly.express as px

# df = pd.read_csv("./statistics/all states/All States Abortion Rate and Presidential Election Results.csv")

# fig = px.scatter(df, y=df["Abortion Rate (Guttmacher)"],
#                  x=df["Democratic Vote"] - df["Republican Vote"],
#                  animation_frame="Year",
#                  animation_group="State",
#                  color=df["Democratic Vote"] - df["Republican Vote"],
#                  range_color=[-100, 100],
#                  color_continuous_scale=[(0.00, "red"),   (0.45, "red"),
#                                          (0.45, "orange"), (0.49, "orange"),
#                                          (0.51, "green"), (0.55, "green"),
#                                          (0.55, "blue"),  (1.00, "blue")],
#                  hover_name="State",
#                  range_y=[0, 40],
#                  range_x=[-50, 50],
#                  text="State",
#                  trendline="ols",
#                  # size=df["Abortion Rate (Guttmacher)"],
#                  )

# fig.update_traces(textposition="top center",
#                   )
# fig.update_layout(
#     title="State Abortion Rate and State Presidential Margin",
#     xaxis_title="<--- Greater R Margin     Greater D Margin --->",
#     showlegend=True,
#     coloraxis_showscale=False,
#     # coloraxis_colorbar=dict(
#     # title="Margin",
#     # ),
#     # coloraxis=dict(colorbar=dict(orientation="h")),
# )
# fig.update_yaxes(nticks=10)
# fig.update_xaxes(nticks=20)
# fig["layout"].pop("updatemenus")  # optional, drop animation buttons
# fig.show()
