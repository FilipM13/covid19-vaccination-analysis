<h1 align="center">Analysis of Covid-19 vaccination data</h1>

## Which country is using what vaccine?
<small>Files corresponding to this part are stored in country_vaccine_manufacturer folder</small>

Using MySQL and country_vaccination.csv I exported distinct pairs of countries and vaccines (country-vaccine.sql).
Results were exported into country-vaccine.csv file. From this file I created table and bar chart below.
Most popular vaccine is manufactured by Pfizer/BioNTech, it's used in 45 countries.

| country              | vaccine manufacturer                                                               |
|----------------------|------------------------------------------------------------------------------------|
| Albania              | Pfizer/BioNTech                                                                    |
| Argentina            | Sputnik V                                                                          |
| Austria              | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| Belgium              | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| Brazil               | Oxford/AstraZeneca, Sinovac                                                        |
| Bulgaria             | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| Cayman Islands       | Pfizer/BioNTech                                                                    |
| Chile                | Pfizer/BioNTech, Sinovac                                                           |
| Croatia              | Pfizer/BioNTech                                                                    |
| Czechia              | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| Denmark              | Moderna, Pfizer/BioNTech                                                           |
| England              | Oxford/AstraZeneca, Pfizer/BioNTech                                                |
| Estonia              | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| Faeroe Islands       | Pfizer/BioNTech                                                                    |
| Finland              | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| France               | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| Germany              | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| Gibraltar            | Pfizer/BioNTech                                                                    |
| Greece               | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| Hungary              | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech, Sinopharm/Beijing, Sputnik V         |
| Iceland              | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| India                | Covaxin, Oxford/AstraZeneca                                                        |
| Indonesia            | Sinovac                                                                            |
| Ireland              | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| Isle of Man          | Oxford/AstraZeneca, Pfizer/BioNTech                                                |
| Israel               | Moderna, Pfizer/BioNTech                                                           |
| Italy                | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| Latvia               | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| Lithuania            | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| Luxembourg           | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| Malta                | Pfizer/BioNTech                                                                    |
| Mexico               | Oxford/AstraZeneca, Pfizer/BioNTech, Sputnik V                                     |
| Morocco              | Oxford/AstraZeneca, Sinopharm/Beijing                                              |
| Northern Ireland     | Oxford/AstraZeneca, Pfizer/BioNTech                                                |
| Norway               | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| Oman                 | Oxford/AstraZeneca, Pfizer/BioNTech                                                |
| Poland               | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| Portugal             | Moderna, Pfizer/BioNTech                                                           |
| Romania              | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| Scotland             | Oxford/AstraZeneca, Pfizer/BioNTech                                                |
| Serbia               | Pfizer/BioNTech, Sinopharm/Beijing, Sputnik V                                      |
| Seychelles           | Oxford/AstraZeneca, Sinopharm/Beijing                                              |
| Slovakia             | Pfizer/BioNTech                                                                    |
| Slovenia             | Oxford/AstraZeneca, Pfizer/BioNTech                                                |
| South Africa         | Johnson&Johnson                                                                    |
| Spain                | Moderna, Oxford/AstraZeneca, Pfizer/BioNTech                                       |
| Sweden               | Oxford/AstraZeneca, Pfizer/BioNTech                                                |
| Switzerland          | Moderna, Pfizer/BioNTech                                                           |
| Turkey               | Sinovac                                                                            |
| United Arab Emirates | Oxford/AstraZeneca, Pfizer/BioNTech, Sinopharm/Beijing, Sinopharm/Wuhan, Sputnik V |
| United Kingdom       | Oxford/AstraZeneca, Pfizer/BioNTech                                                |
| United States        | Moderna, Pfizer/BioNTech                                                           |
| Wales                | Oxford/AstraZeneca, Pfizer/BioNTech                                                |

