import csv, pickle
from sklearn import model_selection as cv

from collections import defaultdict


data1 = defaultdict(dict)


with open('ratings_Video_games.csv') as csvfile:
    
    data = csv.reader(csvfile)
    
    for rows in data:
        data1[rows[0]][rows[1]] = rows[2]
    
    pickle.dump(data1, open('Video_games.dict', 'wb'))