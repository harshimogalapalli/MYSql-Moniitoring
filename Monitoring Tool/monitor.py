#!/usr/bin/env python
# coding: utf-8

# In[64]:


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import mysql
import mysql.connector
from matplotlib import pyplot as plt
plt.style.use('seaborn-darkgrid')

# In[65]:


cnx = mysql.connector.connect(host='localhost',port=3306,user='root',password='Harshi@053',database="performance_schema") 


# In[79]:


cursor = cnx.cursor()
xar1=[]
xar2=[]


# In[86]:
x=["Queries","Threads_connected","Slow_queries","Innodb_data_reads","Innodb_data_writes","Innodb_data_fsyncs","Bytes_received","Bytes_sent"]


xar1=[[] for i in range(len(x))]
def animate(i):

    values=[]
    names=[]
    for i in range(len(x)):
        str="Show status like '"+x[i]+"';"
        # print(str)
        cursor.execute(str)
        y1 = cursor.fetchall()
        xar1[i].append(int(y1[0][1]))
        
        # values.append(int(y1[0][1]))
        # names.append(y1[0][0])
        
        ax1[int(i%4)][int(i/4)].clear()
        ax1[int(i%4)][int(i/4)].plot(xar1[i],'.-')
        ax1[int(i%4)][int(i/4)].set_title(x[i])
        # print(ax1[int(i%4)][int(i/4)].get_yaxis_transform)
        ax1[int(i%4)][int(i/4)].fill_between(range(len(xar1[i])),xar1[i],facecolor='aqua', alpha=0.5)



# In[88]:




fig1 = plt.figure()
ax1 = fig1.subplots(4,2,sharex='col')
# ax1  = fig1.subplots_adjust(hspace=0.01)




ani = animation.FuncAnimation(fig1, animate, interval=2000)


plt.show()








