
# coding: utf-8
# Before running the program make sure you have pandas and datetime and xlrd packages installed on your Python3.
# You can put the python file inside your main program folder and use the import command to import it in your program and use it.
# 
#         from timkruz import next_bus
# 		  next_bus()
# Or
#		  next_bus('Village')
# Or
#		  next_bus('Emerald',datetime.time(23,50,0)) # Emerald station at 23:50:00.





# First, We import two very useful modules. 
# 
# Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
# 
# datetime is the second module that is very powerful for manipulating time and dates.
# 

# In[37]:

import pandas as pd
import datetime


# Next, we read all your data into a dataframe. A dataframe is a very useful container for tabulated data. The first
# argument in this function is the file name (address to the file), and the second argument, "South" is the name of the WorkSheet in Excel.

# In[38]:

df = pd.read_excel("bustimesupdate.xlsx","South")


# Here, I am defining the function called **next_bus** that gets two arguments. The first one is a string that is the station name, the second one is a time. The time should be given in a datetime format.
# 
#         next_bus('Spruce Grove',datetime.time(hour = 5,minute=15,second=0))
#         
# The function makes two subsets of the main dataframe based on the time and station name.
# 

# In[55]:

def next_bus(mystation = 'Emerald', mytime = datetime.datetime.time(datetime.datetime.now())):
    
    def next_ride(mystation,mytime):
        temp = df[df.Time > mytime]
        #print(temp)
        temp1 = temp[temp.Station == mystation]
        # subset to find the arrival time to Village
        temp2 = df[df.Time > temp1.Time.iat[0]]
        temp2 = temp2[temp2.Station == 'Village']

        nextRide = str(temp1.Time.iat[0])

        nextRideVillage = str(temp2.Time.iat[0])
        return nextRide, nextRideVillage

    try:
        nextRide, nextRideVillage = next_ride(mystation,mytime)
        
    except:
        mytime = datetime.time(0,0,1)
        nextRide, nextRideVillage = next_ride(mystation,mytime)

    return nextRide, nextRideVillage

    


# Let's give it a shot and see how it works:

# In this example we call the function with a time.

# In[56]:

#next_bus('Emerald',datetime.time(23,50,0))


# In the second example we call the function without a time. In this case, it reads the current time of your system and findes your next ride.

# In[57]:

#next_bus('Village')


# If you call the function without any arguments, it will use **Emerald** as the station and your **Current Time** as the default value.

# In[58]:

#next_bus()


# You can put the python file inside your main program folder and use the import command to import it in your program and use it.
# 
#         from timkruz import next_bus
