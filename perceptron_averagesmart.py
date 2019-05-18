import os

w=[0]
age=[0]
hours=[0]
input_age=0
avg_age=0
workclass={'Private':0, 'Self-emp-not-inc':0, 'Self-emp-inc':0, 'Federal-gov':0, 'Local-gov':0, 'State-gov':0, 'Without-pay':0, 'Never-worked':0}
key_workclass=['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked']
education={'Bachelors':0, 'Some-college':0, '11th':0, 'HS-grad':0, 'Prof-school':0, 'Assoc-acdm':0, 'Assoc-voc':0, '9th':0, '7th-8th':0, '12th':0, 'Masters':0, '1st-4th':0, '10th':0, 'Doctorate':0, '5th-6th':0, 'Preschool':0}
key_education=['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', '9th', '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool']
maritalstatus={'Married-civ-spouse':0, 'Divorced':0, 'Never-married':0, 'Separated':0, 'Widowed':0, 'Married-spouse-absent':0, 'Married-AF-spouse':0}
key_maritalstatus=['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse']
occupation={'Tech-support':0, 'Craft-repair':0, 'Other-service':0, 'Sales':0, 'Exec-managerial':0, 'Prof-specialty':0, 'Handlers-cleaners':0, 'Machine-op-inspct':0, 'Adm-clerical':0, 'Farming-fishing':0, 'Transport-moving':0, 'Priv-house-serv':0, 'Protective-serv':0, 'Armed-Forces':0}
key_occupation=['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces']
race={'White':0, 'Asian-Pac-Islander':0, 'Amer-Indian-Eskimo':0, 'Other':0, 'Black':0}
key_race=['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']
sex={'Female':0, 'Male':0}
key_sex=['Female', 'Male']
count_mistake=0
input_hours=0
avg_hours=0
nativecountry={'United-States':0, 'Cambodia':0, 'England':0, 'Puerto-Rico':0, 'Canada':0, 'Germany':0, 'Outlying-US(Guam-USVI-etc)':0, 'India':0, 'Japan':0, 'Greece':0, 'South':0, 'China':0, 'Cuba':0, 'Iran':0, 'Honduras':0, 'Philippines':0, 'Italy':0, 'Poland':0, 'Jamaica':0, 'Vietnam':0, 'Mexico':0, 'Portugal':0, 'Ireland':0, 'France':0, 'Dominican-Republic':0, 'Laos':0, 'Ecuador':0, 'Taiwan':0, 'Haiti':0, 'Columbia':0, 'Hungary':0, 'Guatemala':0, 'Nicaragua':0, 'Scotland':0, 'Thailand':0, 'Yugoslavia':0, 'El-Salvador':0, 'Trinadad&Tobago':0, 'Peru':0, 'Hong':0, 'Holand-Netherlands':0}
key_nativecountry=['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands']
salary={'>50K\n':0, '<=50K\n':0}
count=0
u=[0]
for num in range(1,95):
    w.append(0)
    u.append(0)
