import matplotlib.pyplot as plt
import csv
import numpy as np
import matplotlib.lines as mlines
from matplotlib.legend_handler import HandlerLine2D
import statistics


def thousands(x):
    x2 = [i / 1000 for i in x]
    return x2


def main():
    with open('rsel.csv', newline='') as csvfile:
        rsel = csv.reader(csvfile, delimiter=',')
        next(rsel)
        rselData = []
        effort = []
        for row in rsel:
            sum = 0
            rselLast = []
            i = True
            for cell in row[1:]:
                if i:
                    effort.append(float(cell));
                    i = False;
                else:
                    sum += float(cell)
                    rselLast.append(100*float(cell));
            rselData.append(100 * sum / len(row))
        print(rselData)
        # del rselLast[:2]
        # map(float,rselLast)
        print(effort)
        print(rselLast)

    with open('cel.csv', newline='') as csvfile:
        cel = csv.reader(csvfile, delimiter=',')
        next(cel)
        celData = []
        for row in cel:
            celLast = []
            sum = 0
            for cell in row[2:]:
                sum += float(cell)
                celLast.append(100 * float(cell));
            celData.append(100 * sum / len(row))

    with open('cel-rs.csv', newline='') as csvfile:
        celrs = csv.reader(csvfile, delimiter=',')
        next(celrs)
        celrsData = []
        for row in celrs:
            celrsLast = []
            sum = 0
            for cell in row[2:]:
                sum += float(cell)
                celrsLast.append(100 * float(cell));
            celrsData.append(100 * sum / len(row))

    with open('2cel.csv', newline='') as csvfile:
        twoCel = csv.reader(csvfile, delimiter=',')
        next(twoCel)
        twoCelData = []
        for row in twoCel:
            twoCelLast = []
            sum = 0
            for cell in row[2:]:
                sum += float(cell)
                twoCelLast.append(100 * float(cell));
            twoCelData.append(100 * sum / len(row))

    with open('2cel-rs.csv', newline='') as csvfile:
        twoCelrs = csv.reader(csvfile, delimiter=',')
        next(twoCelrs)
        twoCelrsData = []
        for row in twoCelrs:
            twoCelrsLast=[]
            sum = 0
            for cell in row[2:]:
                sum += float(cell)
                twoCelrsLast.append(100 * float(cell));
            twoCelrsData.append(100 * sum / len(row))

#first plot

    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(1, 2, 1)
    ax1 = ax.twiny()

    effort = thousands(effort)

    ax.plot(effort, rselData, label='1-Evol-RS', color='b', marker='o', markeredgecolor='black', markevery=25,
            markersize=10)
    ax.plot(effort, celrsData, label='1-Coev-RS', color='g', marker='v', markeredgecolor='black', markevery=25,
            markersize=10)
    ax.plot(effort, twoCelrsData, label='2_coev-RS', color='r', marker='D', markeredgecolor='black', markevery=25,
            markersize=10)
    ax.plot(effort, celData, label='1-Coev', color='black', marker='s', markeredgecolor='black', markevery=25,
            markersize=10)
    ax.plot(effort, twoCelData, label='2-Coev', color='m', marker='d', markeredgecolor='black', markevery=25,
            markersize=10)
    ax.legend(bbox_to_anchor=(0.95, 0.15), numpoints=2)
    ax.set_xlim(0, 500)
    ax.set_ylim(60, 100)
    ax.yaxis.grid(linestyle='--')  #
    ax.xaxis.grid(linestyle='--')  #
    ax.tick_params('both', direction='in')
    ax1.tick_params('both', direction='in')
    ax.yaxis.set_ticks_position('both')
    ax.set(xlabel="Rozegranych gier (x1000)", ylabel="Odsetek wygranych gier [%]")
    ax.yaxis.label.set_size(17)
    ax.xaxis.label.set_size(17)
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)
    ax1.set_xticks([0, 40, 80, 120, 160, 200])

#boxplot

    boxplot = fig.add_subplot(1,2,2)
    data=[]
    data.extend([rselLast,celrsLast,twoCelrsLast,celLast,twoCelLast])

    fliersP = dict(markersize=15, linewidth=5, markeredgecolor='b', markerfacecolor='b')
    meanpointsP = dict(marker='o', markeredgecolor='black',markeredgewidth='2', markerfacecolor='b',markersize=10)
    whiskersP = dict(linestyle='--', dashes=(5, 5), linewidth=2, color='g')
    medianP = dict(linestyle='-', linewidth=2.5, color='red')
    boxP = dict(linewidth=2.5,color='b')
    boxplot.boxplot(data,1,'b+',boxprops=boxP,whiskerprops=whiskersP,flierprops=fliersP,meanprops=meanpointsP,medianprops=medianP,vert=True,
                    showmeans=True, whis=1.5)
    boxplot.set_xticklabels(labels=['1-Evol-RS', '1-Coev-RS', '2-Coev-RS', '1-Coev', '2-Coev'], rotation=20)
    boxplot.set_ylim(60,100)
    boxplot.tick_params('both', direction='in')
    boxplot.xaxis.set_ticks_position('both')
    boxplot.yaxis.grid(linestyle='--')  #
    boxplot.xaxis.grid(linestyle='--')  #
    boxplot.tick_params(axis='x', labelsize=15)
    boxplot.tick_params(axis='y', labelsize=15)
    boxplot.yaxis.tick_right()












    plt.show()

    ax1.set_xlabel('Pokolenie')
    ax1.set_xticklabels([0, 40, 120, 160, 200])
    plt.show()


main()
