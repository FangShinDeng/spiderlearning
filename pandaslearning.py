import pandas as pd
from pandasgui import show

df = pd.DataFrame({
    "Name": ["Braund, Mr. Owen Harris",
             "Allen, Mr. William Henry",
             "Bonnell, Miss. Elizabeth"],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"]}
)

print(df)

# print(df["Age"])

# show(df)
show(df, settings={'block': True})
