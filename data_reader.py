import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

#open the file
with open('SampleRecords.txt') as f:
    contents = f.read()

column_names = contents[:contents.find('|RECORD ACTION INDICATOR') + len('|RECORD ACTION INDICATOR')].split('|')
data_inputs = contents[contents.find('|RECORD ACTION INDICATOR') + len('|RECORD ACTION INDICATOR'):].split('|')
cleaned_inputs = []
for word in data_inputs:
    cleaned_inputs.append(word.strip())

#clean data
data_inputs = cleaned_inputs

#save column_names into a list
lst_data = []
with open('real_estate_sample_data.csv', 'w') as file:
    # 2. Create a CSV writer
    writer = csv.writer(file)
    # 3. Write data to the file
    writer.writerow(column_names)
    for i in range(0,len(data_inputs),len(column_names)-1):
        #add to a pandas dataframe
        lst_data.append(data_inputs[i:i+len(column_names)-1])
        writer.writerow(data_inputs[i:i+len(column_names)-1])


lst_data.pop(-1)
column_names.pop(-1)
rel_data = pd.DataFrame(lst_data, columns = column_names)
print(rel_data.head())




# Creating plot
plt.boxplot(rel_data["LAND SQUARE FOOTAGE"])

# show plot
plt.show()




