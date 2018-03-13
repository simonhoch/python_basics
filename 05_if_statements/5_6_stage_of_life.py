ages = [8, 4, 2, 10, 66, 35, 15, 20,0]
age_stages = ['baby', 'todler', 'kid', 'teenager', 'adult', 'elder']
print(ages)

for age in ages:
    if age < 2:
        age_stage = age_stages [0]
    elif age < 4:
        age_stage = age_stages [1]
    elif age < 13:
        age_stage = age_stages [2]
    elif age < 20:
        age_stage = age_stages [3]
    elif age < 65:
        age_stage = age_stages [4]
    else:
        age_stage = age_stages [5]
        
    print ('Your age is ' + str(age) + ' years old, so you are a ' + age_stage)
