#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# # LOADING THE DATASET
# 

# In[5]:


df=pd.read_csv("C:\\Users\\MOHAMMED RUBEZ\\Downloads\\hotel_bookings 2.csv")


# # exploratory data analysis and data cleaning
# 
# 

# In[6]:


df.head()


# In[7]:


df.shape


# In[8]:


df.columns


# In[9]:


df.info()


# In[10]:


df['reservation_status_date']=pd.to_datetime(df['reservation_status_date'])


# In[11]:


df.info()


# In[12]:


df.describe(include='object')


# In[13]:


for col in df.describe(include='object').columns:
    print(col)
    print(df[col].unique())
    print('*'*50)


# In[14]:


df.isnull().sum()


# In[15]:


df.drop(['company','agent'],axis =1 ,inplace = True)
df.dropna(inplace = True)


# # df after droping columns['company','agent']

# In[16]:


df.isnull().sum()


# In[18]:


df.describe()


# # Removing Outliers

# In[19]:


df=df[df['adr']<5000]


# # Analysing the cleaned data and visualizing data
# 

# In[20]:


cancelled_percentage = df['is_canceled'].value_counts(normalize=True)
print(cancelled_percentage)
plt.figure(figsize=(5,6))
plt.title('reservation status count')
plt.bar(['Not canceled','Canceled'],df['is_canceled'].value_counts(),edgecolor ='k',width =0.7)
plt.show()
        


# In[46]:


plt.figure(figsize=(8, 4))
ax1 = sns.countplot(x='hotel', hue='is_canceled', data=df, palette='Blues')
ax1.legend(legend_labels, ['Not Canceled', 'Canceled'], title='Reservation Status')
legend_labels, _ = ax1.get_legend_handles_labels()


# In[22]:


resort_hotel = df[df['hotel']== 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)


# In[23]:


City_hotel = df[df['hotel']== 'City Hotel']
City_hotel['is_canceled'].value_counts(normalize = True)


# In[24]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
City_hotel = City_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[25]:


sns.set_style('darkgrid', {'axes.facecolor': 'grey', 'grid.color': 'grey'})

plt.figure(figsize=(12, 8))
plt.title('Average Daily Rate in City and Resort Hotel', fontsize=30)

plt.plot(resort_hotel.index, resort_hotel['adr'], label='Resort Hotel', color='black')  
plt.plot(City_hotel.index, City_hotel['adr'], label='City Hotel', color='red')  

plt.legend()
plt.xlabel('Index') 
plt.ylabel('Average Daily Rate')
plt.show()


# In[41]:


df['month'] = df['reservation_status_date'].dt.month

vibrant_colors = sns.color_palette("husl", 2)

plt.figure(figsize=(16, 8))
plt.title('Reservation Status Per Month',fontsize=30)
ax1 = sns.countplot(x='month', hue='is_canceled', data=df, palette=vibrant_colors)
ax1.legend(title='Reservation Status', labels=['Not Canceled', 'Canceled'])
ax1.set_facecolor('#f5f5f5')

plt.show()


# In[27]:


sns.set(style="darkgrid")

custom_colors_dark = sns.color_palette("dark", n_colors=len(df['month'].unique()))

plt.figure(figsize=(20, 10))
plt.title('ADR per month', fontsize=30)

sns.barplot(x='month', y='adr', data=df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index(), palette=custom_colors_dark)

plt.show()


# In[38]:


cancelled_data = df[df['is_canceled'] == 1]  
top_5_country = cancelled_data['country'].value_counts()[:5]

plt.figure(figsize=(10, 10))
plt.title('TOP 5 COUNTRIES WITH RESERVATIONS CANCELED')
plt.pie(top_5_country, autopct='%2f', labels=top_5_country.index)  
plt.show()


# # FINDING MARKET SEGMENT OF THE CUSTOMERS
# 

# In[29]:


import matplotlib.pyplot as plt

mk_seg = df['market_segment'].value_counts()

custom_colors_dark = ['#8c2d19', '#1a5276', '#196f3d', '#b27300', '#4d4d99', '#993366', '#4d994d']

plt.figure(figsize=(10, 10))
plt.title('MARKET SEGMENT OF THE CUSTOMERS')

explode = (0.1, 0, 0, 0, 0, 0, 0)
plt.pie(mk_seg, autopct='%1.1f%%', labels=mk_seg.index, colors=custom_colors_dark, explode=explode)

plt.show()


# In[30]:


import matplotlib.pyplot as plt

canceled_mk_seg = cancelled_data['market_segment'].value_counts(normalize=True)

plt.figure(figsize=(10, 6))
plt.title('CANCELED MARKET SEGMENT OF THE CUSTOMERS')

plt.plot(canceled_mk_seg.index, canceled_mk_seg * 100, marker='o', color='red', linestyle='-')

plt.xlabel('Market Segment')
plt.ylabel('Cancellation Percentage')
plt.xticks(rotation=45, ha='right')

plt.show()


# In[ ]:




