# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 18:40:51 2022

@author: wajee
"""

import pandas as pd

gray_data = []
cinnamon_data = []
black_data = []

get_file_path = "path"

data = pd.read_csv(get_file_path)

color_data = data["Primary Fur Color"]

list_data = color_data.to_list()

#print(list_data)

for squirrel in list_data:
    
    if (squirrel == "Gray"):
        gray_data.append(squirrel)
    
    if(squirrel == "Black"):
        black_data.append(squirrel)
    
    if(squirrel == "Cinnamon"):
        cinnamon_data.append(squirrel)
        


#print(gray_data)
#print(black_data)
#print(cinnamon_data)

gray_count = gray_data.count("Gray")
#print(gray_count)

black_count = black_data.count("Black")
#print(black_count)

cinnamon_count = cinnamon_data.count("Cinnamon")
#print(cinnamon_count)


data_dict = {
    "Fur Color" : ["Gray","Black","Cinnamon"],
    "Count" : [gray_count,black_count,cinnamon_count]
    }

new_data = pd.DataFrame(data_dict)
print(new_data)
new_data.to_csv("squirrel_color.csv")
