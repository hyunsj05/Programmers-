#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
#input = user id ,job id output= applied
data=pd.read_csv("train.csv")
#user id, job id, applied *6000
job_data=pd.read_csv("job_tags.csv")
#job id, tag id *3477 
user_data=pd.read_csv("user_tags.csv")
# user id, tag id *17194
company_data=pd.read_csv("job_companies.csv")
applied=data['applied']
# company id job id company size *733
# print(company_data)
# print(company_data)
# print(job_data)
# print(data["userID"]=='fe292163d06253b716e9a0099b42031d')


# data= userID, jobID, applied 6000 
# 
# job_data= jobID, tagID 3477 
# 
# user_data= userID, tagID 17194 
# 
# company_data= companyID, jobID, companySize  733

# # Try 2 
# ## 다음번에는 진짜로 머신러닝 할수 있도록 하자
# ## 유저 아이디, job id, 관심있는 job id 의 태그가 유저관심이 있는지, company id , company size 이 형태로 data frame 짜자
# ### 그리고 내일 은 이거 바탕으로 머신러닝 모델하나 만드는걸 목표로하자

# In[2]:


user_prefer=[]
company_id=[]
company_size=[]
for po,i in enumerate(data['userID']):
    jobid=data['jobID'][po]
    tem=job_data['jobID']==jobid
    job_tag=job_data['tagID'][tem]
    tem=user_data['userID']==i
    user_tag=user_data['tagID'][tem]
    flag=1
    tem=company_data['jobID']==jobid
    companyid=company_data['companyID'][tem]
    companysize=company_data['companySize'][tem]
    for j in companysize:
        company_size.append(j)
    for j in companyid:
        company_id.append(j)
#     company_id.append(companyid)
#     company_size.append(companysize)
#     print(job_tag['tagID'],1)
#     print(user_tag['tagID'],2)
    tem=0
    for j in job_tag:
        if sum(user_tag==j):
            tem+=1
#     user_prefer.append(tem/len(jobid))
    user_prefer.append(tem)
#     user_prefer.append(tem/len(job_tag))
# print(company_size)
for po,i in enumerate(company_size):
    if i=='11-50':
        company_size[po]=1;
    elif i=='51-100':
        company_size[po]=2;
    elif i=='101-200':
        company_size[po]=3;
    elif i=='201-500':
        company_size[po]=4;
    elif i=='501-1000':
        company_size[po]=5;
    elif i=='1000 이상':
        company_size[po]=6;
    else:
        company_size[po]=0;
# print(company_size)
# company_size=company_size/6
data=pd.DataFrame(data,columns=['userID','jobID','user_prefer','companyId','companySize','applied'])
data['user_prefer']=user_prefer
data['companyId']=company_id
data['companySize']=company_size
data['applied']=applied
del data['jobID']
del data['companyId']


# In[59]:


X=data[["user_prefer","companySize"]]
Y=data[["applied"]]
from sklearn.preprocessing import StandardScaler
x_std =StandardScaler().fit_transform(X)
# X.head()
# Y.head()


# In[60]:


import matplotlib.pyplot as plt
markers=['^','s']
data.head()
for i,marker in enumerate(markers):
    x_d=data[data['applied']==i]['user_prefer']
    y_d=data[data['applied']==i]['companySize']
    plt.scatter(x_d,y_d,marker=marker)
plt.show()


# In[3]:


from sklearn.preprocessing import StandardScaler
print(data)
a=data.iloc[:,1:3]
aa=StandardScaler().fit_transform(a)
aaa=pd.DataFrame(aa)
aaa['applied']=data[["applied"]]
# aaa.describe()
# print(aa)


# In[7]:


# print(data)
markers=['^','s']
# data.head()
data=aaa
for i,marker in enumerate(markers):
    x_d=data[data['applied']==i][0]
    y_d=data[data['applied']==i][1]
    plt.scatter(x_d,y_d,marker=marker)
plt.show()


# In[4]:


from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
acc=[]
from sklearn.model_selection import train_test_split
training_data, validation_data , training_labels, validation_labels = train_test_split(aa, data["applied"], test_size = 0.2, random_state = 100)
for i in range(1,101,1):
#     print(i)
    cla=KNeighborsClassifier(n_neighbors=i)
#     cla.fit(aa[0:5000],data["applied"][0:5000])
#     cla.fit(aa,data["applied"])
    cla.fit(training_data,training_labels)
#     acc.append(cla.score(aa[5000:],data["applied"][5000:]))
#     acc.append(cla.score(aa,data["applied"]))
    acc.append(cla.score(validation_data,validation_labels))
