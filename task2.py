import locale
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import re
from matplotlib.dates import DayLocator, DateFormatter

path = "/Users/varungandhi/Downloads/assignment2_2122/BabyRecords.csv"
locale.setlocale(locale.LC_ALL, "hu_HU")


def main():

    baby = pd.read_csv(path)
    pump = baby[baby["RecordCategory"] == "Pumping"]
    feed = baby[baby["RecordCategory"] == "Feeding"]
    pump.reset_index(inplace=True)
    feed.reset_index(inplace=True)

    bii = [
        re.sub(r"szept", "sze", pump["StartDate"][i])
        for i in range(len(pump["StartDate"]))
    ]
    aii = [
        datetime.datetime.strptime(bii[i], "%d-%b.-%Y %H:%M")
        for i in range(len(pump["StartDate"]))
    ]

    cii = [
        re.sub(r"szept", "sze", feed["StartDate"][i])
        for i in range(len(feed["StartDate"]))
    ]
    dii = [
        datetime.datetime.strptime(cii[i], "%d-%b.-%Y %H:%M")
        for i in range(len(feed["StartDate"]))
    ]

    pump["aii"] = aii
    pump["aii"] = pd.to_datetime(pump["aii"])
    feed["dii"] = dii
    feed["dii"] = pd.to_datetime(feed["dii"])

    numbers = []
    for i in range(len(pump["Details"])):
        if type(pump["Details"][i]) == str:
            obj = re.findall(r"\d+ml", pump["Details"][i])
            if obj != []:
                obj[0] = int(obj[0][:-2])
                numbers.append(obj[0])
            else:
                numbers.append(float("NAN"))
        else:
            numbers.append(float("NaN"))

    numbers2 = []

    for i in range(len(feed["Details"])):
        if type(feed["Details"][i]) == str:
            objc = re.findall(r"\d+ml", feed["Details"][i])
            if objc != []:
                objc[0] = int(objc[0][:-2])
                numbers2.append(objc[0])
            else:
                numbers2.append(float("NAN"))
        else:
            numbers2.append(float("NaN"))

    pump["numbers"] = numbers
    feed["numbers"] = numbers2
    pump = pump[["numbers", "aii"]].sort_values(by=["aii"], ascending=True)
    feed = feed[["numbers", "dii"]].sort_values(by=["dii"], ascending=True)
    feed.reset_index(inplace=True)
    pump.reset_index(inplace=True)

    x = pump.resample("1D", on="aii", closed="right").sum()
    x["date"] = x.index
    x.reset_index(inplace=True)
    x["ma"] = x["numbers"].rolling(window=7).mean()

    y = feed.resample("1D", on="dii", closed="right").sum()
    y["date"] = y.index
    y.reset_index(inplace=True)
    y["ma"] = y["numbers"].rolling(window=7).mean()

    x.rename(
        columns={
            "index": "index_x",
            "numbers": "numbers_x",
            "date": "date_x",
            "ma": "ma_x",
        },
        inplace=True,
    )
    y.rename(
        columns={
            "index": "index_y",
            "numbers": "numbers_y",
            "date": "date_y",
            "ma": "ma_y",
        },
        inplace=True,
    )

    x.set_index(x["aii"], inplace=True)
    y.set_index(y["dii"], inplace=True)

    x_y = pd.concat([x, y], axis=1)
    x_y = x_y[(x_y["date_x"] >= "2021-09-09") & (x_y["date_x"] <= "2021-12-01")]
    x_y["ratio"] = x_y["ma_x"] / x_y["ma_y"]

    fig, (ax1, ax2) = plt.subplots(1, 2)
    plt.rcParams["figure.figsize"] = (25, 10)
    ax1.plot(x.date_x, x.ma_x, label="pump")
    ax1.plot(y.date_y, y.ma_y, label="feed")
    # ax.xaxis.set_major_locator(DayLocator())
    ax1.xaxis.set_major_formatter(DateFormatter("%m-%d"))
    ax1.legend(loc="upper left", prop={"size": 15}, ncol=1)
    ax1.set_xlabel("Date", fontsize=15)
    ax1.set_ylabel("ml", fontsize=15)
    ax1.tick_params(axis="both", which="major", labelsize=15)
    ax1.set_title("pumping and feeding", fontdict={"fontsize": 20})

    ax2.plot(x_y.date_x, x_y.ratio, color="red")
    ax2.xaxis.set_major_formatter(DateFormatter("%m-%d"))
    ax2.set_xlabel("Date", fontsize=15)
    ax2.tick_params(axis="both", which="major", labelsize=15)
    ax2.set_title("ratio of pump and feed", fontdict={"fontsize": 20})
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

