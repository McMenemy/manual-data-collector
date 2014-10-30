'''
Created on Oct 1, 2014
    
@author: joshmcmenemy

'''
import os.path

date = (raw_input(
"""Please enter today's date (dd/mm/yyyy): """))
print date


'''                 '''
''' Sleep Questions '''
'''                 '''
bedTime = float(raw_input(
"""Please enter the army time you went to bed as decimal: """))
wakeTime = float(raw_input(
"""Please enter the army time you woke up as decimal: """))
if bedTime <= 24.0 and bedTime >= 12.0:
    sleepTime = 24.0 - bedTime + wakeTime
else:
    sleepTime = wakeTime - bedTime
print sleepTime
nap = (raw_input(
"""Did you take a nap? (y/n): """))
if nap == 'y':
    napTime = float(raw_input(
"""How long did you nap (hour decimal): """))
    napStart = nap = float(raw_input(
"""When did your nap start (army time as decimal): """))
    napEnd = napStart + napTime
else:
    napTime = 'na'
    napStart = 'na'
    napEnd = 'na'
    
 
'''                     '''
''' Nutrition Questions '''
'''                     '''
breakfast = raw_input(
"""Did you eat breakfast? (y/n): """)
if breakfast == 'y':
    breakfastSize = int(raw_input(
"""Rate the size of your breakfast (1=handful, 7=1.5 cups oatmeal, 10=stuffed) : """))
    breakfastNutrition = int(raw_input(
"""Rate the nutrition of your breakfast (1=really unhealthy, 10=super healthy) : """))
    breakfastTime = float(raw_input(
"""What time did you start breakfast (army time decimal): """))
    breakfastItem = raw_input(
"""What did you eat for breakfast: """)
else:
    breakfastSize = 0
    breakfastNutrition = 'na'
    breakfastTime = 'na'
    breakfastItem = 'no breakfast'
lunch = raw_input(
"""Did you eat lunch? (y/n): """)
if lunch == 'y':
    lunchSize = int(raw_input(
"""Rate the size of your lunch (1=handful, 7=main course w/ 2 sides, 10=stuffed): """))
    lunchNutrition = int(raw_input(
"""Rate the nutrition of your lunch (1=really unhealthy, 10=super healthy): """))
    lunchTime = float(raw_input(
"""What time did you start lunch? (army time decimal): """))
    lunchItem = raw_input(
"""What did you eat for lunch?: """)
else:
    lunchSize = 0
    lunchNutrition = 'na'
    lunchTime = 'na'
    lunchItem = 'no lunch'  
dinner = raw_input(
"""Did you eat Dinner? (y/n): """)
if dinner == 'y':
    dinnerSize = int(raw_input(
"""Rate the size of your dinner (1=handful, 7=main course w/ 2 sides, 10=stuffed): """))
    dinnerNutrition = int(raw_input(
"""Rate the nutrition of your dinner (1=really unhealthy, 10=super healthy): """))
    dinnerTime = float(raw_input(
"""What time did you start dinner? (army time decimal): """))
    dinnerItem = raw_input(
"""What did you eat for dinner?: """)
else:
    dinnerSize = 0
    dinnerNutrition = 'na'
    dinnerTime = 'na'
    dinnerItem = 'no dinner'    
snack = int(raw_input(
"""How many times did you snack?: """))
snackSize = []
snackNutrition = []
snackTime = []
snackItem = []
if snack == 0:
    snackSize = 0
    snackNutrition = 'na'
    snackTime = 'na'
    snackItem = 'na'
else:
    for i in range(snack):
        snckSize = int(raw_input(
"""Rate the size of your snack (1=handful, 7=sand which, 10=stuffed): """))
        snackSize.append(snckSize)
        snckNutr = int(raw_input(
"""Rate the nutrition of your snack (1=really unhealthy, 10=super healthy): """))
        snackNutrition.append(snckNutr)
        snckTime = float(raw_input(
"""What time did you snack? (army time decimal): """))
        snackTime.append(snckTime)
        snckItem = raw_input(
"""What did you eat for your snack?: """)
        snackItem.append(snckItem)

