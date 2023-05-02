import calendar

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        leap_years = {i for i in range(1970, 2101) if calendar.isleap(i)}
        months_count = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        def f(date: str) -> int:
            y1, m1, d1 = 1970, 1, 1
            y2, m2, d2 = list(map(int, date.split('-')))
            diff = 0
            for year in range(y1, y2):
                diff += 365 + int(year in leap_years)
            for month in range(m2-1):
                diff += months_count[month] + int(month == 1 and calendar.isleap(y2))
            return diff + d2
        return abs(f(date1) - f(date2))