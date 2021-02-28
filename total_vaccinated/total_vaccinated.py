import pandas as pd
import matplotlib.pyplot as plt

# taking data from file
data = pd.read_csv('total_vaccinated.csv')
data = data.iloc[:,:].values

# creating bar chart
plt.bar(data[:,0], data[:,1], width=1, align='center', label='total vaccinations')
plt.bar(data[:,0], data[:,2], width=1, align='center', label='total vaccinated people')
plt.bar(data[:,0], data[:,3], width=1, align='center', label='total fully vaccinated people')
plt.title('Vaccinations in countries')
plt.ylabel('number of vaccination or people')
plt.xticks(rotation=90)
plt.legend()
plt.show()