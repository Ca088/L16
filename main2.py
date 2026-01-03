import random
import time

def getRandomDate(startDate,endDate):
    print('Printing random modules between ',startDate,"and",endDate)
    randomgenerator=random.random()
    dateFormat='%m/%d/%Y'

    startTime=time.mktime(time.strptime(startDate,dateFormat))
    endTime=time.mktime(time.strptime(endDate,dateFormat))

    randomTime=startTime+randomgenerator*(endTime-startTime)
    randomdate=time.strftime(dateFormat,time.localtime(randomTime))
    return randomdate 
print("Random date=",getRandomDate("1/1/2016","12/12/2018"))
