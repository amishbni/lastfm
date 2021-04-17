import pandas as pd
import color_codes as cc
import constants as c
import sys
from datetime import datetime as dt
from collections import Counter


def read_df(address):
    columns = ["artist", "album", "track", "date"]
    df = pd.read_csv(address, names=columns).dropna(subset=["date"])
    df["date"] = pd.to_datetime(
        df["date"],
        format=c.LASTFM_DATETIME_FORMAT
    )
    return df


def first_scrobble(df):
    minimum = df["date"].min()
    date = minimum.strftime(c.STANDARD_DATETIME_FORMAT)

    return date


def last_scrobble(df):
    maximum = df["date"].max()
    date = maximum.strftime(c.STANDARD_DATETIME_FORMAT)

    return date


def scrobble_days(df):
    days = df["date"].apply(lambda x: x.strftime("%Y-%m-%d"))
    unique_days = set(days.tolist())

    return len(unique_days)


def most_scrobbles_in_a_day(df):
    days = df["date"].apply(lambda x: x.strftime("%B %d, %Y"))
    unique_days = Counter(days).most_common(1)
    date = unique_days[0][0]
    count = unique_days[0][1]

    return (count, date)


def main():
    args = sys.argv
    if len(args) < 2:
        print("Specify CSV file.")
        exit()

    df = read_df(args[1])

    total_scrobbles = len(df.index)
    print(f"Total scrobbles: {cc.BLUE}{total_scrobbles}{cc.NORMAL}")

    first = first_scrobble(df)
    print(f"First scrobble: {cc.MAGENTA}{first}{cc.NORMAL}")

    last = last_scrobble(df)
    print(f"Last scrobble: {cc.MAGENTA}{last}{cc.NORMAL}")

    days = scrobble_days(df)
    print(f"Days with at least one scrobble: {cc.BLUE}{days}{cc.NORMAL}")

    top_day = most_scrobbles_in_a_day(df)
    most_scrobbles_text = (
        "Most scrobbles in a day: "
        f"{cc.BLUE}{top_day[0]}{cc.NORMAL}"
        " on "
        f"{cc.MAGENTA}{top_day[1]}{cc.NORMAL}"
    )
    print(most_scrobbles_text)


if __name__ == "__main__":
    main()
