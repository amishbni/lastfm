import pandas as pd
import sys
from collections import Counter

def get_hours(address):
    columns = ["artist", "album", "track", "date"]
    df = pd.read_csv(address, names=columns).dropna(subset=["date"])
    hours = df["date"].apply(lambda x: int(x.split(" ")[3].split(":")[0]))
    count = list(Counter(hours.tolist()).items())
    result = sorted(count, key=lambda tup: tup[0])

    return result

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("Specify CSV file.")
        exit()
    
    hours = get_hours(args[1])
    print(hours)