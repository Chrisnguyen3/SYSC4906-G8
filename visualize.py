import os

import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime

def plot(file_name):
    keyword = os.path.basename(file_name)
    keyword = keyword[:keyword.find("-")]
    data = []
    with open(file_name, "r") as file:
        for i, line in enumerate(file.readlines()):
            if i == 0: continue

            temp_str = line.split(",")
            date = datetime.strptime(temp_str[1].strip(), "%Y/%m/%d")
            price = float(temp_str[2].strip())

            if date.year < 2021: continue
            if price < 0: continue

            data.append([date, price])

    data = np.array(data, dtype=object)
    data = np.sort(data, axis=0)
    print(data)

    plt.step(data[:, 0], data[:, 1:])
    plt.title(keyword)
    plt.xlabel("Date")
    plt.ylabel("Price (CAD$)")
    plt.savefig(f"figures/{keyword}.png")
    # plt.show()
    plt.clf()

if __name__ == "__main__":
    import tkinter as tk
    from tkinter import filedialog

    # get file of supplies
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilename(
        title="Choose input file", 
        initialdir=os.getcwd() + "/raw_data/",
        initialfile="supplies.txt",
        multiple=True
    )

    for path in file_paths:
        plot(path)
