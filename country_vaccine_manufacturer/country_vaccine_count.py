import pandas as pd
import matplotlib.pyplot as plt

# taking data from csv file
file = pd.read_csv('country_vaccine.csv')
vaccines = file.iloc[:,1]

#creating list of unique manufacturers
vac_set = set()
vac_list = list()

for record in vaccines:
  record = record.split(',')
  for r in record:
    r = ' '.join(r.split())
    vac_list.append(r)
    vac_set.add(r)

# counting countries that use certain vaccine
country_count = {k:vac_list.count(k) for k in vac_set}

# descending sorting count
country_count = {k: v for k, v in sorted(country_count.items(), key=lambda item: item[1], reverse=True)}

# creating bar chart with manufacturers and count
plt.bar(range(len(vac_set)), list(country_count.values()), align='center')
plt.xticks(range(len(vac_set)), country_count.keys())
plt.xlabel('Manufacturer name')
plt.ylabel('Number of countries')
plt.title('Count of countries = f(manufacturer)')
plt.grid(axis='y')
plt.show()