from itertools import groupby

employees = [
{'name': 'Ali', 'department': 'HR'},
{'name': 'Sara', 'department': 'Engineering'},
{'name': 'Reza', 'department': 'HR'},
{'name': 'Maryam', 'department': 'Engineering'},
{'name': 'Nima', 'department': 'Sales'},
{'name': 'Hadi', 'department': 'Sales'}
]

employees_sorted = sorted(employees, key=lambda x: x['department'])

grouped_employees = {}
for key, group in groupby(employees_sorted, key=lambda x: x['department']):
    grouped_employees[key] = list(group)

# print(grouped_employees)

i = 0
engineering_names = []
for names in grouped_employees['Engineering']:
    engineering_names.append(grouped_employees['Engineering'][i]['name'])
    i+=1

i = 0
sales_names = []
for names in grouped_employees['Sales']:
    sales_names.append(grouped_employees['Sales'][i]['name'])
    i+=1

i = 0
hr_names = []
for names in grouped_employees['HR']:
    hr_names.append(grouped_employees['HR'][i]['name'])
    i+=1

print(f"Department: Engineering -> {engineering_names}")
print(f"Department: Sales -> {sales_names}")
print(f"Department: HR -> {hr_names}")
