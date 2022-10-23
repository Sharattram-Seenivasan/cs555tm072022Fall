from datetime import *
from dateutil.relativedelta import *

def marriage_after_14(individuals, families):
    legal_marriage_age = 14
    all_legal_marriages = True

    for index, row in families.iterrows():
        marriage_time = datetime.strptime(row['married'], " %d %b %Y")

        #error check if husband in individuals does not exist
        husband_birth = individuals.loc[individuals['id'] == row['Husband ID'], 'birthday'].iloc[0]
        husband_birth_time = datetime.strptime(husband_birth, " %d %b %Y")
        husband_marriage_age = relativedelta(marriage_time, husband_birth_time).years

        #error check if wife in individuals does not exist
        wife_birth = individuals.loc[individuals['id'] == row['Wife ID'], 'birthday'].iloc[0]
        wife_birth_time = datetime.strptime(wife_birth, " %d %b %Y")
        wife_marriage_age = relativedelta(marriage_time, wife_birth_time).years

        if husband_marriage_age < legal_marriage_age:
            print("ERROR: FAMILY: US10: " + row['Husband ID'] + " from family " + row['id'] + " married before the age of 14!")
            all_legal_marriages = False
        if wife_marriage_age < legal_marriage_age:
            print("ERROR: FAMILY: US10: " + row['Wife ID'] + " from family " + row['id'] + " married before the age of 14!")
            all_legal_marriages = False

    if all_legal_marriages:
        print("File has all marriages after 14.")

    return all_legal_marriages