import pandas as pd
import color_codes as cc
import constants as c
import sys
import os
from datetime import datetime as dt


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


def main():
    args = sys.argv
    if len(args) < 2:
        print("Specify CSV file.")
        exit()

    file_name = os.path.splitext(args[1])[0]
    df = read_df(args[1])
    
    total_scrobbles = len(df.index)
    print(f"Total Scrobbles: {cc.BLUE}{total_scrobbles}{cc.NORMAL}")

    first = first_scrobble(df)
    print(f"First Scrobble: {cc.MAGENTA}{first}{cc.NORMAL}")

    last = last_scrobble(df)
    print(f"Last Scrobble: {cc.MAGENTA}{last}{cc.NORMAL}")


if __name__ == "__main__":
    main()
