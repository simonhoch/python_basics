alien_colors = ['green', 'green', 'red', 'yellow', 'purple']
total_points = 0

for alien_color in alien_colors:
    if alien_color == 'green':
        points = 5
    elif alien_color == 'yellow':
        points = 10
    else:
        points = 15
    print ('u earn ' + str(points) + ' points')
    total_points += points

print ('\nu earned a total of ' + str(total_points) + ' points')
