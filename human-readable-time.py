def make_readable(seconds):
    hours = seconds // 3600
    rem_h = seconds % 3600
    mins = rem_h // 60
    secs = rem_h % 60
    return '{0:02}:{1:02}:{2:02}'.format(hours, mins, secs)
