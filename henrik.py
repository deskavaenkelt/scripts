one_wrap_around = 2 ** 32 - 1

a_sec = 1000
a_minute = 60 * a_sec
a_hour = 60 * a_minute
a_day = 24 * a_hour


def get_days(millis):
    number_of_days = millis // a_day
    rest = millis % a_day
    return [number_of_days, rest]


def get_hour(rest_millis):
    number_of_hours = rest_millis // a_hour
    rest = rest_millis % a_hour
    return [number_of_hours, rest]


def get_minutes(rest_millis):
    number_of_minutes = rest_millis // a_minute
    rest = rest_millis % a_minute
    return [number_of_minutes, rest]


def get_seconds(rest_millis):
    number_of_seconds = rest_millis // a_sec
    rest = rest_millis % a_sec
    return [number_of_seconds, rest]


one_wrap_a_round_day = 49
one_wrap_a_round_hour = 17
one_wrap_a_round_minute = 2
one_wrap_a_round_second = 47

current_wrap = 4
current_millis = 34567295

current_cycle_days = get_days(current_millis)
current_cycle_hours = get_hour(current_cycle_days[1])
current_cycle_minutes = get_minutes(current_cycle_hours[1])
current_cycle_seconds = get_seconds(current_cycle_minutes[1])

total_days = current_cycle_days[0] + (current_wrap * one_wrap_a_round_day)
total_hours = current_cycle_hours[0] + (current_wrap * one_wrap_a_round_hour)
total_minutes = current_cycle_minutes[0] + (current_wrap * one_wrap_a_round_minute)
total_seconds = current_cycle_seconds[0] + (current_wrap * one_wrap_a_round_second)

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
