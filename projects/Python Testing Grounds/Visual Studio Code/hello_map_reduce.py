#%%
import pandas as pd
import numpy as np
import os

#%%
def convert_to_numeric(df, column_name):
    # Create a buffer to store values converted to numeric form
    _list = []
    # Iterate through content of the specified column
    for i in range(0, len(df[column_name].values)):
        x = df.iloc[i][column_name]
        
        # If the value is NaN, convert it to an empty value of "0" for now...
        if x == np.nan or x.__contains__("n/a"):
            x = 0
        
        # If the value encountered is not an integer, convert it to one
        if type(x) != int:
            # Typecast value to an integer         
            try:
                x = int(x)
            except:
                print("Could not cast value \'{}\' to an integer. Setting to 0 instead.".format(x))
                x = 0
            
        # Append value to buffer
        _list.append(x)
    
    # Return buffer as output
    return _list

def find_difference_in_windspeed(df, current_wban, current_date):
    new_df = pd.DataFrame({" Wind Speed (kt)" : convert_to_numeric(df, " Wind Speed (kt)")})
    df.update(new_df)
    
    max_windspeed   = np.max(df[" Wind Speed (kt)"].values)
    min_windspeed   = np.min(df[" Wind Speed (kt)"].values)
    delta_windspeed = max_windspeed - min_windspeed
                    
    print("Difference in maximum windspeed {}kt and minimum windspeed {}kt for Wban: {}, Date: {}, is: {}kt".format(max_windspeed, min_windspeed, current_wban, current_date, delta_windspeed))

def find_daily_min_of_relative_humidity(df):
    pass

def find_corr_matrix(df):
    pass