''''                    '''
''' Social Questions    '''
'''                     '''    
socialEncounters = int(raw_input(
"""How many social encounters did you have today?: """))
socialEncounterStart = []
socialEncounterTime = []
socialEncounterFun = []
socialEncounterValue = []
socialEncounterValuePerson = []
socialEncounterItem = []
if socialEncounters == 0:
    socialEncounterStart = 'na'
    socialEncounterTime = 0
    socialEncounterFun = 'na'
    socialEncounterValue = 'na'
    socialEncounterValuePerson = 'na'
    socialEncounterItem = 'na'
else:
    for i in range(socialEncounters):
        socEncStart = float(raw_input(
"""What time did this social encounter start (army time decimal)?: """))
        socialEncounterStart.append(socEncStart)
        socEncTime = float(raw_input(
"""How long did this social encounter last (hour decimal)?: """))
        socialEncounterTime.append(socEncTime)
        socEncFun = float(raw_input(
"""How much fun was this social encounter? (1= non-fun, 5=kinda pleasant, 10 = super fun/memorable)?: """))
        socialEncounterFun.append(socEncFun)
        socEncVal = raw_input(
"""Was anyone from you valuable people list involved? (y/n): """)
        socialEncounterValue.append(socEncVal)
        if socEncVal == 'y':
            socEncValPerson = raw_input(
"""Name of valuable person (fist last caps): """)
            socialEncounterValuePerson.append(socEncValPerson)
        else:
            socialEncounterValuePerson.append('na') 
        socEncItem = raw_input(
"""Describe social encounter: """)
        socialEncounterItem.append(socEncItem)
    
''''                    '''
'''  Exercise Questions '''
'''                     ''' 
exercise = raw_input(
"""Did you exercise? (y/n): """)
if exercise == 'y':
    exerciseTime = float(raw_input(
"""How long did you exercise? (Hours decimal): """))
    exerciseIntensity = int(raw_input(
"""Rate the intensity of your exercise (1=no sweat/soreness/breathing hard, 10= drenched in sweat / breathing hard/ very sore): """))
    exerciseType = raw_input(
"""Type either cardio, weights, or both: """)
    exerciseItem = raw_input(
"""Describe your exercise: """)
else:
    exerciseTime = 0
    exerciseIntensity = 0
    exerciseType = 'na'
    exerciseItem = 'na'

''''                    '''
''' Drug Questions      '''
'''                     '''  
weed = raw_input(
"""Did you smoke weed? (y/n): """)
if weed == 'y':
    weedAmount = float(raw_input(
"""How much weed did you smoke (grams)?: """))
else:
    weedAmount = 0
alcohol = raw_input(
"""Did you drink alcohol? (y/n): """)
if alcohol == 'y':
    alcoholAmount = float(raw_input(
"""How much alcohol did you drink (standard drinks)?: """))
else:
    alcoholAmount = 0
caffeine = raw_input(
"""Did you drink caffeine? (y/n): """)
if caffeine == 'y':
    caffeineAmount = float(raw_input(
"""How much alcohol did you drink (standard drinks)?: """))
else:
    caffeineAmount = 0

''''                    '''
''' Relaxation Questions'''
'''                     '''     
relax = int(raw_input(
"""How many relaxation events did you have today?: """))
relaxTime = []
relaxItem = []
if relax == 0:
    relaxTime = 0
    relaxItem = 'na' 
else:  
    for i in range(relax):
        relItem = raw_input(
"""How did you relax?: """)
        relaxItem.append(relItem)
        relTime = float(raw_input(
"""How long did you do this relaxation activity? (hours decimal): """))
        relaxTime.append(relTime)

''''                    '''
''' Meditation Questions'''
'''                     ''' 
meditate = raw_input(
"""Did you meditate today? (y/n): """)
if meditate == 'y':
    meditateTime = float(raw_input(
"""How long did you meditate? (hours decimal): """))
else:
    meditateTime = 0
    
