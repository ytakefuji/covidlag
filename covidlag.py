import pandas as pd
import numpy as np
import sys
from time import sleep
import matplotlib.pyplot as plt
import subprocess as sp
from sklearn.metrics import r2_score as r2
import matplotlib.patches as mpatches
from scipy import signal

sp.call("wget https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv",shell=True)
sp.call("cat owid-covid-data.csv|sed '2,$s/,-/,/g' >new",shell=True)
sp.call("mv new owid-covid-data.csv",shell=True)
d=pd.read_csv("owid-covid-data.csv")
sp.call("rm owid-covid-data.csv",shell=True)
span=50
class main:
 def main(self,country="Japan",samples=400,degree=7):
   cases=d[d.location==country]['new_cases']
   deaths=d[d.location==country]['new_deaths']
   days=d[d.location==country]['date']
   n=len(days)
   today=str(days[n-1:]).split()[1]
   deaths=deaths[n-samples:n]
   deaths.fillna(0,inplace=True)
   cases=cases[n-samples:n]
   cases.fillna(0,inplace=True)
   days=days[n-samples:n]
   x=np.arange(n-samples,n)
   valid = ~(np.isnan(x) | np.isnan(deaths))
   modeldeath=np.poly1d(np.polyfit(x[valid],deaths[valid],degree))
   valid = ~(np.isnan(x) | np.isnan(cases))
   modelcase=np.poly1d(np.polyfit(x[valid],cases[valid],degree))
   ydeath=modeldeath(x)
   ycase=modelcase(x)
   maxiddeath = signal.argrelmax(ydeath)
   miniddeath = signal.argrelmin(ydeath)
   maxidcase = signal.argrelmax(ycase)
   minidcase = signal.argrelmin(ycase)
   maxdeath=np.array(maxiddeath)
   print('maxima information')
   for i in range(len(maxiddeath[0])):
    j=maxiddeath[0][i]
    print('death peak:',str(days[j:j+1]).split()[1])
   for i in range(len(maxidcase[0])):
    j=maxidcase[0][i]
    print('case peak:',str(days[j:j+1]).split()[1])
   print('maxiddeath',maxiddeath)
   print('maxidcase',maxidcase)
   print('ydeath[maxiddeath]',ydeath[maxiddeath].astype(int))
   print('ycase[maxidcase]',ycase[maxidcase].astype(int))
   print("==================================")
   print('minima information')
   for i in range(len(miniddeath[0])):
    j=miniddeath[0][i]
    print('death minima:',str(days[j:j+1]).split()[1])
   for i in range(len(minidcase[0])):
    j=minidcase[0][i]
    print('case minima:',str(days[j:j+1]).split()[1])
   print('miniddeath',miniddeath)
   print('minidcase',minidcase)
   print('ydeath[miniddeath]',ydeath[miniddeath].astype(int))
   print('ycase[minidcase]',ycase[minidcase].astype(int))
   r2d=round(r2(deaths,ydeath),3)
   r2c=round(r2(cases,ycase),3)
   fig,ax1=plt.subplots()
   ax1.set_xticks(np.arange(n-samples,n,span))
   ax1.set_xticklabels(days[::span],rotation = 15,fontsize=7)
   ax1.set_xlabel('days')
   ax1.set_ylabel('the number of daily cases')
   ax2=ax1.twinx()
   ax1.plot(x,cases,color="black",alpha=0.4)
   ax1.plot(x,ycase,color="blue")
   ax1.plot(x[maxidcase],ycase[maxidcase],'ro')
   ax1.plot(x[minidcase],ycase[minidcase],'bo')
   ax2.set_xlabel('days')
   ax2.set_xticks(np.arange(n-samples,n,span))
   ax2.set_xticklabels(days[::span],rotation = 15,fontsize=7)
   ax2.set_ylabel('the number of daily deaths')
   ax2.plot(x,deaths,color="black",alpha=0.4)
   ax2.plot(x,ydeath,color="red")
   ax2.plot(x[maxiddeath],ydeath[maxiddeath],'ro')
   ax2.plot(x[miniddeath],ydeath[miniddeath],'bo')
   maxdeath=" ".join(str(i) for i in maxiddeath)
   maxcase=" ".join(str(i) for i in maxidcase)
   handles,labels = ax1.get_legend_handles_labels()
   st='daily deaths in '+str(country)+'\n'+str(samples)+' days from '+str(today)+'\n'+str(degree)+'th regression'+' r2death: '+str(r2d)+' '+'r2case: '+str(r2c)+'\n'+'death peaks:'+str(maxdeath)+' '+str(ydeath[maxiddeath].astype(int))+'\n'+'case peaks:'+str(maxcase)+' '+str(ycase[maxidcase].astype(int))
   handles.append(mpatches.Patch(color='none',label=st))
   if LR=='L':
    plt.legend(handles=handles,fontsize=7,loc='upper left')
   elif LR=='R':
    plt.legend(handles=handles,fontsize=7,loc='upper right')
   elif LR=='C':
    plt.legend(handles=handles,fontsize=7,loc='upper center')
   elif LR=='':
    plt.legend(handles=handles,fontsize=7,loc='best')
   plt.savefig(country+".png")
   plt.show()
country=str(sys.argv[1])
samples=int(sys.argv[2])
degree=int(sys.argv[3])
if len(sys.argv)==4:
 LR=''
else: LR=str(sys.argv[4])
m=main()  
m.main(country,samples,degree)
 