def partition_by_wban_and_date(df):
    wban_partition_dict = {
        "Wban Number" :             [],
        " YearMonthDay" :           [],
        " Time" :                   [],
        " Station Type" :           [],
        " Maintenance Indicator" :  [],
        " Sky Conditions" :         [],
        " Visibility" :             [],
        " Weather Type" :           [],
        " Dry Bulb Temp" :          [],
        " Dew Point Temp" :         [],
        " Wet Bulb Temp" :          [],
        " % Relative Humidity" :    [],
        " Wind Speed (kt)" :        [],
        " Wind Direction" :         [],
        " Wind Char. Gusts (kt)" :  [],
        " Val for Wind Char." :     [],
        " Station Pressure" :       [],
        " Pressure Tendency" :      [],
        " Sea Level Pressure" :     [],
        " Record Type" :            [],
        " Precip. Total" :          []
        }
    
    i_lim = len(df["Wban Number"].values)
    for i in range(0, i_lim):
        this_wban = df.iloc[i]["Wban Number"]
        next_wban = None
        if i == i_lim - 1:
            pass
        else:
            next_wban = df.iloc[i+1]["Wban Number"]
        
        wban_partition_dict["Wban Number"]           .append(this_wban)
        wban_partition_dict[" YearMonthDay"]         .append(df.iloc[i][" YearMonthDay"])
        wban_partition_dict[" Time"]                 .append(df.iloc[i][" Time"])
        wban_partition_dict[" Station Type"]         .append(df.iloc[i][" Station Type"])
        wban_partition_dict[" Maintenance Indicator"].append(df.iloc[i][" Maintenance Indicator"])
        wban_partition_dict[" Sky Conditions"]       .append(df.iloc[i][" Sky Conditions"])
        wban_partition_dict[" Visibility"]           .append(df.iloc[i][" Visibility"])
        wban_partition_dict[" Weather Type"]         .append(df.iloc[i][" Weather Type"])
        wban_partition_dict[" Dry Bulb Temp"]        .append(df.iloc[i][" Dry Bulb Temp"])
        wban_partition_dict[" Dew Point Temp"]       .append(df.iloc[i][" Dew Point Temp"])
        wban_partition_dict[" Wet Bulb Temp"]        .append(df.iloc[i][" Wet Bulb Temp"])
        wban_partition_dict[" % Relative Humidity"]  .append(df.iloc[i][" % Relative Humidity"])
        wban_partition_dict[" Wind Speed (kt)"]      .append(df.iloc[i][" Wind Speed (kt)"])
        wban_partition_dict[" Wind Direction"]       .append(df.iloc[i][" Wind Direction"])
        wban_partition_dict[" Wind Char. Gusts (kt)"].append(df.iloc[i][" Wind Char. Gusts (kt)"])
        wban_partition_dict[" Val for Wind Char."]   .append(df.iloc[i][" Val for Wind Char."])
        wban_partition_dict[" Station Pressure"]     .append(df.iloc[i][" Station Pressure"])
        wban_partition_dict[" Pressure Tendency"]    .append(df.iloc[i][" Pressure Tendency"])
        wban_partition_dict[" Sea Level Pressure"]   .append(df.iloc[i][" Sea Level Pressure"])
        wban_partition_dict[" Record Type"]          .append(df.iloc[i][" Record Type"])
        wban_partition_dict[" Precip. Total"]        .append(df.iloc[i][" Precip. Total"])
        
        if this_wban != next_wban or i == i_lim:
            # If the subsequent Wban number is different from the current one
            # then the current one must be the last for the series.
            # Use the partition then wipe it for the next series.
            wban_partition_df = pd.DataFrame.from_dict(wban_partition_dict)
            # print(wban_partition_df)
            
            # Next, partition by date.
            date_partition_dict = {
                "Wban Number" :             [],
                " YearMonthDay" :           [],
                " Time" :                   [],
                " Station Type" :           [],
                " Maintenance Indicator" :  [],
                " Sky Conditions" :         [],
                " Visibility" :             [],
                " Weather Type" :           [],
                " Dry Bulb Temp" :          [],
                " Dew Point Temp" :         [],
                " Wet Bulb Temp" :          [],
                " % Relative Humidity" :    [],
                " Wind Speed (kt)" :        [],
                " Wind Direction" :         [],
                " Wind Char. Gusts (kt)" :  [],
                " Val for Wind Char." :     [],
                " Station Pressure" :       [],
                " Pressure Tendency" :      [],
                " Sea Level Pressure" :     [],
                " Record Type" :            [],
                " Precip. Total" :          []
                }
            
            j_lim = len(wban_partition_df["Wban Number"].values)
            for j in range(0, j_lim):
                this_date = wban_partition_df.iloc[j][" YearMonthDay"]
                next_date = None
                if j == j_lim - 1:
                    pass
                else:
                     next_date  = wban_partition_df.iloc[j+1][" YearMonthDay"]
                
                date_partition_dict["Wban Number"]           .append(wban_partition_df.iloc[j]["Wban Number"])
                date_partition_dict[" YearMonthDay"]         .append(this_date)
                date_partition_dict[" Time"]                 .append(wban_partition_df.iloc[j][" Time"])
                date_partition_dict[" Station Type"]         .append(wban_partition_df.iloc[j][" Station Type"])
                date_partition_dict[" Maintenance Indicator"].append(wban_partition_df.iloc[j][" Maintenance Indicator"])
                date_partition_dict[" Sky Conditions"]       .append(wban_partition_df.iloc[j][" Sky Conditions"])
                date_partition_dict[" Visibility"]           .append(wban_partition_df.iloc[j][" Visibility"])
                date_partition_dict[" Weather Type"]         .append(wban_partition_df.iloc[j][" Weather Type"])
                date_partition_dict[" Dry Bulb Temp"]        .append(wban_partition_df.iloc[j][" Dry Bulb Temp"])
                date_partition_dict[" Dew Point Temp"]       .append(wban_partition_df.iloc[j][" Dew Point Temp"])
                date_partition_dict[" Wet Bulb Temp"]        .append(wban_partition_df.iloc[j][" Wet Bulb Temp"])
                date_partition_dict[" % Relative Humidity"]  .append(wban_partition_df.iloc[j][" % Relative Humidity"])
                date_partition_dict[" Wind Speed (kt)"]      .append(wban_partition_df.iloc[j][" Wind Speed (kt)"])
                date_partition_dict[" Wind Direction"]       .append(wban_partition_df.iloc[j][" Wind Direction"])
                date_partition_dict[" Wind Char. Gusts (kt)"].append(wban_partition_df.iloc[j][" Wind Char. Gusts (kt)"])
                date_partition_dict[" Val for Wind Char."]   .append(wban_partition_df.iloc[j][" Val for Wind Char."])
                date_partition_dict[" Station Pressure"]     .append(wban_partition_df.iloc[j][" Station Pressure"])
                date_partition_dict[" Pressure Tendency"]    .append(wban_partition_df.iloc[j][" Pressure Tendency"])
                date_partition_dict[" Sea Level Pressure"]   .append(wban_partition_df.iloc[j][" Sea Level Pressure"])
                date_partition_dict[" Record Type"]          .append(wban_partition_df.iloc[j][" Record Type"])
                date_partition_dict[" Precip. Total"]        .append(wban_partition_df.iloc[j][" Precip. Total"])
                
                if this_date != next_date or j == j_lim:
                    # If the subsequent date is different from the current date, then
                    # we may take all the observations gathered thus far for the current
                    # Wban number and save them to a partition for the current date only.
                    date_partition_df = pd.DataFrame.from_dict(date_partition_dict)
                    
                    # Use partitioned data
                    find_difference_in_windspeed(date_partition_df, this_wban, this_date)
                    
                    # Wipe for next date partition
                    date_partition_dict["Wban Number"]           .clear()
                    date_partition_dict[" YearMonthDay"]         .clear()
                    date_partition_dict[" Time"]                 .clear()
                    date_partition_dict[" Station Type"]         .clear()
                    date_partition_dict[" Maintenance Indicator"].clear()
                    date_partition_dict[" Sky Conditions"]       .clear()
                    date_partition_dict[" Visibility"]           .clear()
                    date_partition_dict[" Weather Type"]         .clear()
                    date_partition_dict[" Dry Bulb Temp"]        .clear()
                    date_partition_dict[" Dew Point Temp"]       .clear()
                    date_partition_dict[" Wet Bulb Temp"]        .clear()
                    date_partition_dict[" % Relative Humidity"]  .clear()
                    date_partition_dict[" Wind Speed (kt)"]      .clear()
                    date_partition_dict[" Wind Direction"]       .clear()
                    date_partition_dict[" Wind Char. Gusts (kt)"].clear()
                    date_partition_dict[" Val for Wind Char."]   .clear()
                    date_partition_dict[" Station Pressure"]     .clear()
                    date_partition_dict[" Pressure Tendency"]    .clear()
                    date_partition_dict[" Sea Level Pressure"]   .clear()
                    date_partition_dict[" Record Type"]          .clear()
                    date_partition_dict[" Precip. Total"]        .clear()
                        
            # Wipe for next Wban partition
            wban_partition_dict["Wban Number"]           .clear()
            wban_partition_dict[" YearMonthDay"]         .clear()
            wban_partition_dict[" Time"]                 .clear()
            wban_partition_dict[" Station Type"]         .clear()
            wban_partition_dict[" Maintenance Indicator"].clear()
            wban_partition_dict[" Sky Conditions"]       .clear()
            wban_partition_dict[" Visibility"]           .clear()
            wban_partition_dict[" Weather Type"]         .clear()
            wban_partition_dict[" Dry Bulb Temp"]        .clear()
            wban_partition_dict[" Dew Point Temp"]       .clear()
            wban_partition_dict[" Wet Bulb Temp"]        .clear()
            wban_partition_dict[" % Relative Humidity"]  .clear()
            wban_partition_dict[" Wind Speed (kt)"]      .clear()
            wban_partition_dict[" Wind Direction"]       .clear()
            wban_partition_dict[" Wind Char. Gusts (kt)"].clear()
            wban_partition_dict[" Val for Wind Char."]   .clear()
            wban_partition_dict[" Station Pressure"]     .clear()
            wban_partition_dict[" Pressure Tendency"]    .clear()
            wban_partition_dict[" Sea Level Pressure"]   .clear()
            wban_partition_dict[" Record Type"]          .clear()
            wban_partition_dict[" Precip. Total"]        .clear()
            
        

