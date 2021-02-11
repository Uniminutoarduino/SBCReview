#Before run the script, check the packages imported
#DOIs must be allocated in the file DOIs.txt
#This script extracts the number of citations per article.

import urllib3
import codecs
import json
import time
import operator
countpapers=0 #Variable to count papers
#Block to open DOIs
f=open('DOIs.txt','r') #Abrir archivo DOI.txt en caso contrario crear archivo con DOI
DOIS=f.readlines()
f.close()
#Block for CrossRef Query
http = urllib3.PoolManager()
dest = codecs.open('CitedPublications.txt',"w") #txt file with Citations with each paper
#This file will be used in order to plot the information

dictionaryFinal={} #Dictionary to allocate cites and titles.

for p in DOIS:
    try:
        countpapers=countpapers+1
        r = http.request('GET', 'https://api.crossref.org/works/'+p)
        data= json.loads(r.data.decode('utf-8'))
        print (str(countpapers)+":"+str(data))
        Cites = (data['message']['is-referenced-by-count']) #Get Data for cites. Data are encoding in UTF-8 through JSON
        print (Cites) #Print cites
        Title=(data['message']['title'])#Get Title
        dictionaryFinal[str(Title)] = int(Cites) #Create dictionary with cites and title for each article
        dest.write(str(Cites))
        dest.write("\n")
        time.sleep(10) #Ten seconds between requests
    except:
        time.sleep(10)  # Ten seconds between requests
        print("Error") #In this case only printing an error

dest.close() #Close File of publications by years

#block to sort the cites. Cites are sorted from major to minor
sorted_d = sorted(dictionaryFinal.items(), key=operator.itemgetter(1), reverse=True)
k=0
f=open('CitedPublications.txt','w+', encoding='utf-8') #Open file .txt with citations
print (type(sorted_d))
for w in sorted_d: #Data are saved in order in a txt file (CitedPublications.txt)
    s=str(sorted_d[k][0])
    s=s+':'
    s=s+str(sorted_d[k][1])
    k = k + 1
    f.write(s)
    f.write('\n')
    print(k,'-',w)

f.close()

