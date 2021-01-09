one_wrap_around = 2 ** 32 - 1

a_sec = 1000
a_minute = 60 * a_sec
a_hour = 60 * a_minute
a_day = 24 * a_hour


def get_days(current_millis):
    number_of_days = current_millis // a_day
    rest = one_wrap_around % a_day
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


print(one_wrap_around // a_day)
print(one_wrap_around % a_day)

print('=' * 40)

sum = get_days(one_wrap_around)
print('Number of days: \t\t\t{}, \trest: {} '.format(sum[0], sum[1]))

sum = get_hour(sum[1])
print('Number of hours: \t\t\t{}, \trest: {} '.format(sum[0], sum[1]))

sum = get_minutes(sum[1])
print('Number of minutes: \t\t\t{}, \trest: {} '.format(sum[0], sum[1]))

sum = get_seconds(sum[1])
print('Number of seconds: \t\t\t{}, \trest: {} '.format(sum[0], sum[1]))


print('Number of nano seconds: \t{}'.format(sum[1]))

one_wrap_a_round_days = 49
one_wrap_a_round_hours = 17
one_wrap_a_round_minutes = 2
one_wrap_a_round_seconds = 47


number_of_wrap_a_rounds = 4
current_millis = 34567295

current_a_round_days = get_days(current_millis)
current_a_round_hours = get_hour(current_a_round_days[1])
current_a_round_minutes = get_minutes(current_a_round_hours[1])
current_a_round_seconds = get_seconds(current_a_round_minutes[1])

wrap_days = number_of_wrap_a_rounds * one_wrap_a_round_days
wrap_hours = number_of_wrap_a_rounds * one_wrap_a_round_hours
wrap_minutes = number_of_wrap_a_rounds * one_wrap_a_round_minutes
wrap_seconds = number_of_wrap_a_rounds * one_wrap_a_round_seconds

total_days = current_a_round_days[0] + wrap_days
total_hours = current_a_round_hours[0] + wrap_hours
total_minutes = current_a_round_minutes[0] + wrap_minutes
total_seconds = current_a_round_seconds[0] + wrap_seconds

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
