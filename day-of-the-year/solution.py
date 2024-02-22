import calendar

class Solution:
    def dayOfYear(self, date: str) -> int:
        daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
        cal = date.split('-')
        year = int(cal[0])
        month = int(cal[1])
        day = int(cal[2])

        dayInYear = day
        for i in range(0, month - 1):
            dayInYear += daysInMonth[i]

        if (calendar.isleap(year)):
            if (month > 2):
                dayInYear += 1
        return dayInYear
