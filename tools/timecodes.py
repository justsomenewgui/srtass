import re
from tools.subtime import SubTime

def timecode(old_file, new_file, seconds=0, milliseconds=0, minutes=0):
    with (open(old_file) as o_f, open(new_file, 'w') as n_f):
        for line in o_f:
            if old_file.endswith('.srt'):
                if '-->' in line:
                    line = re.split(':|,| |\n', line)
                    time_line = SubTime(seconds, milliseconds, minutes)
                    first_timecode = time_line.timechanger(line, 3)
                    next_timecode = time_line.timechanger(first_timecode, 8)
                    print('%s:%s:%s,%s %s %s:%s:%s,%s' %
                      (line[0], line[1], line[2], line[3], line[4],
                       line[5],line[6],line[7], line[8]), file = n_f)
                else:
                    print(line, end='', file=n_f)

            elif old_file.endswith('.ass'):
                if line.startswith('Dialogue:'):
                    line = re.split('[:,.]', line, maxsplit=10)
                    #.ass files have two-digit number milliseconds
                    #so i do them 3-digit and 2 digit again later
                    line[5] = line[5] + '0'
                    line[9] = line[9] + '0'
                    time_line = SubTime(seconds, milliseconds, minutes)
                    first_timecode = time_line.timechanger(line, 5)
                    next_timecode = time_line.timechanger(first_timecode, 9)
                    #Don't know is this necessary or not.
                    line[5] = line[5][:-1]
                    line[9] = line[9][:-1]
                    print('%s:%s,%s:%s:%s.%s,%s:%s:%s.%s,%s' %
                  (line[0], line[1],
                   line[2], line[3], line[4], line[5], line[6], line[7],
                   line[8], line[9], line[10]), end='', file=n_f)
                else:
                    print(line, end='', file=n_f)
