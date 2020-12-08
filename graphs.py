import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys


def plot_graphs(filename):
    f = open(filename, "r")
    play_time = []
    buffered_playback_time = []
    available_playback_time = []
    for x in f:
        values = x.split("#")
        play_time.append(round(float(values[1]), 2))
        buffered_playback_time.append(round(float(values[2]), 2))
        available_playback_time.append(round(float(values[3]), 2))

    plt.plot(play_time, available_playback_time,label="available playback time")
    # sns.lineplot(play_time, available_playback_time, label="available playback time")
    plt.plot(play_time, buffered_playback_time, label="buffered playback time")
    plt.legend(loc="upper left")
    plt.xlabel("Video play time in seconds")
    plt.ylabel("Time in seconds")
    plt.title("100 kbps throughput")
    plt.ylim(0,100)
    plt.show()



def main():
    filename =  sys.argv[1]
    plot_graphs(filename)



if __name__ == '__main__':
	main()