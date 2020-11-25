from wordcloud_fa import WordCloudFa
import pandas as pd
import arabic_reshaper as ar
import re
import sys
from os import path

args = sys.argv
if len(args) < 2:
	print("Specify CSV file!")
	exit()

csv_address = args[1]
username = path.splitext(csv_address)[0]

columns = ["artist", "album", "track", "date"]
data = pd.read_csv(csv_address, header=None, names=columns)
top_series = data["artist"].value_counts()[:50]
top = dict(zip(top_series.index, top_series))

wordcloud = WordCloudFa(
	prefer_horizontal=1,
	background_color='white',
	width=2048,
	height=2048
).generate_from_frequencies(top)

image = wordcloud.to_image()
image.save(f"{username}.png")
