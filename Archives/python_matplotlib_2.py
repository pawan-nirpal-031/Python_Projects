'''
Pawan Nirpal 
TECOC341
'''

import matplotlib.pyplot as plt
import csv
import numpy as np

Country_names=["Aus","Ind","Eng"]
gold_medals=[120,110,90]
silver_medals=[60,70,60]
bronze_medals=[30,40,50]

dataZ=zip(Country_names,gold_medals,silver_medals,bronze_medals)

with open("Game_medal.csv",'w')as file:
    writer=csv.writer(file,lineterminator='\r')
    writer.writerow(("Country_names","gold_medals","silver_medals","bronze_medals"))
    for row in dataZ:
        writer.writerow(row)

with open("Game_medal.csv",'r')as file:
    reader=csv.reader(file)
    next(reader)
    data=[r for r in reader]
    gold_m=[int(i[1]) for i in data]
    silver_m=[int(i[2]) for i in data]
    bronze_m=[int(i[3]) for i in data]
    
n=np.arange(3)

def Plot(gold_m,silver_m,bronze_m):
    plt.bar(n+0.0, gold_m,color='b', width=0.2, label='GOLD MEDALS')
    plt.bar(n+0.2, silver_m,color='#ffa500', width=0.2, label='SILVER MEDALS')
    plt.bar(n+0.4, bronze_m,color='g', width=0.2, label='BRONZE MEDALS')
    plt.xlabel('Nations',fontweight='bold',color='#03A9F4')
    plt.ylabel('Medals',fontweight='bold',color='#03A9F4')
    plt.xticks([r+ 0.2 for r in range(len(gold_m))],['Aus','Ind','Eng'])
    plt.title('Olympics 2018',color='purple',fontweight='bold')
    plt.legend()
    plt.show()

Plot(gold_medals,silver_medals,bronze_medals)