![country_vaccine_count](https://raw.githubusercontent.com/FilipM13/covid19-vaccination-analysis/main/country_vaccine_manufacturer/country_vaccine_count.png)  
<small>Bar chart generated with count_vaccine_country.py</small>

## In which country the vaccination programme is more advanced?

## Where are vaccinated more people per day in terms of percent from entire population?
<small>Files corresponding to this part are stored in vaccinated_per_day folder</small>

Based on main data source Gibraltar vaccinates the largest percent of population per day.
I took most important information by using vaccinated_per_day.sql which takes average value of people daily 
vaccinations per million for each country from main data source.

| country              | average population vaccination per day [%]          |
|----------------------|-----------------------------------------------------|
| Gibraltar            | 2.28                                                |
| Seychelles           | 1.75                                                |
| Israel               | 1.44                                                |
| Cayman Islands       | 0.69                                                |
| Wales                | 0.61                                                |
| United Arab Emirates | 0.6                                                 |
| Scotland             | 0.55                                                |
| England              | 0.54                                                |
| Isle of Man          | 0.54                                                |
| United Kingdom       | 0.53                                                |
| Serbia               | 0.51                                                |
| Northern Ireland     | 0.49                                                |
| United States        | 0.4                                                 |
| Morocco              | 0.39                                                |
| Turkey               | 0.36                                                |
| Chile                | 0.36                                                |
| Malta                | 0.36                                                |
| Faeroe Islands       | 0.34                                                |
| Switzerland          | 0.22                                                |
| Iceland              | 0.22                                                |
| Norway               | 0.17                                                |
| Sweden               | 0.17                                                |
| Greece               | 0.17                                                |
| Estonia              | 0.17                                                |
| Romania              | 0.16                                                |
| Finland              | 0.16                                                |
| Denmark              | 0.16                                                |
| Slovakia             | 0.16                                                |
| Poland               | 0.16                                                |
| Lithuania            | 0.16                                                |
| Hungary              | 0.16                                                |
| Ireland              | 0.15                                                |
| Portugal             | 0.15                                                |
| France               | 0.14                                                |
| Spain                | 0.14                                                |
| Belgium              | 0.14                                                |
| Austria              | 0.14                                                |
| Slovenia             | 0.14                                                |
| Luxembourg           | 0.13                                                |
| Germany              | 0.13                                                |
| Croatia              | 0.12                                                |
| Czechia              | 0.11                                                |
| Italy                | 0.11                                                |
| Brazil               | 0.11                                                |
| Latvia               | 0.05                                                |
| Bulgaria             | 0.05                                                |
| Argentina            | 0.03                                                |
| Mexico               | 0.03                                                |
| Oman                 | 0.03                                                |
| India                | 0.03                                                |
| Indonesia            | 0.02                                                |
| Albania              | 0.01                                                |
| South Africa         | 0.01                                                |

![vaccinated_per_day](https://raw.githubusercontent.com/FilipM13/covid19-vaccination-analysis/main/vaccinated_per_day/vaccinated_per_day.png)
<small>Bar chart generated with vaccinated_per_day.py</small>

## What country has vaccinated a larger percent from its population?
<small>Files corresponding to this part are stored in vaccinated_percent folder</small>

Based on main data source Gibraltar vaccinated the largest percent of population.
I took most important information by using vaccinated_percent.sql which takes maximum value of people
vaccinated per hundred for each country from main data source.

| country              | vaccinated population [%]          |
|----------------------|------------------------------------|
| Gibraltar            | 64.09                              |
| Israel               | 53.87                              |
| Seychelles           | 44.19                              |
| United Arab Emirates | 35.19                              |
| England              | 28.83                              |
| Wales                | 28.62                              |
| United Kingdom       | 28.25                              |
| Scotland             | 28.24                              |
| Northern Ireland     | 26.68                              |
| Cayman Islands       | 19.34                              |
| Chile                | 17.21                              |
| Isle of Man          | 15.99                              |
| United States        | 14.11                              |
| Serbia               | 13.02                              |
| Malta                | 11.38                              |
| Morocco              | 9.02                               |
| Faeroe Islands       | 8.57                               |
| Turkey               | 8                                  |
| Denmark              | 6.49                               |
| Finland              | 6.26                               |
| Switzerland          | 6.1                                |
| Lithuania            | 5.96                               |
| Norway               | 5.88                               |
| Hungary              | 5.83                               |
| Slovenia             | 5.79                               |
| Iceland              | 5.74                               |
| Slovakia             | 5.52                               |
| Greece               | 5.34                               |
| Portugal             | 5.28                               |
| Estonia              | 5.17                               |
| Spain                | 5.05                               |
| Ireland              | 4.84                               |
| Poland               | 4.82                               |
| Sweden               | 4.69                               |
| Romania              | 4.63                               |
| Germany              | 4.63                               |
| Italy                | 4.46                               |
| Luxembourg           | 4.17                               |
| France               | 4.14                               |
| Belgium              | 3.98                               |
| Czechia              | 3.8                                |
| Austria              | 3.77                               |
| Croatia              | 3.31                               |
| Brazil               | 2.99                               |
| Bulgaria             | 2.41                               |
| Latvia               | 2.32                               |
| Argentina            | 1.37                               |
| Mexico               | 1.33                               |
| Oman                 | 0.95                               |
| India                | 0.84                               |
| Indonesia            | 0.58                               |
| South Africa         | 0.11                               |
| Albania              | 0.08                               |

![vaccinated_percent](https://raw.githubusercontent.com/FilipM13/covid19-vaccination-analysis/main/vaccinated_percent/vaccinated_percent.png)
<small>Bar chart generated with vaccinated_percent.py</small>

## What country has vaccinated more people?
<small>Files corresponding to this part are stored in total_vaccinated folder</small>

According to data United States vaccinated more people than any other country. 
They also fully vaccinated the largest number of people and therefore used the largest number of vaccines.
I took most important information by using total_vaccinated.sql which takes maximum value of total vaccinations,
people vaccinated and people fully vaccinated for each country from main data source.

| country              | used vaccinations       | vaccinated people      | fully vaccinated people      |
|----------------------|-------------------------|------------------------|------------------------------|
| United States        | 70454064                | 47184199               | 22613359                     |
| United Kingdom       | 19913592                | 19177555               | 736037                       |
| England              | 16785841                | 16227104               | 558737                       |
| India                | 13756940                | 11552857               | 2204083                      |
| Turkey               | 8298805                 | 6745147                | 1553658                      |
| Brazil               | 8101787                 | 6346769                | 1755018                      |
| Israel               | 7957787                 | 4663028                | 3294759                      |
| Germany              | 5910537                 | 3881490                | 2029047                      |
| United Arab Emirates | 5668264                 | 3480415                | 2187849                      |
| France               | 4298573                 | 2808490                | 1490083                      |
| Italy                | 4074575                 | 2696588                | 1377987                      |
| Spain                | 3605635                 | 2361852                | 1243783                      |
| Morocco              | 3424295                 | 3327858                | 96437                        |
| Chile                | 3345027                 | 3289086                | 55941                        |
| Poland               | 2759436                 | 1824654                | 934782                       |
| Indonesia            | 2449451                 | 1583581                | 865870                       |
| Mexico               | 2271032                 | 1708721                | 562311                       |
| Scotland             | 1608269                 | 1542929                | 65340                        |
| Romania              | 1506033                 | 890068                 | 615965                       |
| Serbia               | 1393086                 | 886086                 | 507000                       |
| Wales                | 982396                  | 902334                 | 80062                        |
| Argentina            | 903915                  | 620635                 | 283280                       |
| Greece               | 857306                  | 556380                 | 300926                       |
| Hungary              | 808008                  | 563601                 | 244407                       |
| Portugal             | 797005                  | 538636                 | 258369                       |
| Belgium              | 757229                  | 461060                 | 296169                       |
| Switzerland          | 748791                  | 527979                 | 220812                       |
| Sweden               | 720631                  | 474028                 | 246603                       |
| Czechia              | 644321                  | 406410                 | 237911                       |
| Austria              | 582135                  | 339470                 | 211897                       |
| Denmark              | 556878                  | 375794                 | 181084                       |
| Northern Ireland     | 537086                  | 505188                 | 31898                        |
| Norway               | 468344                  | 318722                 | 149622                       |
| Slovakia             | 433998                  | 301488                 | 132510                       |
| Finland              | 426806                  | 347082                 | 79724                        |
| Ireland              | 373280                  | 238841                 | 134439                       |
| Lithuania            | 234959                  | 162148                 | 72811                        |
| Bulgaria             | 204439                  | 167258                 | 37181                        |
| Croatia              | 194267                  | 135756                 | 58511                        |
| Slovenia             | 171605                  | 120377                 | 51228                        |
| Estonia              | 96980                   | 68629                  | 28351                        |
| Malta                | 73644                   | 50249                  | 23395                        |
| Oman                 | 67660                   | 48641                  | 19019                        |
| Seychelles           | 65060                   | 43461                  | 21599                        |
| South Africa         | 63648                   | 63648                  | 63648                        |
| Latvia               | 60732                   | 43743                  | 16989                        |
| Luxembourg           | 36071                   | 26089                  | 9982                         |
| Gibraltar            | 34600                   | 21591                  | 13009                        |
| Iceland              | 32157                   | 19593                  | 12564                        |
| Cayman Islands       | 20468                   | 12710                  | 7758                         |
| Isle of Man          | 19884                   | 13600                  | 6284                         |
| Faeroe Islands       | 6713                    | 4190                   | 2523                         |
| Albania              | 3049                    | 2438                   | 611                          |

![total_vaccinated](https://raw.githubusercontent.com/FilipM13/covid19-vaccination-analysis/main/total_vaccinated/total_vaccinated.png)
<small>Bar chart generated with total_vaccinated.py</small>

## Approximate expense paid until 25.02.2021 for vaccines for each country.  
"Pfizer: $20 per dose."  
"Moderna: $10 to $50 per dose."  
"AstraZeneca: under $4 per dose."  
"The cost of one dose of the Sputnik V vaccine for international markets will be less than $10."  
 
If country didn't use any of vaccines listed above then it would not appear on the graph. 
Else price for single vaccine is average of vaccine it used.

![paid_expenses](https://raw.githubusercontent.com/FilipM13/covid19-vaccination-analysis/main/paid_expenses/paid_expenses.png)
<small>Bar chart generated with paid_expenses.py</small>

## Approximate total expense  for vaccines for each country.

### Sources:
kaggle task with data: https://www.kaggle.com/gpreda/covid-world-vaccination-progress/tasks  
'main data source' refers to country_vaccinations.csv file in the main directory.  
Vaccine prices:  
https://sputnikvaccine.com/newsroom/pressreleases/the-cost-of-one-dose-will-be-less-than-10-for-international-markets/  
https://observer.com/2020/11/covid19-vaccine-price-pfizer-moderna-astrazeneca-oxford  