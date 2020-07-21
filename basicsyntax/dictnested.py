"""
Nested Dictionary:
d = {'k1': {'nestk1': 'nestvalue1', 'nestk2': 'nestvalue2'}}
Example: d['k1']['nestk1']
"""

cars = {'bmw': {'model': '235i', 'year': 2020}, 'vw': {'model': 'Golf', 'year': 2020}}
bmw_year = cars['bmw']['year']
print(bmw_year)
print(cars['vw']['model'])