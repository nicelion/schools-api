from bs4 import BeautifulSoup
import requests
import array

from ColorIt import *
initColorIt()

# soup = BeautifulSoup(html_doc, 'html.parser')


# sc1 = requests.get('https://nces.ed.gov/ccd/districtsearch/district_list.asp?Search=1&details=1&InstName=&DistrictID=&Address=&City=&State=45&Zip=&Miles=&County=&PhoneAreaCode=&Phone=&DistrictType=1&DistrictType=2&DistrictType=3&DistrictType=4&DistrictType=5&DistrictType=6&DistrictType=7&DistrictType=8&NumOfStudents=&NumOfStudentsRange=more&NumOfSchools=&NumOfSchoolsRange=more')
# ab1 = requests.get('https://nces.ed.gov/ccd/districtsearch/district_list.asp?Search=1&details=1&State=01&DistrictType=1&DistrictType=2&DistrictType=3&DistrictType=4&DistrictType=5&DistrictType=6&DistrictType=7&DistrictType=8&NumOfStudentsRange=more&NumOfSchoolsRange=more&DistrictPageNum=2')
# soup = BeautifulSoup(ab1.text, 'html.parser')

# print(soup.body.contents26])

# districts = soup.find_all('strong')
# table = soup.find_all('table')[3]
# districts = table.find_all('strong')

# for district in districts:
#     d = district.get_text()

#     print(d)


def sanitize_school_districts(districts):
    
    districts = districts[5:]
    districts = districts[:len(districts)-2]

    for d in districts:
        print(d)

    return districts

def get_school_districts(page, url):
    print (color ('STATE page %s' % (i), colors.BLUE))

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


# sc1 = 'https://nces.ed.gov/ccd/districtsearch/district_list.asp?Search=1&details=1&State=45&DistrictType=1&DistrictType=2&DistrictType=3&DistrictType=4&DistrictType=5&DistrictType=6&DistrictType=7&DistrictType=8&NumOfStudentsRange=more&NumOfSchoolsRange=more&ID2=4500870&DistrictPageNum=7'
# sc2 = 'https://nces.ed.gov/ccd/districtsearch/district_list.asp?Search=1&details=1&State=23&DistrictType=1&DistrictType=2&DistrictType=3&DistrictType=4&DistrictType=5&DistrictType=6&DistrictType=7&DistrictType=8&NumOfStudentsRange=more&NumOfSchoolsRange=more&DistrictPageNum=4'
# u = get_school_districts(sc1)

# # print(u[1])

print (color ('Retreiving School Districts', colors.RED))

should_query = True
i = 1
root = 'https://nces.ed.gov/ccd/districtsearch/district_list.asp?Search=1&details=1&State=45&DistrictType=1&DistrictType=2&DistrictType=3&DistrictType=4&DistrictType=5&DistrictType=6&DistrictType=7&DistrictType=8&NumOfStudentsRange=more&NumOfSchoolsRange=more&ID2=4500870&DistrictPageNum=%s'
while should_query:

    query = root % (i)
    result = get_school_districts(i, query)

    should_query = result[1] == 15

    i += 1

# i = 0
# for t in table:
#     print(t)
#     print(i)
#     i += 1

# for district in table:
#     print(district)
# print(district)
# url = 'https://nces.ed.gov/ccd/districtsearch/district_list.asp?Search=1&details=1&InstName=&DistrictID=&Address=&City=&State=45&Zip=&Miles=&County=&PhoneAreaCode=&Phone=&DistrictType=1&DistrictType=2&DistrictType=3&DistrictType=4&DistrictType=5&DistrictType=6&DistrictType=7&DistrictType=8&NumOfStudents=&NumOfStudentsRange=more&NumOfSchools=&NumOfSchoolsRange=more'
# r = requests.get(url)
# df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
# df = df_list[0]
# df.head()



# https://nces.ed.gov/ccd/districtsearch/district_detail.asp?Search=1&details=1&amp;State=45&amp;DistrictType=1&amp;DistrictType=2&amp;DistrictType=3&amp;DistrictType=4&amp;DistrictType=5&amp;DistrictType=6&amp;DistrictType=7&amp;DistrictType=8&amp;NumOfStudentsRange=more&amp;NumOfSchoolsRange=more&amp;ID2=4500690
# https://nces.ed.gov/ccd/districtsearch/district_detail.asp?Search=1&details=1&State=45&DistrictType=1&DistrictType=2&DistrictType=3&DistrictType=4&DistrictType=5&DistrictType=6&DistrictType=7&DistrictType=8&NumOfStudentsRange=more&NumOfSchoolsRange=more&DistrictPageNum=1&ID2=4500690