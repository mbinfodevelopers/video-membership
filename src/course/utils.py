from .models import Course

def calculate_time(self):
    get_time = Course.objects.filter(video__duration_video=self)
    time = get_time % (24 * 1440)
    hour = time // 1440
    time %= 1400
    minute = time // 60
    time %= 60
    seconds = time
    result = ("h:m:s  %d:%d:%d" % (hour, minute, seconds))
    return result