for T in range(0,5):
    with open("income.train.txt","r") as f:
            lines=f.readlines()
            for line in lines:
                       
                workclass={'Private':0, 'Self-emp-not-inc':0, 'Self-emp-inc':0, 'Federal-gov':0, 'Local-gov':0, 'State-gov':0, 'Without-pay':0, 'Never-worked':0}
                key_workclass=['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked']
                education={'Bachelors':0, 'Some-college':0, '11th':0, 'HS-grad':0, 'Prof-school':0, 'Assoc-acdm':0, 'Assoc-voc':0, '9th':0, '7th-8th':0, '12th':0, 'Masters':0, '1st-4th':0, '10th':0, 'Doctorate':0, '5th-6th':0, 'Preschool':0}
                key_education=['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', '9th', '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool']
                maritalstatus={'Married-civ-spouse':0, 'Divorced':0, 'Never-married':0, 'Separated':0, 'Widowed':0, 'Married-spouse-absent':0, 'Married-AF-spouse':0}
                key_maritalstatus=['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse']
                occupation={'Tech-support':0, 'Craft-repair':0, 'Other-service':0, 'Sales':0, 'Exec-managerial':0, 'Prof-specialty':0, 'Handlers-cleaners':0, 'Machine-op-inspct':0, 'Adm-clerical':0, 'Farming-fishing':0, 'Transport-moving':0, 'Priv-house-serv':0, 'Protective-serv':0, 'Armed-Forces':0}
                key_occupation=['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces']
                race={'White':0, 'Asian-Pac-Islander':0, 'Amer-Indian-Eskimo':0, 'Other':0, 'Black':0}
                key_race=['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']
                sex={'Female':0, 'Male':0}
                key_sex=['Female', 'Male']
                nativecountry={'United-States':0, 'Cambodia':0, 'England':0, 'Puerto-Rico':0, 'Canada':0, 'Germany':0, 'Outlying-US(Guam-USVI-etc)':0, 'India':0, 'Japan':0, 'Greece':0, 'South':0, 'China':0, 'Cuba':0, 'Iran':0, 'Honduras':0, 'Philippines':0, 'Italy':0, 'Poland':0, 'Jamaica':0, 'Vietnam':0, 'Mexico':0, 'Portugal':0, 'Ireland':0, 'France':0, 'Dominican-Republic':0, 'Laos':0, 'Ecuador':0, 'Taiwan':0, 'Haiti':0, 'Columbia':0, 'Hungary':0, 'Guatemala':0, 'Nicaragua':0, 'Scotland':0, 'Thailand':0, 'Yugoslavia':0, 'El-Salvador':0, 'Trinadad&Tobago':0, 'Peru':0, 'Hong':0, 'Holand-Netherlands':0}
                key_nativecountry=['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands']
                salary={'>50K\n':0, '<=50K\n':0}
                y=0
                age_y=0
                workclass_y=0
                education_y=0
                maritalstatus_y=0
                occupation_y=0
                race_y=0
                sex_y=0
                hours_y=0
                nativecountry_y=0
                count=count+1
                a=line.split(", ")
                
                input_age=int(a[0])
                
                avg_age=(avg_age*(count-1)+input_age)/count
                if input_age>avg_age:
                    age=1
                else:
                    age=0
                    '''
                print(input_age)
                print(age)
                print(avg_age)
                print("count",count)
                '''
                workclass[a[1]]=1
                
                education[a[2]]=1
                
                maritalstatus[a[3]]=1
                occupation[a[4]]=1
                race[a[5]]=1
                sex[a[6]]=1
                
                
                input_hours=int(a[7])
                avg_hours=(avg_hours*(count-1)+input_hours)/count
                if input_hours>avg_hours:
                    hours=1                
                else:
                    hours=0
                
                nativecountry[a[8]]=1
                salary[a[9]]=1
                
                    
                '''print (1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+1+1+len(nativecountry))'''

                age_y=w[0]*age
                for num in range(0,len(workclass)):
                    workclass_y=w[num+1]*workclass[key_workclass[num]]+workclass_y
                for num in range(0,len(education)):
                    education_y=w[num+1+len(workclass)]*education[key_education[num]]+education_y
                for num in range(0,len(maritalstatus)):
                    maritalstatus_y=w[num+1+len(workclass)+len(education)]*maritalstatus[key_maritalstatus[num]]+maritalstatus_y
                for num in range(0,len(occupation)):
                    occupation_y=w[num+1+len(workclass)+len(education)+len(maritalstatus)]*occupation[key_occupation[num]]+occupation_y
                for num in range(0,len(race)):
                    race_y=w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)]*race[key_race[num]]+race_y
                for num in range(0,len(sex)):
                    sex_y=w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)]*sex[key_sex[num]]+sex_y
                
                hours_y=w[1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)]*hours
                for num in range(0,len(nativecountry)):
                    nativecountry_y=w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)+1]*nativecountry[key_nativecountry[num]]+nativecountry_y
                y=age_y+workclass_y+education_y+maritalstatus_y+occupation_y+race_y+sex_y+hours_y+nativecountry_y
                if y>0:
                    y=1
                if y<=0:
                    y=-1            
                  
                if (y==1 and salary['<=50K\n'])or(y==-1 and salary['>50K\n']):
                    count_mistake=count_mistake+1
                    w[0]=y*-1*age+w[0]
                    u[0]=y*-1*count*age+u[0]
                    for num in range(0,len(workclass)):
                        w[num+1]=y*-1*workclass[key_workclass[num]]+w[num+1]
                        u[num+1]=y*-1*count*workclass[key_workclass[num]]+u[num+1]
                    for num in range(0,len(education)):
                        w[num+1+len(workclass)]=y*-1*education[key_education[num]]+w[num+1+len(workclass)]
                        u[num+1+len(workclass)]=y*-1*count*education[key_education[num]]+u[num+1+len(workclass)]
                    for num in range(0,len(maritalstatus)):
                        w[num+1+len(workclass)+len(education)]=y*-1*maritalstatus[key_maritalstatus[num]]+w[num+1+len(workclass)+len(education)]
                        u[num+1+len(workclass)+len(education)]=y*-1*count*maritalstatus[key_maritalstatus[num]]+u[num+1+len(workclass)+len(education)]
                    for num in range(0,len(occupation)):
                        w[num+1+len(workclass)+len(education)+len(maritalstatus)]=y*-1*occupation[key_occupation[num]]+w[num+1+len(workclass)+len(education)+len(maritalstatus)]
                        u[num+1+len(workclass)+len(education)+len(maritalstatus)]=y*-1*count*occupation[key_occupation[num]]+u[num+1+len(workclass)+len(education)+len(maritalstatus)]
                    for num in range(0,len(race)):
                        w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)]=y*-1*race[key_race[num]]+w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)]
                        u[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)]=y*-1*count*race[key_race[num]]+u[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)]
                    for num in range(0,len(sex)):
                        w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)]=y*-1*sex[key_sex[num]]+w[1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)]
                        u[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)]=y*-1*count*sex[key_sex[num]]+u[1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)]
                    w[1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)]=y*-1*hours+w[1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)]
                    u[1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)]=y*-1*count*hours+u[1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)]
                    for num in range(0,len(nativecountry)):
                        w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)+1]=y*-1*nativecountry[key_nativecountry[num]]+w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)+1]
                        u[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)+1]=y*-1*count*nativecountry[key_nativecountry[num]]+u[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)+1]
                '''
                if y==1 and salary['<=50K\n']:
                    print("in")

                if y==-1 and salary['>50K\n']:
                    print("out")
                print(salary) 
                print(y)
                print(w)'''
            for num in range(0,len(u)):
                w[num]=w[num]-u[num]/count
            
            '''print(w)'''
            print(count_mistake)
            count_mistake=0
            avg_hours=0
            avg_age=0
            count=0
            for num in range(0,len(u)):
                u[num]=0
            with open("income.dev.txt","r") as f:
                lines=f.readlines()
                for line in lines:
                       
                    workclass={'Private':0, 'Self-emp-not-inc':0, 'Self-emp-inc':0, 'Federal-gov':0, 'Local-gov':0, 'State-gov':0, 'Without-pay':0, 'Never-worked':0}
                    key_workclass=['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked']
                    education={'Bachelors':0, 'Some-college':0, '11th':0, 'HS-grad':0, 'Prof-school':0, 'Assoc-acdm':0, 'Assoc-voc':0, '9th':0, '7th-8th':0, '12th':0, 'Masters':0, '1st-4th':0, '10th':0, 'Doctorate':0, '5th-6th':0, 'Preschool':0}
                    key_education=['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', '9th', '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool']
                    maritalstatus={'Married-civ-spouse':0, 'Divorced':0, 'Never-married':0, 'Separated':0, 'Widowed':0, 'Married-spouse-absent':0, 'Married-AF-spouse':0}
                    key_maritalstatus=['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse']
                    occupation={'Tech-support':0, 'Craft-repair':0, 'Other-service':0, 'Sales':0, 'Exec-managerial':0, 'Prof-specialty':0, 'Handlers-cleaners':0, 'Machine-op-inspct':0, 'Adm-clerical':0, 'Farming-fishing':0, 'Transport-moving':0, 'Priv-house-serv':0, 'Protective-serv':0, 'Armed-Forces':0}
                    key_occupation=['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces']
                    race={'White':0, 'Asian-Pac-Islander':0, 'Amer-Indian-Eskimo':0, 'Other':0, 'Black':0}
                    key_race=['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']
                    sex={'Female':0, 'Male':0}
                    key_sex=['Female', 'Male']
                    nativecountry={'United-States':0, 'Cambodia':0, 'England':0, 'Puerto-Rico':0, 'Canada':0, 'Germany':0, 'Outlying-US(Guam-USVI-etc)':0, 'India':0, 'Japan':0, 'Greece':0, 'South':0, 'China':0, 'Cuba':0, 'Iran':0, 'Honduras':0, 'Philippines':0, 'Italy':0, 'Poland':0, 'Jamaica':0, 'Vietnam':0, 'Mexico':0, 'Portugal':0, 'Ireland':0, 'France':0, 'Dominican-Republic':0, 'Laos':0, 'Ecuador':0, 'Taiwan':0, 'Haiti':0, 'Columbia':0, 'Hungary':0, 'Guatemala':0, 'Nicaragua':0, 'Scotland':0, 'Thailand':0, 'Yugoslavia':0, 'El-Salvador':0, 'Trinadad&Tobago':0, 'Peru':0, 'Hong':0, 'Holand-Netherlands':0}
                    key_nativecountry=['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands']
                    salary={'>50K\n':0, '<=50K\n':0}
                    y=0
                    age_y=0
                    workclass_y=0
                    education_y=0
                    maritalstatus_y=0
                    occupation_y=0
                    race_y=0
                    sex_y=0
                    hours_y=0
                    nativecountry_y=0
                    count=count+1
                    a=line.split(", ")
                    
                    input_age=int(a[0])
                    
                    avg_age=(avg_age*(count-1)+input_age)/count
                    if input_age>avg_age:
                        age=1
                    else:
                        age=0
                        '''
                    print(input_age)
                    print(age)
                    print(avg_age)
                    print("count",count)
                    '''
                    workclass[a[1]]=1
                    
                    education[a[2]]=1
                    
                    maritalstatus[a[3]]=1
                    occupation[a[4]]=1
                    race[a[5]]=1
                    sex[a[6]]=1
                    
                    
                    input_hours=int(a[7])
                    avg_hours=(avg_hours*(count-1)+input_hours)/count
                    if input_hours>avg_hours:
                        hours=1                
                    else:
                        hours=0
                    
                    nativecountry[a[8]]=1
                    salary[a[9]]=1
                    
                        
                    '''print (1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+1+1+len(nativecountry))'''

                    age_y=w[0]*age
                    for num in range(0,len(workclass)):
                        workclass_y=w[num+1]*workclass[key_workclass[num]]+workclass_y
                    for num in range(0,len(education)):
                        education_y=w[num+1+len(workclass)]*education[key_education[num]]+education_y
                    for num in range(0,len(maritalstatus)):
                        maritalstatus_y=w[num+1+len(workclass)+len(education)]*maritalstatus[key_maritalstatus[num]]+maritalstatus_y
                    for num in range(0,len(occupation)):
                        occupation_y=w[num+1+len(workclass)+len(education)+len(maritalstatus)]*occupation[key_occupation[num]]+occupation_y
                    for num in range(0,len(race)):
                        race_y=w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)]*race[key_race[num]]+race_y
                    for num in range(0,len(sex)):
                        sex_y=w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)]*sex[key_sex[num]]+sex_y
                    
                    hours_y=w[1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)]*hours
                    for num in range(0,len(nativecountry)):
                        nativecountry_y=w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)+1]*nativecountry[key_nativecountry[num]]+nativecountry_y
                    y=age_y+workclass_y+education_y+maritalstatus_y+occupation_y+race_y+sex_y+hours_y+nativecountry_y
                    if y>0:
                        y=1
                    if y<=0:
                        y=-1            
                      
                    if (y==1 and salary['<=50K\n'])or(y==-1 and salary['>50K\n']):
                        count_mistake=count_mistake+1
                        w[0]=y*-1*age+w[0]
                        u[0]=y*-1*count*age+u[0]
                        for num in range(0,len(workclass)):
                            w[num+1]=y*-1*workclass[key_workclass[num]]+w[num+1]
                            u[num+1]=y*-1*count*workclass[key_workclass[num]]+u[num+1]
                        for num in range(0,len(education)):
                            w[num+1+len(workclass)]=y*-1*education[key_education[num]]+w[num+1+len(workclass)]
                            u[num+1+len(workclass)]=y*-1*count*education[key_education[num]]+u[num+1+len(workclass)]
                        for num in range(0,len(maritalstatus)):
                            w[num+1+len(workclass)+len(education)]=y*-1*maritalstatus[key_maritalstatus[num]]+w[num+1+len(workclass)+len(education)]
                            u[num+1+len(workclass)+len(education)]=y*-1*count*maritalstatus[key_maritalstatus[num]]+u[num+1+len(workclass)+len(education)]
                        for num in range(0,len(occupation)):
                            w[num+1+len(workclass)+len(education)+len(maritalstatus)]=y*-1*occupation[key_occupation[num]]+w[num+1+len(workclass)+len(education)+len(maritalstatus)]
                            u[num+1+len(workclass)+len(education)+len(maritalstatus)]=y*-1*count*occupation[key_occupation[num]]+u[num+1+len(workclass)+len(education)+len(maritalstatus)]
                        for num in range(0,len(race)):
                            w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)]=y*-1*race[key_race[num]]+w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)]
                            u[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)]=y*-1*count*race[key_race[num]]+u[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)]
                        for num in range(0,len(sex)):
                            w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)]=y*-1*sex[key_sex[num]]+w[1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)]
                            u[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)]=y*-1*count*sex[key_sex[num]]+u[1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)]
                        w[1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)]=y*-1*hours+w[1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)]
                        u[1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)]=y*-1*count*hours+u[1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)]
                        for num in range(0,len(nativecountry)):
                            w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)+1]=y*-1*nativecountry[key_nativecountry[num]]+w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)+1]
                            u[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)+1]=y*-1*count*nativecountry[key_nativecountry[num]]+u[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)+1]
                    '''
                    if y==1 and salary['<=50K\n']:
                        print("in")

                    if y==-1 and salary['>50K\n']:
                        print("out")
                    print(salary) 
                    print(y)
                    print(w)'''
            for num in range(0,len(u)):
                w[num]=w[num]-u[num]/count
            
            '''print(w)'''
            print(count_mistake)
            count_mistake=0
            avg_hours=0
            avg_age=0
            count=0
            with open("income.test.txt","r") as f:
                lines=f.readlines()
                for line in lines:
                
                    workclass={'Private':0, 'Self-emp-not-inc':0, 'Self-emp-inc':0, 'Federal-gov':0, 'Local-gov':0, 'State-gov':0, 'Without-pay':0, 'Never-worked':0}
                    key_workclass=['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked']
                    education={'Bachelors':0, 'Some-college':0, '11th':0, 'HS-grad':0, 'Prof-school':0, 'Assoc-acdm':0, 'Assoc-voc':0, '9th':0, '7th-8th':0, '12th':0, 'Masters':0, '1st-4th':0, '10th':0, 'Doctorate':0, '5th-6th':0, 'Preschool':0}
                    key_education=['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', '9th', '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool']
                    maritalstatus={'Married-civ-spouse':0, 'Divorced':0, 'Never-married':0, 'Separated':0, 'Widowed':0, 'Married-spouse-absent':0, 'Married-AF-spouse':0}
                    key_maritalstatus=['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse']
                    occupation={'Tech-support':0, 'Craft-repair':0, 'Other-service':0, 'Sales':0, 'Exec-managerial':0, 'Prof-specialty':0, 'Handlers-cleaners':0, 'Machine-op-inspct':0, 'Adm-clerical':0, 'Farming-fishing':0, 'Transport-moving':0, 'Priv-house-serv':0, 'Protective-serv':0, 'Armed-Forces':0}
                    key_occupation=['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces']
                    race={'White':0, 'Asian-Pac-Islander':0, 'Amer-Indian-Eskimo':0, 'Other':0, 'Black':0}
                    key_race=['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']
                    sex={'Female':0, 'Male':0}
                    key_sex=['Female', 'Male']
                    nativecountry={'United-States':0, 'Cambodia':0, 'England':0, 'Puerto-Rico':0, 'Canada':0, 'Germany':0, 'Outlying-US(Guam-USVI-etc)':0, 'India':0, 'Japan':0, 'Greece':0, 'South':0, 'China':0, 'Cuba':0, 'Iran':0, 'Honduras':0, 'Philippines':0, 'Italy':0, 'Poland':0, 'Jamaica':0, 'Vietnam':0, 'Mexico':0, 'Portugal':0, 'Ireland':0, 'France':0, 'Dominican-Republic':0, 'Laos':0, 'Ecuador':0, 'Taiwan':0, 'Haiti':0, 'Columbia':0, 'Hungary':0, 'Guatemala':0, 'Nicaragua':0, 'Scotland':0, 'Thailand':0, 'Yugoslavia':0, 'El-Salvador':0, 'Trinadad&Tobago':0, 'Peru':0, 'Hong':0, 'Holand-Netherlands':0}
                    key_nativecountry=['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands']
                    salary={'>50K\n':0, '<=50K\n':0}
                    y=0
                    age_y=0
                    workclass_y=0
                    education_y=0
                    maritalstatus_y=0
                    occupation_y=0
                    race_y=0
                    sex_y=0
                    hours_y=0
                    nativecountry_y=0
                    count=count+1
                    input_age=int(line.split(", ")[0])
                    avg_age=(avg_age*(count-1)+input_age)/count
                    
                    if input_age>=avg_age:
                        age=1
                    else:
                        age=0
                    a=line.split(", ")
                    workclass[a[1]]=1
                    
                    education[a[2]]=1
                    
                    maritalstatus[a[3]]=1
                    occupation[a[4]]=1
                    race[a[5]]=1
                    sex[a[6]]=1
                    
                    
                    input_hours=int(a[7])
                    avg_hours=(avg_hours*(count-1)+input_hours)/count
                    if input_hours>=avg_hours:
                        hours=1
                        
                    else:
                        hours=0
                    
                    nativecountry[a[8]]=1
                    salary[a[9]]=1
                    
                        
                    

                    age_y=w[0]*age
                    for num in range(0,len(workclass)):
                        workclass_y=w[num+1]*workclass[key_workclass[num]]+workclass_y
                    for num in range(0,len(education)):
                        education_y=w[num+1+len(workclass)]*education[key_education[num]]+education_y
                    for num in range(0,len(maritalstatus)):
                        maritalstatus_y=w[num+1+len(workclass)+len(education)]*maritalstatus[key_maritalstatus[num]]+maritalstatus_y
                    for num in range(0,len(occupation)):
                        occupation_y=w[num+1+len(workclass)+len(education)+len(maritalstatus)]*occupation[key_occupation[num]]+occupation_y
                    for num in range(0,len(race)):
                        race_y=w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)]*race[key_race[num]]+race_y
                    for num in range(0,len(sex)):
                        sex_y=w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)]*sex[key_sex[num]]+sex_y
                    
                    hours_y=w[1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)]*hours
                    for num in range(0,len(nativecountry)):
                        nativecountry_y=w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)+1]*nativecountry[key_nativecountry[num]]+nativecountry_y
                    y=age_y+workclass_y+education_y+maritalstatus_y+occupation_y+race_y+sex_y+hours_y+nativecountry_y
                    if y>0:
                        y=1
                    if y<=0:
                        y=-1
                    
                        
                    if (y==1 and salary['<=50K\n'])or(y==-1 and salary['>50K\n']) :
                        count_mistake=count_mistake+1
                        '''
                        w[0]=y*-1*age+w[0]
                        for num in range(0,len(workclass)):
                            w[num+1]=y*-1*workclass[key_workclass[num]]+w[num+1]
                        for num in range(0,len(education)):
                            w[num+1+len(workclass)]=y*-1*education[key_education[num]]+w[num+1+len(workclass)]
                        for num in range(0,len(maritalstatus)):
                            w[num+1+len(workclass)+len(education)]=y*-1*maritalstatus[key_maritalstatus[num]]+w[num+1+len(workclass)+len(education)]
                        for num in range(0,len(occupation)):
                            w[num+1+len(workclass)+len(education)+len(maritalstatus)]=y*-1*occupation[key_occupation[num]]+w[num+1+len(workclass)+len(education)+len(maritalstatus)]
                        for num in range(0,len(race)):
                            w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)]=y*-1*race[key_race[num]]+w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)]
                        for num in range(0,len(sex)):
                            w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)]=y*-1*sex[key_sex[num]]+w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)]
                        w[1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)]=y*-1*hours+w[1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)]
                        for num in range(0,len(nativecountry)):
                            w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)+1]=y*-1*nativecountry[key_nativecountry[num]]+w[num+1+len(workclass)+len(education)+len(maritalstatus)+len(occupation)+len(race)+len(sex)+1]
                        '''
            '''print(w)'''
            print(count_mistake)
            count_mistake=0
            avg_hours=0
            avg_age=0
            count=0

        
            
            
            
           
         
            
            
       
        
       
