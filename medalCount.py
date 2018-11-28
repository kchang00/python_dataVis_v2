import csv
import matplotlib.pyplot as plt
# import numpy as np

# arrays

golds = []
silvers = []
bronzes = []
# need a place to put clean data set (categories)
# puts headers here
categories = []

with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            # gets rid of headers
            # append tells cpu to add info into categories
            categories.append(row)
            line_count += 1
        else:
            # all we want to parse is column # (start @ 0)
            if row[7] == "Gold":
                golds.append(row[7])
            elif row[7] == "Silver":
                silvers.append(row[7])
            else:
                bronzes.append(row[7])
            line_count += 1

print('processed', line_count, 'rows of data')
print('gold medals won:', len(golds))
print('silver medals won:', len(silvers))
print('bronze medals won:', len(bronzes))

total_medals = golds + silvers + bronzes

total_golds = int(len(golds) / len(total_medals) * 100)  # gets percentages
print(total_golds)

total_silvers = int(len(silvers) / len(total_medals) * 100)
print(total_silvers)

total_bronzes = 100 - (total_golds + total_silvers)
print(total_bronzes)

# pie chart 

labels = 'Gold', 'Silver', 'Bronze'
sizes = [(total_golds), (total_silvers), (total_bronzes)]
colors = ['#FFDF00', '#C0C0C0', '#CD7F32']
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode = explode, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 140)
plt.axis('equal')

plt.legend(labels, loc = 1)
plt.title('Percentage of Medals Won')
plt.xlabel('1924 - 2014 Winter Olympics: Total Medal Results')
plt.show()
