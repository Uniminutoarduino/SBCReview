#This file extract the publication year in each study. The years are saved in the file YearsPublications.txt.
# Script created in Python V3.8
import urllib3
import codecs
import json
import time
countpapers=0 #Variable to count papers
#Block to open DOIs
f=open('DOIs.txt','r') #Abrir archivo DOI.txt en caso contrario crear archivo con DOI
DOIS=f.readlines()
f.close()
#Block for CrossRef Query
http = urllib3.PoolManager()
dest = codecs.open('YearsPublications.txt',"w") #txt file with years
#This file will be used in order to plot the information

for p in DOIS:
    try:
        countpapers=countpapers+1
        r = http.request('GET', 'https://api.crossref.org/works/'+p)
        data= json.loads(r.data.decode('utf-8'))
        print (str(countpapers)+":"+str(data))
        D = (data['message']['published-print'])  #Get Data for years. Data are encoding in UTF through JSON
        Year=D['date-parts'][0]
        dest.write(str(Year[0]))
        dest.write("\n")
        print (Year[0])
        time.sleep(10) #Ten seconds between requests
    except:
        time.sleep(10)  # Ten seconds between requests
        dest.write("Error")
        print("Error")
        dest.write("\n")

dest.close() #Close File of publications by years
