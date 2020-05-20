# scrape.py
# schools-api

# Created by Ian Thompson
# MIT Licence

from bs4 import BeautifulSoup
import requests
import array
import states

from ColorIt import *

initColorIt()
USA = states.UnitedStates
state_codes = dict(map(reversed, USA.codes.items()))
state_abbreviations = dict(map(reversed, USA.abbreviations.items()))
# url = 'https://nces.ed.gov/ccd/districtsearch/district_list.asp?Search=1&details=1&State=%s&DistrictType=1&DistrictType=2&DistrictType=3&DistrictType=4&DistrictType=5&DistrictType=6&DistrictType=7&DistrictType=8&NumOfStudentsRange=more&NumOfSchoolsRange=more&ID2=4500870&DistrictPageNum=%s'

def sanitize_school_districts(districts):
    
    districts = districts[5:]
    districts = districts[:len(districts)-2]

    for d in districts:
        print(d)
        # print('-> herese some info')

    return districts

def get_school_districts(state, page, url):
    districts = []

    
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')

    table = soup.find_all('table')[3]
    tables_districts = table.find_all('strong')

    for district in tables_districts:
        d = district.get_text()
        districts.append(d)

    sanitized_districts = sanitize_school_districts(districts)
    return (sanitized_districts, len(sanitized_districts))

# def begin_query(state):
    

def get_state():
    state = input(color ('Enter state abbreviation your state (help for more info): ', colors.GREEN))

    if state == 'help':
        print(state_abbreviations)
        get_state()
    if state in state_codes:
        return state_codes[state]

        



print (color ('Retreiving School Districts', colors.RED))

state = get_state()

should_query = True
i = 1
root = 'https://nces.ed.gov/ccd/districtsearch/district_list.asp?Search=1&details=1&State=%s&DistrictType=1&DistrictType=2&DistrictType=3&DistrictType=4&DistrictType=5&DistrictType=6&DistrictType=7&DistrictType=8&NumOfStudentsRange=more&NumOfSchoolsRange=more&ID2=4500870&DistrictPageNum=%s'

print(state)
while should_query:

    query = root % (state, i)
    result = get_school_districts(state, i, query)

    should_query = result[1] == 15

    i += 1

