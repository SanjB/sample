#!/usr/bin/env python
# coding: utf-8

# In[4]:


# import modules
import math
import pandas as pd
import numpy as np


# In[5]:


product_array=['Product0','Product1','Product2','Product3','Product4']
SIZE_OF_ARRAY = 5
df = pd.DataFrame({'Products' : product_array,
                   'Rate' : np.array(np.random.randint(20,30,size=SIZE_OF_ARRAY),dtype='int32'),
                   'Jan' : np.array(np.random.randint(1000,10000,size=SIZE_OF_ARRAY),dtype='int32'),
                   'Feb' : np.array(np.random.randint(2000,10000,size=SIZE_OF_ARRAY),dtype='int32'),
                   'Mar' : np.array(np.random.randint(4000,10000,size=SIZE_OF_ARRAY),dtype='int32'),    
                })
cols = ['Products','Rate','Jan','Feb','Mar']
df=df[cols]
df


# In[6]:


# Calculate new column from existing ones
# total sales
# Excel equivalent: =(C2+D2+E2) * B2
df["Total"] = (df["Jan"]+df["Feb"]+df["Mar"]*df["Rate"])
df["Comments"] = df["Total"].apply(lambda x: 'Target Met' if x > 300000 else'Target not met')
df


# In[5]:


# Named ranges
# Excel equivalent
#'JAN_SALES = (B2*C2)+(B3*C3)+(B4*C4)' etc.
jan_sales=(df["Jan"]*df["Rate"]).sum()
feb_sales=(df["Feb"]*df["Rate"]).sum()
mar_sales=(df["Mar"]*df["Rate"]).sum()

# Operations on Named ranges
# Excel equivalent
#'TOTAL=SUM(JAN_SALED,FEB_SALES,MAR_SALES)'
total = jan_sales + feb_sales + mar_sales
total


# In[ ]:




