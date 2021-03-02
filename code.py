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
    for j in job_tag:
        if sum(user_tag==j):
            user_prefer.append(True)
            flag=0
            break
    if flag:
        user_prefer.append(False)
data=pd.DataFrame(data,columns=['userID','jobID','user_prefer','companyId','companySize','applied'])
data['user_prefer']=user_prefer
data['companyId']=company_id
data['companySize']=company_size
data['applied']=applied
data.head()
