from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os


def get_hours(address):
    columns = ["artist", "album", "track", "date"]
    df = pd.read_csv(address, names=columns).dropna(subset=["date"])
    hours = df["date"].apply(lambda x: int(x.split(" ")[3].split(":")[0]))
    count = list(Counter(hours.tolist()).items())
    result = sorted(count, key=lambda tup: tup[0])

    return result


def plot(hours, filename):
    x, y = zip(*hours)

    plt.figure()
    plt.plot(list(x), list(y))
    plt.xticks(list(range(24)))

    plt.title(f"lastfm's scrobbles (@{filename})")
    plt.xlabel("Hour of day")
    plt.ylabel("Number of scrobbles")
    plt.savefig(filename, dpi=120)


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("Specify CSV file.")
        exit()

    filename = os.path.splitext(args[1])[0]
    
    hours = get_hours(args[1])
    plot(hours, filename)