#%%
import math
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import neighbors as nb
import numpy as np

data = None

def visualize(df):
    # Visualize data, colored based on sex
    for i in range(0, len(df.values)):
        color = ""
        
        if df.iloc[i]["sex"] == "M":
            color = "blue"
        elif df.iloc[i]["sex"] == "F":
            color = "red"
        else:
            print("Unspecified sex")
            color = "black"
            
        plt.scatter(
            x = df.iloc[i]["age"], 
            y = df.iloc[i]["wage"], 
            color = color,
            linewidths = 5
            )

    plt.xlabel("Age")
    plt.ylabel("Wage")
    plt.legend(["Female", "Male"])
    plt.show()

# Load data into a Pandas DataFrame from CSV
with open(file = "test data/employees.csv") as f:
    dict = pd.read_csv(f)
    data = pd.DataFrame.from_dict(dict)

# Manage non-data
wage_sum_no_na = 0
non_na_wages = 0
for i in range(0, len(data.values)):
    if data.iloc[i].notna()["wage"]:
        wage_sum_no_na = wage_sum_no_na + float(data.iloc[i]["wage"])
        non_na_wages = non_na_wages + 1

mean_wage = float(wage_sum_no_na/non_na_wages).__round__(0)
print("Mean wage of workers is {}".format(mean_wage))
        
data = data.fillna(mean_wage)
    
visualize(data)

# Add a new value to the dataframe without specifiying the sex
new_value = {
    "ï»¿id" : [21], 
    "fname" : ["Alex"], 
    "sname" : ["Kittering"], 
    "department" : ["Community"], 
    "age" : [40], 
    "wage" : [50000.0], 
    "sex" :["UNKNOWN"]
    }

new_value = pd.DataFrame.from_dict(new_value)

data = pd.concat([data, new_value], ignore_index = True, axis = 0)

visualize(data)

# Determine Euclidean distance between test point and K-neighbouring points
def KNN(df, test_point, k = 1):
    
    if k <= 0:
        k = 1
    
    sexes = []
    euclidean_distances = []
    
    for i in range(0, len(df.values)):
        if df.iloc[i]["ï»¿id"] != test_point.iloc[0]["ï»¿id"]:
            sexes.append(df.iloc[i]["sex"])
            
            dx = abs(df.iloc[i]["age"] - test_point.iloc[0]["age"])
            dy = abs(df.iloc[i]["wage"] - test_point.iloc[0]["wage"])
            euclidean_dist = np.sqrt(dx**2 + dy**2)
            
            print("Euclidean distances between point {} and the test point is {}".format(i, euclidean_dist))

            euclidean_distances.append(euclidean_dist)
    
    neighbours = {"sex" : sexes, "euclidean_dist" : euclidean_distances}
    neighbours = pd.DataFrame.from_dict(neighbours)
    neighbours = neighbours.sort_values(by = "euclidean_dist")
    
    print(neighbours)
    
    k_nearest_neighbours = []
    for i in range(0, k):
        k_nearest_neighbours.append(neighbours.iloc[i]["sex"])
    
    return k_nearest_neighbours  
        

# Retreive the k-nearest neighbours to the test point
k_nearest_neighbours = KNN(data, new_value, k = 7)

print(k_nearest_neighbours)

for i in range(0, len(k_nearest_neighbours)):
    male = 0
    female = 0
    if k_nearest_neighbours[i] == "M":
        male = male + 1
    elif k_nearest_neighbours[i] == "F":
        female = female + 1

# Determine category based on majority of neighbours. 
if male > female:
    new_value["sex"].update("M")
elif male < female:
    new_value["sex"].update("F")

print(new_value)

data.iloc[20] = new_value

print(data)

visualize(data)


# %%
