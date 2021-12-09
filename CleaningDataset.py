#!/usr/bin/env python
# coding: utf-8

import pandas as pd

def clean(path):
        df = pd.read_csv(path)
        #remove all the colonne with -1 value 
        df=df[df['Size']!='-1']
        df=df[df['Salary Estimate']!='-1']
        df=df[df['Founded']!='-1']


        #remove text from Salary 
        df['Salary Estimate']= df['Salary Estimate'].apply(lambda x:x.split('(')[0])

        #delete all the characters we don't need
        df['Salary Estimate'] = df['Salary Estimate'].str.replace('K','')
        df['Salary Estimate'] = df['Salary Estimate'].str.replace('$','',regex=False)
        df['Salary Estimate'] = df['Salary Estimate'].str.replace('Per Hour','')
        df['Salary Estimate'] = df['Salary Estimate'].str.replace('Employer Provided Salary:','')

        #add colonne min 
        df['Min_S'] = df['Salary Estimate'].apply(lambda x: int(x.split('-')[0]))
        df

        #add colonne max
        df['Max_S'] = df['Salary Estimate'].apply(lambda x: int(x.split('-')[-1]))

        #calcul of avarg
        df['avg_salary'] = (df.Min_S+df.Max_S)/2


        df['Company'] = df['Company Name'].apply(lambda x: x.split('\n')[0])
        df['Company Name']=df['Company']
        df = df.drop(['Company'], axis =1)



        #add a colonne of coutry of each job
        df['Country'] =df['Location'].apply(lambda s : s[-2:])

        #calculate the age of company
        x=df['Founded']
        df['age_company']=2021-x


        df['Size']=df['Size'].astype(str).replace("NaN"," ")
        df['Founded']=df['Founded'].astype(str).replace("nan"," ")
        df['Type of ownership']=df['Type of ownership'].astype(str).replace("nan"," ")
        df['age_company']=df['age_company'].astype(str).replace("nan"," ")


        #count number d'occ in describe session 
        df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
        df['java'] = df['Job Description'].apply(lambda x: 1 if 'java' in x.lower() else 0)
        df['machine learning'] = df['Job Description'].apply(lambda x: 1 if 'machine learning' in x.lower() else 0)
        df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

        #function that defines the exact title of jobs (short title)
        def title_simplifier(title):
            if 'data scientist' in title.lower():
                return 'data scientist'
            elif 'data engineer' in title.lower():
                return 'data engineer'
            elif 'analyst' in title.lower():
                return 'analyst'
            elif 'machine learning' in title.lower():
                return 'ML'
            elif 'manager' in title.lower():
                return 'manager'
            elif 'director' in title.lower():
                return 'director'
            else:
                return 'na'



        df['Job'] = df['Job Title'].apply(title_simplifier)

        #function that defines the grade of the job
        def seniority(title):
            if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower():
                    return 'senior'
            elif 'jr' in title.lower() or 'jr.' in title.lower():
                return 'jr'
            else:
                return 'na'



        df['Seniority'] = df['Job Title'].apply(seniority)
        return pd.DataFrame(df)