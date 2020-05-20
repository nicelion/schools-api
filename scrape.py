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
# url = 'https://nces.ed.gov/ccd/districtsearch/district_list.asp?Search=1&details=1&State=%s&DistrictType=1&DistrictType=2&DistrictType=3&DistrictType=4&DistrictType=5&DistrictType=6&DistrictType=7&DistrictType=8&NumOfStudentsRange=more&NumOfSchoolsRange=more&ID2=4500870&DistrictPageNum=%s'

def sanitize_school_districts(districts):
    
    districts = districts[5:]
    districts = districts[:len(districts)-2]

    for d in districts:
        print(d)
        # print('-> herese some info')

    return districts

def get_school_districts(state, page, url):
    print (color ('STATE page %s' % (page), colors.BLUE))

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

def get_state():
    state = input(color ('Enter (1-50) your state: ', colors.GREEN))

    try:
        if int(state) <= 50:
            return (state)
        else:
            print ((color ('[ERROR]:', colors.RED)), "Please enter a number between 1-50 corresponding to state's order alphabetically.")
            get_state()
 
    except TypeError:
        print ((color ('[ERROR]:', colors.RED)), "Please enter a number between 1-50 corresponding to state's order alphabetically.")
        get_state()

        

USA = states.UnitedStates
abbrev_us_state = dict(map(reversed, USA.us_state_abbrev.items()))

print(abbrev_us_state['AK'])

# print (color ('Retreiving School Districts', colors.RED))

# state = get_state()

# should_query = True
# i = 1
# root = 'https://nces.ed.gov/ccd/districtsearch/district_list.asp?Search=1&details=1&State=%s&DistrictType=1&DistrictType=2&DistrictType=3&DistrictType=4&DistrictType=5&DistrictType=6&DistrictType=7&DistrictType=8&NumOfStudentsRange=more&NumOfSchoolsRange=more&ID2=4500870&DistrictPageNum=%s'

# while should_query:

#     query = root % (state, i)
#     result = get_school_districts(state, i, query)

#     should_query = result[1] == 15

#     i += 1

