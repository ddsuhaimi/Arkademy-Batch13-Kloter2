import json


def get_person_dict(name, age):
    person_dict = {}
    person_dict['name'] = name
    person_dict['age'] = age
    person_dict['address'] = 'Banda Aceh'
    person_dict['hobbies'] = ['Programming']
    person_dict['is_married'] = False
    person_dict['list_school'] = [{'year_in': 2015, 'year_out': 2019, 'major': 'Mathematics'}]
    person_dict['skills'] = [{'skill_name': 'Web Programming', 'level': 'Intermediate'},
          {'skill_name': 'Python', 'level': 'Intermediate'}]
    person_dict['interest_in_coding'] = True

    return person_dict


name = 'Dedi Suhaimi'
age = 22

person_dict = get_person_dict(name, age)

with open('person.json', 'w') as json_file:
    json.dump(person_dict, json_file)