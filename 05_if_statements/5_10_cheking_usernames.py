curent_users = ['simon', 'sophie', 'rumi', 'velli', 'bobi']
new_users = ['hoha', 'Sophie', 'slavi', 'haho', 'Velli']

for new_user in new_users:
    if new_user.lower() in curent_users:
        print ('Sorry u need to enter a new user name')
    else:
        print ('The user name is available')
