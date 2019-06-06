def get_seconds(minutes):
    return minutes * 60

def get_speed_mile_per_second(total_second):
    return 1 / total_second

minutes = int(input('minutes: '))
seconds = int(input('seconds: '))

#minutes = 9
#seconds = 14
#miles = 5

#minutes = 8
#seconds = 0
#miles = 3

#minutes = 7
#seconds = 45
#miles = 6

#minutes = 7
#seconds = 25
#miles = 1

total_second = get_seconds(minutes) + seconds
#print('time in seconds is ' + str(total_second))

speed_mile_per_second = get_speed_mile_per_second(total_second)

mph = speed_mile_per_second * 3600
print('Your speed is ' + str(mph) + ' mph')

miles = int(input('miles:'))
elapsed_total_seconds = miles / speed_mile_per_second
elapsed_minite = int(elapsed_total_seconds // 60)
elapsed_seconds = int(elapsed_total_seconds % 60)
print('elapsed time is ' + str(elapsed_minite) + ' minutes ' + str(elapsed_seconds) + ' seconds')

