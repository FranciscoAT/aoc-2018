import sys
import datetime

def get_guard(entry):
    return(entry.split(' ')[1][1:])



times = []
for val in open(sys.argv[1]).readlines():
    log_entry = val.rstrip()
    month, day = [int(x) for x in log_entry[6:11].split('-')]
    hour, minute = [int(x) for x in log_entry[12:17].split(':')]
    epoch_time = datetime.datetime(2018, month, day, hour, minute).timestamp()
    hour_time = datetime.datetime(2018, 1, 1, hour, minute).timestamp()
    cleaned_entry = (epoch_time, hour_time, log_entry[19:])
    times.append(cleaned_entry)

times.sort(key = lambda x:x[0])
# print(times)

time_slept = {}
curr_guard = ""
is_awake = True
prev_time = None

for epoch_time, entry in times:
    if curr_guard not in time_slept and curr_guard is not "":
        time_slept[curr_guard] = [0] * 60
    if 'begins shift' in entry:
        if curr_guard is not "" and is_awake is False:

            time_slept[curr_guard] += (epoch_time - prev_time)
        curr_guard = get_guard(entry)
    elif 'falls asleep' in entry:
        is_awake = False
    else:
        is_awake = True
        time_slept[curr_guard] += (epoch_time - prev_time)
    prev_time = epoch_time

guard_id = max(time_slept, key=time_slept.get)
print(guard_id)
print(int(guard_id) * time_slept[guard_id])


