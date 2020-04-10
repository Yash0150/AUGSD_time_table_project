# This file contains utility functions for course_load

import itertools
import math
import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile

def get_department_list():
    return ['BIO', 'CHE', 'CHEM', 'CS', 'ECON', 'EEE', 'HUM', 'MATH', 'MECH', 'PHY']

def get_department_cdc_list(dept):
    df = pd.read_excel('data.xlsx','CDC')
    df.replace(np.nan,0)
    Lst=[]
    for i in range(0, df.shape[0]):
        if(df['dept'][i]==dept):
            Lst.append([
                df['course no'][i],
                df['course title'][i],
                0 if math.isnan(df['L'][i]) else df['L'][i],
                0 if math.isnan(df['T'][i]) else df['T'][i],
                0 if math.isnan(df['P'][i]) else df['P'][i],
                0 if math.isnan(df['comcode'][i]) else df['comcode'][i],
            ])
    return Lst

def get_department_elective_list(dept):
    dfe= pd.read_excel('data.xlsx','ELECTIVE')
    Dict={}
    for i in range(0, dfe.shape[0]):
        if(dfe['Disc'][i]=='B.E (Electronics & Instrumentation)' or dfe['Disc'][i]=='B.E. (Electrical & Electronics)'):
            Dict[dfe['Disc'][i]]='EEE'
        if(dfe['Disc'][i]=='B.E. (Computer Science)' or dfe['Disc'][i]=='ME. (Computer Science)'):
            Dict[dfe['Disc'][i]]='CS'
        if(dfe['Disc'][i]=='ELECTRONICS AND COMMUNICATION ENGINEERING' or dfe['Disc'][i]=='M.E. (Embeded System)'):
            Dict[dfe['Disc'][i]]='EEE'
        if(dfe['Disc'][i]=='M.E. (Micro Electronics)'):
            Dict[dfe['Disc'][i]]='EEE' 
        if(dfe['Disc'][i]=='B.E. (Mechanical)' or dfe['Disc'][i]=='M.E. Design Engineering' or dfe['Disc'][i]=='M.E. Mechanical Engineering'):
            Dict[dfe['Disc'][i]]='MECH'
        if(dfe['Disc'][i]=='B.E.(Chemical)' or dfe['Disc'][i]=='M.E. (Chemical)'):
            Dict[dfe['Disc'][i]]='CHEM'
        if(dfe['Disc'][i]=='M.Sc. (Chemistry)'):
            Dict[dfe['Disc'][i]]='CHE'
        if(dfe['Disc'][i]=='ENGLISH  MINOR' or dfe['Disc'][i]=='GENERAL' or dfe['Disc'][i]=='HUM' or dfe['Disc'][i]=='M. Phil. in Liberal Studies' or dfe['Disc'][i]=='PEP Minor'):
            Dict[dfe['Disc'][i]]='HUM'
        if(dfe['Disc'][i]=='M.E. (Biotechnology )' or dfe['Disc'][i]=='M.E. Sanitation Science, Technology and Management' or dfe['Disc'][i]=='M.Sc. (Biological Science) '):
            Dict[dfe['Disc'][i]]='BIO'
        if(dfe['Disc'][i]=='M.Sc. (Economics)' or dfe['Disc'][i]=='Minor In Finace'):
            Dict[dfe['Disc'][i]]='ECON'
        if(dfe['Disc'][i]=='M.Sc. (Mathematics)'):
            Dict[dfe['Disc'][i]]='MATH'
        if(dfe['Disc'][i]=='M.Sc. (Physics)'):
            Dict[dfe['Disc'][i]]='PHY'
    Lst=[]
    for i in range(0, dfe.shape[0]):
        if(Dict[dfe['Disc'][i]]==dept):
            Lst.append([dfe['Course No'][i],dfe['Course Title'][i],dfe['com code'][i]])

    return Lst

def get_department_instructor_list(dept):
    dff= pd.read_excel('data.xlsx','FACULTY')
    Lst=[]
    for i in range(0, 176):
        if(dff['discipline'][i]==dept):
            Lst.append([dff['name'][i],dff['PSRN'][i]])
    return Lst

def get_department_phd_student_list(dept):
    dfs= pd.read_excel('data.xlsx','RESEARCH SCHOLAR')
    Lst=[]
    if(dept=='HSS' or dept=='HUM'):
        for i in range(0, 420):
            if(dfs['discipline'][i]=='HSS' or dfs['discipline'][i]=='HUM'):
                Lst.append([dfs['name'][i],dfs['IDNO'][i]])
    else:
        for i in range(0, 420):
            if(dfs['discipline'][i][0:3]==dept[0:3]):
                if(dept=='CHE'):
                    if(dfs['discipline'][i]=='CHE' or dfs['discipline'][i]=='CHEMISTRY'):
                        Lst.append([dfs['name'][i],dfs['IDNO'][i]])
                elif(dept=='CHEM'):
                    if(dfs['discipline'][i]=='CHEM' or dfs['discipline'][i]=='CHEMICAL'):
                        Lst.append([dfs['name'][i],dfs['IDNO'][i]])
                else:
                    Lst.append([dfs['name'][i],dfs['IDNO'][i]])
    return Lst

def get_instructor_list():
    dff= pd.read_excel('data.xlsx','FACULTY')
    Lst=[]
    for i in range(0,176):
        Lst.append([dff['name'][i],dff['PSRN'][i]])
    return Lst
