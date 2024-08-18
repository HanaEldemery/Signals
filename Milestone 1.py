import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

t=np.linspace(0,3,12*1024)
#12*1024 is the number of samples

leftFreq=np.array([329.63,349.23,196,220,440])
#frequencies for the left notes
rightFreq=np.array([130.81,293.66,146.83,196,220])
#frequencies for the right notes

startTime=np.array([0,0.5,1,1.5,2])
#starting time for each note
interval=np.array([0.5,0.4,0.5,0.4,0.9])
#interval for each note

i=0
#index and counter for the while loop
Pairs=5
#bec i have 5 notes
sumNotes=0
#sum of all notes

while(Pairs>i):
    LF=leftFreq[i]
    #ith left note frequency
    RF=rightFreq[i]
    #ith right note frequency
    ST=startTime[i]
    #ith note starting time 
    I=interval[i]
    #ith note interval
    leftNote=np.sin(2*np.pi*LF*t)
    #ith left note
    rightNote=np.sin(2*np.pi*RF*t)
    #ith right note
    sumNotes=sumNotes+((leftNote+rightNote)*((t>=ST)&(t<=(ST+I))))
    #((t>=ST)&(t<=(ST+I))) represents the unit step
    #𝑥𝑡=෍𝑖=1𝑁[sin2𝜋Ϝ𝑖𝑡+sin2𝜋𝑓𝑖𝑡][𝑢(𝑡−𝑡𝑖)−𝑢(𝑡−𝑡𝑖−𝑇𝑖)]
    i=i+1
    #incrementation
    
plt.plot(t,sumNotes)
#plotting the notes
sd.play(sumNotes,3*1024)
#playing the notes









