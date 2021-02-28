import pandas as pd
import matplotlib.pyplot as plt

# taking data from file
data = pd.read_csv('vaccinated_percent.csv')
data = data.iloc[:,:].values

# creating bar chart
plt.bar(data[:,0], data[:,1])
plt.xticks(rotation=90)
plt.ylabel('Vaccinated population [%]')
plt.title('Population vaccinated by countries')
plt.show()