import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

counted_colors_dict = data['Primary Fur Color'].value_counts(dropna=False).to_dict()

colors_values = data['Primary Fur Color'].unique()
colors_strings = []
counted_colors = []

for color in colors_values:
    colors_strings.append(str(color))
    counted_colors.append(counted_colors_dict[color])

data_dict = {
    "Fur color": colors_strings,
    "Count": counted_colors
}

pd.DataFrame(data_dict).to_csv("fur_colors.csv")
