from pathlib import Path
import statistics
from crowdtype import CrowdType

big_crowd = CrowdType('big_crowd')
small_crowd = CrowdType('small_crowd')
no_crowd = CrowdType('no_crowd')

# iterate through all files
entries = Path('proxemic_data/')
for entry in entries.iterdir():
    print('\n\nFile about to process: %s' % entry.name)
    file_name_lower = entry.name.lower()
    do_not_use = False
    if 'mfvbsn1' in file_name_lower:
        do_not_use = True
    #if 'fvmnsb1' in file_name_lower:
        #do_not_use = True
    if 'fmvsbn1' in file_name_lower:
        do_not_use = True
    if 'fmvnbs1' in file_name_lower:
        do_not_use = True
    if 'event' not in file_name_lower and do_not_use is False:
        file_str = 'proxemic_data/' + entry.name
        f = open(file_str, 'rt')  # open file
        file_data: str = f.read()
        prox_data: list = file_data.split(' ')  # copy file to list
        prox_data = prox_data[122:-119:2]  # format list
        f.close()  # close file
        min_of_data = min(prox_data)
        max_of_data = max(prox_data)
        if 'food' in file_name_lower:
            category = 'food'
            position: int = file_name_lower.find('f')
        elif 'movie' in file_name_lower:
            category = 'movie'
            position: int = file_name_lower.find('m')
        elif 'vacation' in file_name_lower:
            category = 'vacation'
            position: int = file_name_lower.find('v')
        print('File contained: %s' % category + ' \nVacation position: %s' % str(position))
        crowd_type_position = 3 + position

        if file_name_lower[crowd_type_position:crowd_type_position + 1] is 'n':
            print('File contained: n \nn position: %s' % str(crowd_type_position))
            no_crowd.crowd_data[position].append((min_of_data, max_of_data))
            no_crowd.full_data_crowd[position].extend(prox_data)

        if file_name_lower[crowd_type_position:crowd_type_position + 1] is 's':
            print('File contained: s \ns position: %s' % str(crowd_type_position))
            small_crowd.crowd_data[position].append((min_of_data, max_of_data))
            small_crowd.full_data_crowd[position].extend(prox_data)

        if file_name_lower[crowd_type_position:crowd_type_position + 1] is 'b':
            print('File contained: b \nb position: %s' % str(crowd_type_position))
            big_crowd.crowd_data[position].append((min_of_data, max_of_data))
            big_crowd.full_data_crowd[position].extend(prox_data)

        print('File data min: %s' % str(min_of_data))
        print('File data max: %s' % str(max_of_data))

counter = 0
no_crowd_min_list = list()
no_crowd_max_list = list()
small_crowd_min_list = list()
small_crowd_max_list = list()
big_crowd_min_list = list()
big_crowd_max_list = list()
min_list = list()
max_list = list()

print('\nNo crowd data:')
for n in no_crowd.crowd_data:
    print('No crowd data[' + str(counter) + ']: ' + str(n))
    for m in n:
        # print(m)
        min_list.append(m[0])
        max_list.append(m[1])
        no_crowd_min_list.append(m[0])
        no_crowd_max_list.append(m[1])
    min_info = min(min_list)
    max_info = max(max_list)
    mean_min_info = sum(float(i) for i in min_list) / len(min_list)
    mean_max_info = sum(float(i) for i in max_list) / len(max_list)
    print('No crowd data[' + str(counter) + '] min: ' + str(min_info))
    print('No crowd data[' + str(counter) + '] max: ' + str(max_info))
    print('No crowd data[' + str(counter) + '] mean_min: ' + str(mean_min_info))
    print('No crowd data[' + str(counter) + '] mean_max: ' + str(mean_max_info))
    if counter == 0:
        no_crowd.first_data_min = min_info
        no_crowd.first_data_max = max_info
        no_crowd.first_data_mean_min = mean_min_info
        no_crowd.first_data_mean_max = mean_max_info
    elif counter == 1:
        no_crowd.second_data_min = min_info
        no_crowd.second_data_max = max_info
        no_crowd.second_data_mean_min = mean_min_info
        no_crowd.second_data_mean_max = mean_max_info
    elif counter == 2:
        no_crowd.third_data_min = min_info
        no_crowd.third_data_max = max_info
        no_crowd.third_data_mean_min = mean_min_info
        no_crowd.third_data_mean_max = mean_max_info
    min_list.clear()
    max_list.clear()
    counter += 1
