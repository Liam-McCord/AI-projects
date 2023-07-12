#Importing CSV reader and time
import pandas as pd
import time



#Setup and starting variables
#Survivors per class
PClass1 = 0
PClass2 = 0
PClass3 = 0
Survival = 0

total = 0

#Deaths per class
DPClass1 = 0
DPClass2 = 0
DPClass3 = 0

#Survivor/Death rates per gender
PMale = 0
PFemale = 0
DPMale = 0
DPFemale = 0

samplesize = int(input("What is your needed passenger sample size? "))
samplesize = samplesize - 1
df = pd.read_csv('training.csv')
didtheydie = []
importantinfo = []
df.head(10)
df5r = df.loc[:samplesize,:]
df5r.shape
df5r.head()
df5r.values.tolist()
tempnumber = 0


for l in df5r.values.tolist():
    importantinfo = [l[1], l[2], l[3], l[4]]
    didtheydie.append(importantinfo)
    importantinfo = [0,0]

# Adds dead/alive passengers to the total based on class
for i in didtheydie:
    Survival = i[0]
    PClass = i[1]
    PGender = i[3]
    if Survival == 0:
        if PClass == 1:
            DPClass1 = DPClass1 + 1
        elif PClass == 2:
            DPClass2 = DPClass2 + 1    
        elif PClass == 3:
            DPClass3 = DPClass3 + 1
        if PGender == "male":
            DPMale = DPMale + 1
        elif PGender == "female":
            DPFemale = DPFemale + 1     
    #Class         
    if PClass == 1:
        PClass1 = PClass1 + 1
    elif PClass == 2:
        PClass2 = PClass2 + 1    
    elif PClass == 3:
        PClass3 = PClass3 + 1 
    #Gender
    if PGender == "male":
        PMale = PMale + 1
    elif PGender == "female":
        PFemale = PFemale + 1      
    total = total + 1

print(PMale, DPMale)

# Calls DPClass (Number of deaths per class) and divides it by PClass (Total population per class), then converts it to a readable percentage.
if DPClass1 > 0:
    SurvivalRateClass1 = DPClass1 / PClass1
else:
    SurvivalRateClass1 = 1
print("In Class 1, you have a {}% chance of dying.".format(100 * SurvivalRateClass1))

if DPClass2 > 0:
    SurvivalRateClass2 = DPClass2 / PClass2
else:
    SurvivalRateClass2 = 1
print("In Class 2, you have a {}% chance of dying.".format(100 * SurvivalRateClass2))

if DPClass3 > 0:
    SurvivalRateClass3 = DPClass3 / PClass3
else:
    SurvivalRateClass3 = 1
print("In Class 3, you have a {}% chance of dying.".format(100 * SurvivalRateClass3))

if DPMale > 0:
    SurvivalRateMale = DPMale / PMale
else: 
    SurvivalRateMale = 1
if DPFemale > 0:
    SurvivalRateFemale = DPFemale / PFemale
else: 
    SurvivalRateFemale = 1  





# Allows inputs of new passengers and checks the percentage of them dying based on entered factors
work = True
while work == True:
    time.sleep(3)
    classrate = 0
    yourgender = 0
    passenger = input("What class is your passenger? ")
    gender = input("What gender is your passenger? ")
    #Checkforclass
    if passenger == 1:
        classrate = SurvivalRateClass1
    elif passenger == 2:
        classrate = SurvivalRateClass2
    elif passenger == 3:
        classrate = SurvivalRateClass3
    #Checkforgender  
    if gender == "male" or gender == "Male":
        genderrate = SurvivalRateMale
    elif gender == "female" or gender == "Female":
        genderrate = SurvivalRateFemale
    
    PassengerSurvivalRate = (genderrate + classrate) / 2
    print("Your passenger has a {}% chance of dying in Class {} with a gender of {} and a sample size of {} passengers.".format(100 * PassengerSurvivalRate, passenger, gender, total))
    print(classrate, genderrate, PMale, DPMale)
        
    breakornot = 0
    breakornot = input("Continue? Y/N" )
    if breakornot == "N" or breakornot == "n":
        print("Stopping.")
        break
    else:
        print("Continuing.")
        print('\033[H\033[J')
        