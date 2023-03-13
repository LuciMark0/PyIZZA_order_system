# Importing necessary libraries and functions
from pizza_full_database import receipt_pizza_addmade_database
import pandas as pd
import matplotlib.pyplot as plt

# Fetching data from the database
data_all = receipt_pizza_addmade_database()
data1 = data_all.all_receipt_pizza()
data2 = data_all.all_receipt_pizza_addmade()
data3 = data_all.all_receipt_pizza_name()
data4 = data_all.all_receipt_pizza_total()

# Creating a dictionary to store the fetched data
database_dictionary = {}

# Extracting pizza name, add-ons, and prices from the data and storing in a list
pizza_database_name_addmade_price = []
for i in data1:
    for j in(i[0].split("\n")):
        if(j!=""):
            pizza_database_name_addmade_price.append(j)
database_dictionary["pizza_database_name_addmade_price"] = pizza_database_name_addmade_price

# Extracting all add-ons used with each pizza and storing in a list
pizza_database_addmade=[]
all_addmade_list=[]
for i in data2:
    for j in(i[0].split("\n")):
        for t in(j.split(" ")):
            if (t!=""):
                all_addmade_list.append(t)
        if(j!=""):
            pizza_database_addmade.append(j)
database_dictionary["all_preferred_together_addmade"] = pizza_database_addmade

# Extracting all pizza names and storing in a list
pizza_database_name=[]
for i in data3:
    for j in(i[0].split("\n")):
        if(j!=""):
            pizza_database_name.append(j)
database_dictionary["all_pizza_name"] = pizza_database_name

# Extracting all pizza prices and storing in a list
pizza_database_total=[]
for i in data4:
    for j in(i[0].split("\n")):
        if(j!=""):
            pizza_database_total.append(j)

# Converting the dictionary to a pandas DataFrame
data_frame = pd.DataFrame.from_dict(database_dictionary)

# Defining functions for data analysis and visualization
def pizza_database_name_addmade_func():
    global data_frame
    data_frame_pizza_database_name_addmade_price = data_frame.iloc[:,0]
    counterlist = []
    set_data_frame_pizza_database_name_addmade_price = list(set(data_frame_pizza_database_name_addmade_price))
    for i in set_data_frame_pizza_database_name_addmade_price:
        counterlist.append(list(data_frame_pizza_database_name_addmade_price).count(i))

    plt.figure().set_figwidth(20)
    plt.subplots_adjust(left=0.3)
    plt.title("Graph of all pizzas by sale")
    plt.barh(set_data_frame_pizza_database_name_addmade_price, counterlist)
    plt.show()

def pizza_database_together_addmade_func():
    global data_frame
    all_addmade = data_frame.iloc[:,1]
    all_addmade = (list(all_addmade))
    all_addmade_list = []
    for i in all_addmade:
        for j in (i.split(" ")):
            if(j != ""):
                all_addmade_list.append(j)

    set_allmade_list = list(set(all_addmade))
    allmade_list_count = []
    for i in set_allmade_list:
        allmade_list_count.append(all_addmade.count(i))
        
    plt.figure().set_figwidth(20)
    plt.subplots_adjust(left=0.3)
    plt.title("Proportion of additional materials used together")
    plt.barh(set_allmade_list, allmade_list_count)
    plt.show()

def how_many_best_selling_pizzas(count):
    data_find_max = list(set(data_frame.iloc[:,0]))
    set_data_find_max = list(data_frame.iloc[:,0])
    new_list = []
    for i in data_find_max:
        new_list.append(set_data_find_max.count(i))
    direction_database = {"database": data_find_max, "count": new_list}
    new_data_frame = pd.DataFrame(direction_database)
    a = new_data_frame.sort_values(by=["count"], ascending=False).head(count)
    print(a)
    input("\nPress enter to continue\n")
    
    all_addmade = data_frame.iloc[:,1]
    all_addmade = list(all_addmade)
    all_addmade_list = []
    for i in all_addmade:
        for j in (i.split(" ")):
            if(j != ""):
                all_addmade_list.append(j)

    set_allmade_list = list(set(all_addmade))
    allmade_list_count = []
    for i in set_allmade_list:
        allmade_list_count.append(all_addmade.count(i))
    
    dictionary = {"set_allmade_list": set_allmade_list, "allmade_list_count": allmade_list_count}
    data_frame_allmade = pd.DataFrame(dictionary)
    print(data_frame_allmade.sort_values(by=["allmade_list_count"], ascending=False).head(count))
