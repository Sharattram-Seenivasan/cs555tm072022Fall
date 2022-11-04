import os
import pandas as pd

def listMultipleBirths(individuals):
    coveredBirthdays = []
    for index, row in individuals.iterrows():
        birthdays = []
        if row['birthday'] not in coveredBirthdays:
            sameBirthdays = individuals[individuals['birthday'] == row['birthday']]
            coveredBirthdays.append(row['birthday'])
            if len(sameBirthdays.index) > 1:
                print('US32: Has birthday on ' + row['birthday'] + ':')
                print(list(zip(sameBirthdays['id'],sameBirthdays['age'])))