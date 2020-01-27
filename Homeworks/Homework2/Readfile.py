
# coding: utf-8

# In[4]:

#import necessary libraries
import numpy as np
import astropy.units as u


#function for reading in .txt files
def Read(filename):
    file = open(filename, 'r')     #open/read in file
    line1 = file.readline()       #read in first line of file
    label, value = line1.split()  #split parts of first line into label/value
    time = float(value)*10.0*u.Myr   #value of time in Myr
    
    line2 = file.readline()    #read in second line
    label2, value2 = line2.split()   #split parts of second line into label/value
    total = float(value2)      #total number of particles
    file.close()      #close file
    
    #stores rest of file and creates arrays to store data with labels
    data = np.genfromtxt(filename, dtype = None, names = True, skip_header = 3)
    
    #return desired values
    return time, total, data
    


# In[33]:




