import pandas as pd
import sys
import os


def read_df(address):
    columns = ["artist", "album", "track", "date"]
    df = pd.read_csv(address, names=columns).dropna(subset=["date"])
    return df


def main():
    args = sys.argv
    if len(args) < 2:
        print("Specify CSV file.")
        exit()

    file_name = os.path.splitext(args[1])[0]
    df = read_df(args[1])
    
    total_scrobbles = len(df.index)
    print(f"Total Scrobbles: {total_scrobbles}")


if __name__ == "__main__":
    main()