min_info = min(no_crowd_min_list)
max_info = max(no_crowd_max_list)
mean_min_info = sum(float(i) for i in no_crowd_min_list) / len(no_crowd_min_list)
mean_max_info = sum(float(i) for i in no_crowd_max_list) / len(no_crowd_max_list)
no_crowd.all_data_min = min_info
no_crowd.all_data_max = max_info
no_crowd.all_data_mean_min = mean_min_info
no_crowd.all_data_mean_max = mean_max_info
print('No crowd data all min: ' + str(min_info))
print('No crowd data all max: ' + str(max_info))
print('No crowd data all mean_min: ' + str(mean_min_info))
print('No crowd data all mean_max: ' + str(mean_max_info))
temnp123 = statistics.stdev((float(i) for i in no_crowd_min_list), mean_min_info)
print("awefawef: " + str(temnp123))
# full_mean_info = sum(float(i) for i in no_crowd.full_data_crowd) / len(no_crowd.full_data_crowd)
# no_crowd.full_data_crowd_all_mean = full_mean_info
full_mean_first_info = sum(float(i) for i in no_crowd.full_data_crowd[0]) / len(no_crowd.full_data_crowd[0])
full_mean_second_info = sum(float(i) for i in no_crowd.full_data_crowd[1]) / len(no_crowd.full_data_crowd[1])
full_mean_third_info = sum(float(i) for i in no_crowd.full_data_crowd[2]) / len(no_crowd.full_data_crowd[2])
no_crowd.full_data_crowd_first_mean = full_mean_first_info
no_crowd.full_data_crowd_second_mean = full_mean_second_info
no_crowd.full_data_crowd_third_mean = full_mean_third_info

min_list.clear()
max_list.clear()
counter = 0
print('\nSmall crowd data:')
for n in small_crowd.crowd_data:
    print('Small crowd data[' + str(counter) + ']: ' + str(n))
    for m in n:
        # print(m)
        min_list.append(m[0])
        max_list.append(m[1])
        small_crowd_min_list.append(m[0])
        small_crowd_max_list.append(m[1])
    min_info = min(min_list)
    max_info = max(max_list)
    mean_min_info = sum(float(i) for i in min_list) / len(min_list)
    mean_max_info = sum(float(i) for i in max_list) / len(max_list)
    print('Small crowd data[' + str(counter) + '] min: ' + str(min_info))
    print('Small crowd data[' + str(counter) + '] max: ' + str(max_info))
    print('Small crowd data[' + str(counter) + '] mean_min: ' + str(mean_min_info))
    print('Small crowd data[' + str(counter) + '] mean_max: ' + str(mean_max_info))
    if counter == 0:
        small_crowd.first_data_min = min_info
        small_crowd.first_data_max = max_info
        small_crowd.first_data_mean_min = mean_min_info
        small_crowd.first_data_mean_max = mean_max_info
    elif counter == 1:
        small_crowd.second_data_min = min_info
        small_crowd.second_data_max = max_info
        small_crowd.second_data_mean_min = mean_min_info
        small_crowd.second_data_mean_max = mean_max_info
    elif counter == 2:
        small_crowd.third_data_min = min_info
        small_crowd.third_data_max = max_info
        small_crowd.third_data_mean_min = mean_min_info
        small_crowd.third_data_mean_max = mean_max_info
    min_list.clear()
    max_list.clear()
    counter += 1
min_info = min(small_crowd_min_list)
max_info = max(small_crowd_max_list)
mean_min_info = sum(float(i) for i in small_crowd_min_list) / len(small_crowd_min_list)
mean_max_info = sum(float(i) for i in small_crowd_max_list) / len(small_crowd_max_list)
small_crowd.all_data_min = min_info
small_crowd.all_data_max = max_info
small_crowd.all_data_mean_min = mean_min_info
small_crowd.all_data_mean_max = mean_max_info
print('Small crowd data all min: ' + str(min_info))
print('Small crowd data all max: ' + str(max_info))
print('Small crowd data all mean_min: ' + str(mean_min_info))
print('Small crowd data all mean_max: ' + str(mean_max_info))
# full_mean_info = sum(float(i) for i in small_crowd.full_data_crowd) / len(small_crowd.full_data_crowd)
# small_crowd.full_data_crowd_all_mean = full_mean_info
full_mean_first_info = sum(float(i) for i in small_crowd.full_data_crowd[0]) / len(small_crowd.full_data_crowd[0])
full_mean_second_info = sum(float(i) for i in small_crowd.full_data_crowd[1]) / len(small_crowd.full_data_crowd[1])
full_mean_third_info = sum(float(i) for i in small_crowd.full_data_crowd[2]) / len(small_crowd.full_data_crowd[2])
small_crowd.full_data_crowd_first_mean = full_mean_first_info
small_crowd.full_data_crowd_second_mean = full_mean_second_info
small_crowd.full_data_crowd_third_mean = full_mean_third_info