''''                    '''
'''     Sex Questions   '''
'''                     ''' 
sex = int(raw_input(
"""How many times did you have sex today? (blowjobs and grinding count): """))
masturbation = int(raw_input(
"""How many times did you masturbate today? """))
fantasize = float(raw_input(
"""How long did you spend looking at girls online? (decimal hour) """))
porn = float(raw_input(
"""How long did you spend looking at porn videos? (decimal hour) """))
    
''''                    '''
''' General Questions   '''
'''                     ''' 
plan = raw_input(
"""Did you plan your day in the morning? (y/n): """)
if plan == 'y':
    planPercent = int(raw_input(
"""What percentage of day did you stick to plan? (int): """))
else:
    planPercent = 0
toDoListItems = int(raw_input(
"""How many items were on your to do list? (int): """))
toDoListComplete = int(raw_input(
"""How many items did you remove from your to do list? (int): """))
toDoListAdd = int(raw_input(
"""How many items did you add to tomorrows to do list? (int): """))
satisfaction = int(raw_input(
"""Rate your satisfaction for the day? (1=very unsatisfied, 10=very satisfied) : """))       
happy = int(raw_input(
"""Rate your general happiness? (1=very unhappy, 10=very happy) : """))
stress = int(raw_input(
"""Rate your general stress? (1=stress free, 10=very stressed) : """))
productivity = int(raw_input(
"""Rate your general productivity? (1=not at all productive, 10=very productive) : """))

'''                     '''
''' Append daily data   '''
'''                     '''

savePath = '/Users/joshmcmenemy/Dropbox/College/Philosophy/LifeData'
variablesStr = ['date', 'bedTime', 'wakeTime', 'sleepTime', 'nap', 'napTime', 'napStart', 'napEnd', 'breakfast', 'breakfastSize', 'breakfastNutrition', 'breakfastTime', 'breakfastItem', 'lunch', 'lunchSize', 'lunchNutrition', 'lunchTime', 'lunchItem', 'dinner', 'dinnerSize', 'dinnerNutrition', 'dinnerTime', 'dinnerItem', 'snack', 'snackSize', 'snackNutrition', 'snackTime', 'snackItem', 'socialEncounters', 'socialEncounterStart', 'socialEncounterTime', 'socialEncounterFun', 'socialEncounterValue', 'socialEncounterValuePerson', 'socialEncounterItem', 'exercise', 'exerciseTime', 'exerciseIntensity', 'exerciseType', 'exerciseItem', 'weed', 'weedAmount', 'alcohol', 'alcoholAmount', 'relax', 'relaxTime', 'relaxItem', 'meditate', 'meditateTime', 'sex', 'masturbation', 'fantasize', 'porn', 'plan', 'planPercent', 'toDoListItems', 'toDoListComplete', 'toDoListAdd', 'satisfaction', 'happy', 'stress', 'productivity']
variables = [date, bedTime, wakeTime, sleepTime, nap, napTime, napStart, napEnd, breakfast, breakfastSize, breakfastNutrition, breakfastTime, breakfastItem, lunch, lunchSize, lunchNutrition, lunchTime, lunchItem, dinner, dinnerSize, dinnerNutrition, dinnerTime, dinnerItem, snack, snackSize, snackNutrition, snackTime, snackItem, socialEncounters, socialEncounterStart, socialEncounterTime, socialEncounterFun, socialEncounterValue, socialEncounterValuePerson, socialEncounterItem, exercise, exerciseTime, exerciseIntensity, exerciseType, exerciseItem, weed, weedAmount, alcohol, alcoholAmount, relax, relaxTime, relaxItem, meditate, meditateTime, sex, masturbation, fantasize, porn, plan, planPercent, toDoListItems, toDoListComplete, toDoListAdd, satisfaction, happy, stress, productivity]

print 'str', len(variables)
print 'var', len(variablesStr)
c = 0
while c <= len(variables)-1:
    completeName = os.path.join(savePath, variablesStr[c] +'.txt')         
    file1 = open(completeName, 'a')
    file1.write(str(variables[c]))
    file1.write('\n')
    file1.close()
    c = c + 1

print 'Daily data successfully collected. Have a good night =)'
if __name__ == '__main__':
    pass
