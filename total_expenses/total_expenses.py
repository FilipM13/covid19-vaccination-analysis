import pandas as pd
import matplotlib.pyplot as plt

# taking data from file
data = pd.read_csv('total_expenses.csv')
data = data.iloc[:,:].values

'''
"Pfizer: \$20 per dose."
"Moderna: \$10 to \$50 per dose."
"AstraZeneca: under \$4 per dose."
"The cost of one dose of the Sputnik V vaccine for international markets will be less than \$10."
More in README.md
If country didn't use any vaccine manufactured by companies listed above then it would not be taken to account.
Else country would get expense equal to total vaccinations multiplied by average price of all vaccines it uses and 
divided by percent of fully vaccinated population.
'''

vac_price = {'Pfizer':20, 'Moderna':30, 'AstraZeneca':4, 'Sputnik V':10}

price = {}
for n, v in enumerate(data[:,3]):
  country = data[n,0]
  vaccines = data[n,1]
  percent = data[n,2]
  temp_price = list()
  for manufacturer, pr in vac_price.items():
    if manufacturer in v:
      temp_price.append(pr)
  if len(temp_price) != 0:
    temp_price = sum(temp_price)/len(temp_price)
    price[country] = vaccines*temp_price/(percent/100)

plt.bar(price.keys(), price.values())
plt.xticks(rotation=90)
plt.ylabel('Total expenses in USD')
plt.title('Total expenses')
plt.show()
