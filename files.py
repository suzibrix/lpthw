path = '/home/vll/Documents/days.txt'

days_file = open(path,'r')
title = 'Days of the Week\n'
days = days_file.read()
new_path = '/home/vll/Documents/new_days.txt'
new_days = open(new_path,'w')
new_days.write(title)
print(title)

new_days.write(days)
print(days)

days_file.close()
new_days.close()
