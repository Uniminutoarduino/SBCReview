#Script of Publications per year
#Script designed in Python (V3.8)
#Please see the included packages and install them before to run the script

import operator
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#This block is used to plot the publications by years,
dest=open('YearsPublications.txt','r') #File with years by article.
message=dest.readlines()
dest.close()
c=0
d=0
print (message)
print (type(message))
#print (type(message))
wordlist = message
dictionary={}
wordfreq = []
for w in wordlist:
    dictionary[w]=wordlist.count(w)
    wordfreq.append(wordlist.count(w))

#Organize the frecuency of the years in the publications
print("List\n" + str(wordlist) + "\n") #Print years and frecuencies in these ones.
print("Frequencies\n" + str(wordfreq) +str(wordlist)+ "\n")
sorted_d = sorted(dictionary.items(), key=operator.itemgetter(0))#Option (0) is year
print (sorted_d)
listaMatplot=[]
ListaPaises=[]
counter=0
#Cluster the number of publications in each year
for x in range(0,len(sorted_d)):
    ListaPaises.append(sorted_d[x][0])
    listaMatplot.append(sorted_d[x][1])
    print((sorted_d[x][0]))
    print((sorted_d[x][1]))
    counter=counter+1
suma=0
print(ListaPaises[2])
print(listaMatplot[1])
for x, y in dictionary.items():
  suma=suma+int(y)

#Create the plot for the publications pers year
fig, ax = plt.subplots()
objects = ListaPaises
y_pos = np.arange(len(objects))
performance = listaMatplot

u=plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects, rotation='vertical', fontsize=10)
plt.xlabel('Year') #Label of X-axis
u[8].set_color('g')#Color for the final year (2020)
rects = ax.patches
labels=performance
#Put the number of the articles per year in the middle of the rectangle box.
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 0.2, label,
            ha='center', va='bottom')
plt.show()
plt.savefig("Years.pdf") #Save image in .pdf
