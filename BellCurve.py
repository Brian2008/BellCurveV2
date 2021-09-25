import random
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 

diceResult=[]
for i in range (0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceResult.append(dice1+dice2)

mean=sum(diceResult)/len(diceResult)
std_deiviation=statistics.stdev(diceResult)
median=statistics.median(diceResult)
mode=statistics.mode(diceResult)
print(mean)
print(median)
print(mode)
print(std_deiviation)
fig = ff.create_distplot([diceResult],["Result"])
fig.show()

