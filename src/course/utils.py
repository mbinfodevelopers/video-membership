

def cal_time_to_seconds(time):
    # example of time '00,00,00'

    split_time = time.split(',')
    hour = int(split_time[0]) * 60 * 60
    minute = int(split_time[1]) * 60
    seconds_sum = hour + minute + int(split_time[2])

    return seconds_sum