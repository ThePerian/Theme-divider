#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import csv
import re

filename = 'users.csv'
delim = ';'
outputHeader = list(['email', 'name', 'return_path', 'metadata', 'substitution_data', 'tags'])
inputHeader = list(['Email', 'ФИО'])
themeHeader = 'Темы'

f = open(filename, 'rt')
users = []
try:
    reader = csv.DictReader(f, delimiter=delim)
    for row in reader:
        users.append(row)
finally:
    f.close()

themeList = defaultdict(list)

for user in users:
    userThemes = user[themeHeader]
    for theme in re.split(r'[\[\]]+', userThemes):
        if not themeList[theme]:
            themeList[theme] = []
        themeList[theme].append(user)

for theme in themeList:
    f = open(theme+'.csv', 'wt')
    try:
        writer = csv.writer(f)
        writer.writerow(outputHeader)
        for user in themeList[theme]:
            writer.writerow([user[inputHeader[0]], user[inputHeader[1]]])
    finally:
        f.close()

