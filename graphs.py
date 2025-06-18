import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = os.path.join(os.path.dirname(__file__), "crime_dataset_india.csv")
crime = pd.read_csv(file_path)


#------------>Year-wise Crime Trend<----------
crime['Year'] = pd.to_datetime(crime['Date of Occurrence'], errors = 'coerce').dt.year
most_crime_year = crime.groupby('Year')['Report Number'].count().reset_index().sort_values(by = 'Report Number', ascending = False)
most_crime_year

x = most_crime_year['Year']
y = most_crime_year['Report Number']

plt.figure(figsize=(8, 4))
plt.plot(x, y, marker = 'o', markersize = 10, label='Total Crimes')
plt.xlabel('Years', fontdict={'fontsize' : 14})
plt.ylabel('Total Crimes', fontdict={'fontsize' : 14})
plt.title('Year-wise Crime Trend', fontdict={'fontsize' : 18})
plt.xticks(x)

plt.legend(bbox_to_anchor = (1, 1))
plt.grid()
plt.show()




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

