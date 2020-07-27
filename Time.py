class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.minutes = m
        self.seconds = s

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, right_h):
        if right_h > 23 or right_h < 0:
            self._hours = 23
        else:
            self._hours = right_h

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, right_m):
        if right_m > 59 or right_m < 0:
            self._minutes = 59
        else:
            self._minutes = right_m

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, right_s):
        if right_s > 59 or right_s < 0:
            self._seconds = 59
        else:
            self._seconds = right_s

    def __repr__(self):
        return f'{self.hours} : {self.minutes} : {self.seconds}'

    def __str__(self):
        return f'{self.hours} : {self.minutes} : {self.seconds}'


my_time = Time(14, 89, 34)
print(my_time)
