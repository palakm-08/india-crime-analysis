import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = os.path.join(os.path.dirname(__file__), "crime_dataset_india.csv")
crime = pd.read_csv(file_path)



#---------->Total Reported Crimes per City<----------

crime_city = crime.groupby('City')['Report Number'].count().reset_index().sort_values(by = 'Report Number', ascending = False)
crime_city

cities = crime_city['City']
reports = crime_city['Report Number']

cities = cities[::-1]
reports = reports[::-1]

plt.figure(figsize=(10, 6))
bars = plt.barh(cities, reports, color='indianred')

for bar in bars:
    plt.text(bar.get_width() + 50, bar.get_y() + bar.get_height()/2,
             str(bar.get_width()), va = 'center')

plt.xlabel('Number of Crime Reports')
plt.ylabel('Cities')
plt.title('Crime Reports by City')
plt.tight_layout()
plt.show()



#------------>Year-wise Crime Trend<----------
crime['Year'] = pd.to_datetime(crime['Date of Occurrence'], errors = 'coerce').dt.year
most_crime_year = crime.groupby('Year')['Report Number'].count().reset_index().sort_values(by = 'Report Number', ascending = False)
most_crime_year

fig, ax1 = plt.subplots()






#-------->Delhi crime-rate over years<-----------

delhi_crime = crime[crime['City'] == 'Delhi']
delhi_crime_rate = delhi_crime.groupby('Year')['Report Number'].count().reset_index()
delhi_crime_rate

x = delhi_crime_rate['Year']
y = delhi_crime_rate['Report Number']

maxi = np.max(y)
maxi_index = np.argmax(y)
max_year = x[maxi_index]

plt.figure(figsize=(10, 5))
plt.plot(x, y, marker="o", markersize = 10, label="Delhi Crime-Rate")
plt.title("Delhi Crime-Rate Over Years", fontdict={'fontsize' : 18})
plt.xlabel("Years", fontdict={'fontsize' : 14})
plt.ylabel("No. Of Crimes" , fontdict={'fontsize' : 14})
plt.xticks(x)


plt.annotate(
    f"Highest cases : {maxi}",
    xy=(max_year, maxi),
    xytext=(max_year + 1, maxi + 0.5),
    arrowprops= dict(arrowstyle = '->'),
    fontsize = 10,
    color = '#184452'
)

plt.legend()
plt.grid(True, alpha = 0.7, linestyle = '--')
plt.show()




#--------------->Which Gender is Most Affected by Crime in India?<------------------
victim_gender = crime.groupby('Victim Gender')['Report Number'].count().reset_index().sort_values(by = 'Report Number', ascending=False)
victim_gender

x = victim_gender['Victim Gender']
y = victim_gender['Report Number']
plt.figure(figsize = (8, 4), dpi = 100)

plt.bar(x, y, color='#1a3d75')
plt.xlabel('Gender')
plt.ylabel('No. Of Crimes')
plt.title('Crime Victim Count by Gender in India (2020–2024)', fontdict={'fontsize' : 16})
plt.show()




#----------->Monthly Crime Counts by Year in India (2020–2023)<--------
import calendar

crime['Month'] = pd.to_datetime(crime['Date of Occurrence']).dt.month
lt_2024 = crime[crime['Year'] < 2024]
crime_month = lt_2024.groupby('Month')['Report Number'].count().reset_index()
crime_month

x = crime_month['Month']
y = crime_month['Report Number']
plt.figure(figsize = (9, 6), dpi = 100)

plt.bar(x, y, color='#15694d')

month_names = [calendar.month_name[m] for m in x]
plt.xticks(ticks=x, labels=month_names, rotation=45)

plt.xlabel('Months')
plt.ylabel('No. Of Crimes')
plt.title('Monthly Crime Counts by Year in India (2020–2023)', fontdict={'fontsize' : 16})
plt.show()
