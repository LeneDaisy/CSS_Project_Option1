#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 16:34:02 2024

@author: lenenortje
"""

import pandas as pd 

df = pd.read_csv("movie_dataset.csv")

print(df)

print("describe")
describe = df.describe()
print(describe)

print("info")
df.info()
info = df.info()
print(info)

print("--------------")

print(df["Rating"].max())
highest_rated_mov = df[df['Rating'] == 9]
print("highest rated movie")
print(highest_rated_mov)

x = df["Revenue (Millions)"].mean()

df["Revenue (Millions)"].fillna(x, inplace = True) 

y = df["Metascore"].mean()

df["Metascore"].fillna(y, inplace = True) 

print("mean of the Revenue (Millions)")
print(df["Revenue (Millions)"].mean())

print("Selected years mean (2015-2017)")
selected_year = df[df['Year'] == 2015]
selected_year2 = df[df['Year'] == 2016]
selected_year3 = df[df['Year'] == 2017]
combined_years = pd.concat([selected_year, selected_year2, selected_year3])

print(selected_year)
print(selected_year2)
print(selected_year3)

print("mean of combined years")
print(combined_years["Revenue (Millions)"].mean())

director = df[df['Director'] == "Christopher Nolan"]

print(director)

rating = df[df['Rating'] >= 8]

print("Median of movies rating directed by CN")
print(director["Rating"].median())

print("Year with highest average rating")

year_2006 = df[df["Year"] == 2006]
year_2007 = df[df["Year"] == 2007]
year_2008 = df[df["Year"] == 2008]
year_2016 = df[df["Year"] == 2016]

print("mean values will follow")
year_2006_m = year_2006["Rating"].mean()
print("means of the year 2006")
print(year_2006_m)


year_2007_m = year_2007["Rating"].mean()
print("means of the year 2007")
print(year_2007_m)

year_2008_m = year_2008["Rating"].mean()
print("means of the year 2008")
print(year_2008_m)

year_2016_m = year_2016["Rating"].mean()
print("means of the year 2016")
print(year_2016_m)

print("percentage increase of 2006 t0 2016")

movies_until_2006 = df[df["Year"] <= 2006]
movies_up_to_2016 = df[df["Year"] <= 2016]
movies_up_to_2016_e = df[df["Year"] < 2016]

movies_in_2016 = df[df["Year"] == 2016]

percentage_increase =((movies_in_2016  - movies_until_2006) / movies_until_2006)*100

print("precentage increase is:")
print(percentage_increase)


print("most common actor")
    
from collections import Counter

actors_column = df["Actors"]
all_the_actors = [actor.strip() for actors_list in actors_column.str.split(',') for actor in actors_list]
actors_count = Counter(all_the_actors)
most_common_actor, most_common_count = actors_count.most_common(1)[0]

print(f"The most common actor is: {most_common_actor} with {most_common_count} .")

print("calculate the most common genre")

genres_c = df["Genre"]
all_the_genres = [genre.strip() for genres_list in genres_c.str.split(',') for genre in genres_list]
unique_genres = set(all_the_genres)
num_unique_g = len(unique_genres)
print(f"There are {num_unique_g} unique genres.")

print (df.columns)

from ydata_profiling import ProfileReport

profile = ProfileReport(df, title="Profiling report")

profile.to_file("your_report.html")