#%%
with open(file = "test data/200707hourly.txt", mode = "r") as f:
    july_07_weather_df = pd.read_csv(f, low_memory = False)
    
    print(july_07_weather_df)
    
#%%
partition_by_wban_and_date(july_07_weather_df)

#%%
print(july_07_weather_df.max(numeric_only = False)[july_07_weather_df.columns.get_loc(" Wind Speed (kt)")])




#%%
# MAP
list_of_maps = []
for i in range(0, len(july_07_weather_df["Wban Number"].values)):
    x = july_07_weather_df.iloc[i]
    keys = (str(x["Wban Number"]), str(x[" YearMonthDay"]), str(x[" Wind Speed (kt)"]))
    list_of_maps.append({keys : 1})
    print(list_of_maps[i], "{}%".format(np.round(i/len(july_07_weather_df["Wban Number"].values)*100, decimals = 2)) + " complete")
    

#%%
# PARTITION
unique_keys = []

for i in range(0, len(list_of_maps)):
    this_key = list(list_of_maps[i].keys())[0]
    if unique_keys.__contains__(this_key):
        pass
    else:
        print(this_key, "{}%".format(np.round(i/len(list_of_maps)*100, decimals = 2)) + " complete")
        unique_keys.append(this_key)
    

print(unique_keys)

#%%
# REDUCE
reduced_list = []

# Scan the unique keys
for i in range(0, len(unique_keys)):
    occurances = 1
    # Compare each unique key to the list of mappings
    for j in range(0, len(list_of_maps)):
        this_key = list(list_of_maps[j].keys())[0]
        # If the unique key is encountered, increment the counter
        # for how many times it occurs by +1
        if unique_keys[i] == this_key:
            occurances = occurances + 1
    
    # Once all instances of the unique key are encountered, append the key
    # and its occurances to the reduced list
    print(
        "Found {} occurances of {}".format(occurances, unique_keys[i]), 
        "{}%".format(np.round(i/len(unique_keys)*100, decimals = 2)) + " of unique keys checked, "
        )
    reduced_list.append({unique_keys[i], occurances})

print(reduced_list)
    
# %%
