import pandas as pd
import matplotlib.pyplot as plt

# taking data from file
data = pd.read_csv('vaccinated_per_day.csv')
data = data.iloc[:,:].values

# creating bar chart
plt.bar(data[:,0], data[:,1])
plt.xticks(rotation=90)
plt.ylabel('Average vaccinated population per day [%]')
plt.title('Population vaccinated daily by countries')
plt.show()