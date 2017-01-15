#! python3
# read_census_excel.py - Tabulates population and number of census tracts
# for each county

import openpyxl
import os
import pprint
from collections import defaultdict

print('Opening workbook...')
wb = openpyxl.load_workbook(r'online_materials\censuspopdata.xlsx')
sheet = wb.active
county_data = {}

# Fill in county_data with each county's population and tracts
print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract
    state = sheet['B{}'.format(row)].value
    county = sheet['C{}'.format(row)].value
    pop = sheet['D{}'.format(row)].value

    # Make sure the key for this state exists
    county_data.setdefault(state, {})
    # Make sure the key for this county in this state exists
    county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row represents one census tract, so increment by one
    county_data[state][county]['tracts'] += 1
    # Increase the county pop by the pop in the census tract
    county_data[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of county_data to it
print('Writing results...')
os.makedirs('out', exist_ok=True)
with open(r'out\census2010.py', 'w') as result_file:
    result_file.write('allData = ' + pprint.pformat(county_data))
print('Done')

