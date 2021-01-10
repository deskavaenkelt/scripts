ONE_WRAP_A_ROUND = 2 ** 32 - 1

A_SEC = 1000
A_MINUTE = 60 * A_SEC
A_HOUR = 60 * A_MINUTE
A_DAY = 24 * A_HOUR


def get_days(millis):
    number_of_days = millis // A_DAY
    rest = millis % A_DAY
    return [number_of_days, rest]


def get_hour(rest_millis):
    number_of_hours = rest_millis // A_HOUR
    rest = rest_millis % A_HOUR
    return [number_of_hours, rest]


def get_minutes(rest_millis):
    number_of_minutes = rest_millis // A_MINUTE
    rest = rest_millis % A_MINUTE
    return [number_of_minutes, rest]


def get_seconds(rest_millis):
    number_of_seconds = rest_millis // A_SEC
    rest = rest_millis % A_SEC
    return [number_of_seconds, rest]


ONE_WRAP_DAY = 49
ONE_WRAP_HOUR = 17
ONE_WRAP_MINUTE = 2
ONE_WRAP_SECOND = 47

current_wrap = 4
current_millis = 34567295

current_cycle_days = get_days(current_millis)
current_cycle_hours = get_hour(current_cycle_days[1])
current_cycle_minutes = get_minutes(current_cycle_hours[1])
current_cycle_seconds = get_seconds(current_cycle_minutes[1])

total_days = current_cycle_days[0] + (current_wrap * ONE_WRAP_DAY)
total_hours = current_cycle_hours[0] + (current_wrap * ONE_WRAP_HOUR)
total_minutes = current_cycle_minutes[0] + (current_wrap * ONE_WRAP_MINUTE)
total_seconds = current_cycle_seconds[0] + (current_wrap * ONE_WRAP_SECOND)

print('=' * 40)

print(f'total_days: {total_days}')
print(f'total_hours: {total_hours}')
print(f'total_minutes: {total_minutes}')
print(f'total_seconds: {total_seconds}')

print('=' * 40)

new_seconds = total_seconds % 60  # 235 - 180 = 55
add_minutes = total_seconds // 60  # 180 sec = 3 min

new_minutes = (total_minutes + add_minutes) % 60  # 13
add_hour = (total_minutes + add_minutes) // 60  # 0

new_hour = (total_hours + add_hour) % 24
add_days = (total_hours + add_hour) // 24

new_days = total_days + add_days

print('=' * 40)

print(f'new_days: {new_days}')
print(f'new_hour: {new_hour}')
print(f'new_minutes: {new_minutes}')
print(f'new_seconds: {new_seconds}')
