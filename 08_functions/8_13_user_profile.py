def build_profile (first, last,**infos):
    profile = {}
    profile['first name'] = first.title()
    profile['last name'] = last.title()
    for key, value in infos.items():
        profile[key] = value

    print(profile)

build_profile ('simon', 'hoch', color='white', hair='blond', size= 180)