plt.plot(range(1,1001,1), acc)
plt.xlabel("k")
plt.ylabel("Validation Accuracy")
plt.show()


# In[16]:



cla=KNeighborsClassifier(n_neighbors=300)
cla.fit(training_data,training_labels)


# In[19]:


test=pd.read_csv("test_job.csv")
# test.head()
data=test
user_prefer=[]
company_id=[]
company_size=[]
for po,i in enumerate(data['userID']):
    jobid=data['jobID'][po]
    tem=job_data['jobID']==jobid
    job_tag=job_data['tagID'][tem]
    tem=user_data['userID']==i
    user_tag=user_data['tagID'][tem]
    flag=1
    tem=company_data['jobID']==jobid
    companyid=company_data['companyID'][tem]
    companysize=company_data['companySize'][tem]
    for j in companysize:
        company_size.append(j)
    for j in companyid:
        company_id.append(j)
#     company_id.append(companyid)
#     company_size.append(companysize)
#     print(job_tag['tagID'],1)
#     print(user_tag['tagID'],2)
    tem=0
    for j in job_tag:
        if sum(user_tag==j):
            tem+=1
#     user_prefer.append(tem/len(jobid))
    user_prefer.append(tem)
#     user_prefer.append(tem/len(job_tag))
# print(company_size)
for po,i in enumerate(company_size):
    if i=='11-50':
        company_size[po]=1;
    elif i=='51-100':
        company_size[po]=2;
    elif i=='101-200':
        company_size[po]=3;
    elif i=='201-500':
        company_size[po]=4;
    elif i=='501-1000':
        company_size[po]=5;
    elif i=='1000 이상':
        company_size[po]=6;
    else:
        company_size[po]=0;
# print(company_size)
# company_size=company_size/6
data=pd.DataFrame(data,columns=['userID','jobID','user_prefer','companyId','companySize','applied'])
data['user_prefer']=user_prefer
data['companyId']=company_id
data['companySize']=company_size
# data['applied']=applied
del data['jobID']
del data['companyId']
from sklearn.preprocessing import StandardScaler

a=data.iloc[:,1:3]
aa=StandardScaler().fit_transform(a)
aaa=pd.DataFrame(aa)
tem=cla.predict(aaa)
temp=len(tem)

import csv
with open("answer.csv",'w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['apllied'])
    for i in tem:
        writer.writerow([i])
# aaa['applied']=data[["applied"]]


# In[10]:


from sklearn.preprocessing import StandardScaler

a=data.iloc[:,1:3]
aa=StandardScaler().fit_transform(a)
aaa=pd.DataFrame(aa)
aaa['applied']=data[["applied"]]
tem=cla.predict(aa)
import csv
with open("answer.csv",'w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['apllied'])
    for i in tem:
        writer.writerow([i])


# In[92]:


tem=cla.predict(aa)
temp=len(tem)
tem2=[[0]*N for i in range(temp)]
for i in range(temp):
    for j in range(temp):
        


# In[ ]:





# In[100]:


import csv
with open("answer.csv",'w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['apllied'])
    for i in tem:
        writer.writerow([i])


# ## try 1
# ### 유저가 관심있는 tag면 지원

# In[7]:


# test=pd.read_csv("test_job.csv")
# test=data
# # user id job id * 2435
# # print(len(pd.unique(company_data["jobID"])))
# test_id=test["userID"]
# job_id=test["jobID"]
# # r_ans=test["applied"]
# answer=[]
# # print(job_data['tagID'])
# for po,k in enumerate(test_id):
# #     print(po,k)
# #     i=k.loc('userID')
#     tag2=user_data[user_data['userID'].isin([k])]
#     tag=tag2['tagID']
# #     print(user_data[user_data['userID'].isin([i])])
#     job=[]
#     for j in tag:
#         job.append(job_data[job_data['tagID'].isin([j])]['jobID'].tolist())
# #     print(job)
# #     print(job_id[po])
# #     break
#     flag=0
#     for j in job:
#         if job_id[po] in j:
#             answer.append(1)
#             flag=1
#             break
#     if flag==0:
#         answer.append(0)
# print(answer)
    
# # print(test_id)


# In[8]:


# # d=pd.DataFrame({"applied" : answer})
# # d.to_csv("answer2.csv")
# a=0
# b=0
# c=0
# d=0
# r_ans=test["applied"]
# for po,i in enumerate(answer):
#     if i==r_ans[po]:
#         a=a+i
#         b=b+1
#     else:
#         c=c+i
#         d=d+1
# print(a,d-c,"\n",c,b-a)
# print(sum(answer))
#     if i==1:

