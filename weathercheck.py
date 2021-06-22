import requests
#import os
from datetime import datetime

api_key = '1a9d34d5c0f76121717b26d03407ce63'

location = input("Enter the city name: ")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp =((api_data['main']['temp']) - 273.15)
desc =api_data['weather'][0]['description']
hmdt =api_data['main']['humidity']
wspd =api_data['wind']['speed']
date =datetime.now().strftime("%d %b %Y")
time =datetime.now().strftime("%I:%M:%S %p")
print ("------------------------------------------------------------")
print ("Weather Stats for - "+location.upper())
print ("------------------------------------------------------------")
print("DATE: "+date)
print("TIME: "+time)
print("Current Temperature   : {:.2f} deg C".format(temp))
print("Current Weather Desc  :",desc)
print("Current Humidity      :",hmdt, '%')
print("Current Wind Speed    :",wspd ,'kmph')

count=0
try:
    f=open('Weather_Report.txt','r')
    for i in f.readlines():
        count += 1
except:
    pass
recno = count / 11
f=open('Weather_Report.txt','a+')
f.write("-------------------------RECORD "+str(recno+1)+'-------------------------\n')
f.write("------------------------------------------------------------\n")
f.write("DATE: "+date+'\n')
f.write("TIME: " + time+'\n')
f.write("Current Temperature   : {:.2f} deg C".format(temp)+'\n')
f.write("Current Weather Desc  :" + desc+'\n')
f.write("Current Humidity      :" + str(hmdt) + '%\n')
f.write("Current Wind Speed    :" + str(wspd) + 'kmph\n')
f.write("\n\n")
f.close()