min_list.clear()
max_list.clear()
counter = 0
print('\nBig crowd data:')
for n in big_crowd.crowd_data:
    print('Big crowd data[' + str(counter) + ']: ' + str(n))
    for m in n:
        # print(m)
        min_list.append(m[0])
        max_list.append(m[1])
        big_crowd_min_list.append(m[0])
        big_crowd_max_list.append(m[1])
    min_info = min(min_list)
    max_info = max(max_list)
    mean_min_info = sum(float(i) for i in min_list) / len(min_list)
    mean_max_info = sum(float(i) for i in max_list) / len(max_list)
    print('Big crowd data[' + str(counter) + '] min: ' + str(min_info))
    print('Big crowd data[' + str(counter) + '] max: ' + str(max_info))
    print('Big crowd data[' + str(counter) + '] mean_min: ' + str(mean_min_info))
    print('Big crowd data[' + str(counter) + '] mean_max: ' + str(mean_max_info))
    if counter == 0:
        big_crowd.first_data_min = min_info
        big_crowd.first_data_max = max_info
        big_crowd.first_data_mean_min = mean_min_info
        big_crowd.first_data_mean_max = mean_max_info
    elif counter == 1:
        big_crowd.second_data_min = min_info
        big_crowd.second_data_max = max_info
        big_crowd.second_data_mean_min = mean_min_info
        big_crowd.second_data_mean_max = mean_max_info
    elif counter == 2:
        big_crowd.third_data_min = min_info
        big_crowd.third_data_max = max_info
        big_crowd.third_data_mean_min = mean_min_info
        big_crowd.third_data_mean_max = mean_max_info
    min_list.clear()
    max_list.clear()
    counter += 1
min_info = min(big_crowd_min_list)
max_info = max(big_crowd_max_list)
mean_min_info = sum(float(i) for i in big_crowd_min_list) / len(big_crowd_min_list)
mean_max_info = sum(float(i) for i in big_crowd_max_list) / len(big_crowd_max_list)
big_crowd.all_data_min = min_info
big_crowd.all_data_max = max_info
big_crowd.all_data_mean_min = mean_min_info
big_crowd.all_data_mean_max = mean_max_info
print('Big crowd data all min: ' + str(min_info))
print('Big crowd data all max: ' + str(max_info))
print('Big crowd data all mean_min: ' + str(mean_min_info))
print('Big crowd data all mean_max: ' + str(mean_max_info))
# full_mean_info = sum(float(i) for i in big_crowd.full_data_crowd) / len(big_crowd.full_data_crowd)
# big_crowd.full_data_crowd_all_mean = full_mean_info
full_mean_first_info = sum(float(i) for i in big_crowd.full_data_crowd[0]) / len(big_crowd.full_data_crowd[0])
full_mean_second_info = sum(float(i) for i in big_crowd.full_data_crowd[1]) / len(big_crowd.full_data_crowd[1])
full_mean_third_info = sum(float(i) for i in big_crowd.full_data_crowd[2]) / len(big_crowd.full_data_crowd[2])
big_crowd.full_data_crowd_first_mean = full_mean_first_info
big_crowd.full_data_crowd_second_mean = full_mean_second_info
big_crowd.full_data_crowd_third_mean = full_mean_third_info

print('\n\n')
no_crowd.print_crowdtype_info()
print('\n\n')
small_crowd.print_crowdtype_info()
print('\n\n')
big_crowd.print_crowdtype_info()

'''
f = open('proxemic_data/mvfnsb1_ProxemicFoodData.txt', 'rt')
file_data: str = f.read()
prox_data: list = file_data.split(' ')
prox_data = prox_data[2::2]
print(prox_data)
print(min(prox_data))
print(max(prox_data))'''
