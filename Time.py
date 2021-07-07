import time

class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):
        return f"{hours}:{minutes}:{seconds}"

    def get_time(self):
        hh = self.hours
        mm = self.minutes
        ss = self.seconds
        if self.hours < 10:
            hh = f'0{self.hours}'
        if self.minutes < 10:
            mm = f'0{self.minutes}'
        if self.seconds < 10:
            ss = f'0{self.seconds}'
        return time_t.set_time(hh, mm, ss)

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0
        return Time.get_time(self)



time_t = Time(17, 8, 00)
time_t.next_second()
for _ in range(60**3):
    time.sleep(1)
    print(f'\r{time_t.next_second()}', end="")


# print('Start.')
# for _ in range(61):
#     time.sleep(1)
#     print('\rDownloading File FooFile.txt [%d%%]'% _, end="")
# print('\nDone.')

