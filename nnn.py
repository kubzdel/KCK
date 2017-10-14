import matplotlib.pyplot as plt
import csv
import numpy as np
import statistics
with open('rsel.csv',newline='') as csvfile:
    rsel = csv.reader(csvfile,delimiter =',')
    next(rsel)
    rselData=[]
    rselLast=[]
    for row in rsel:
        sum = 0
        rselLast=[]
        rselLast.clear();
        for cell in row[2:]:
            sum+=float(cell)
            rselLast.append(float(cell));
        rselData.append(sum/len(row))
    print(rselData)
    # del rselLast[:2]
    # map(float,rselLast)
    print(rselLast)

with open('cel.csv',newline='') as csvfile:
    cel = csv.reader(csvfile,delimiter =',')
    next(cel)
    celData=[]
    for row in cel:
        sum=0
        for cell in row[2:]:
            sum+=float(cell)
        celData.append(sum/len(row))


with open('cel-rs.csv',newline='') as csvfile:
    celrs = csv.reader(csvfile,delimiter =',')
    next(celrs)
    celrsData=[]
    for row in celrs:
        sum=0
        for cell in row[2:]:
            sum+=float(cell)
        celrsData.append(sum/len(row))

with open('2cel.csv',newline='') as csvfile:
    twoCel = csv.reader(csvfile,delimiter =',')
    next(twoCel)
    twoCelData=[]
    for row in twoCel:
        sum=0
        for cell in row[2:]:
            sum+=float(cell)
        twoCelData.append(sum/len(row))

with open('2cel-rs.csv',newline='') as csvfile:
    twoCelrs = csv.reader(csvfile,delimiter =',')
    next(twoCelrs)
    twoCelrsData=[]
    for row in twoCelrs:
        sum=0
        for cell in row[2:]:
            sum+=float(cell)
        twoCelrsData.append(sum/len(row))



t1 = np.arange(0.0, 500000, 100)
plt.plot(rselData,'bo',markevery=28)
plt.show()