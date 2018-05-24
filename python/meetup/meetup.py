from datetime import date
import calendar

def meetup_day(year, month, day_of_the_week, which):
    day_idx = list(calendar.day_name).index(day_of_the_week)

    list_of_days = [week[day_idx] for week in calendar.monthcalendar(year, month)
                                        if week[day_idx] != 0]
    
    day = 0

    if which == '1st': 
        day = list_of_days[0]
    elif which == '2nd': 
        day = list_of_days[1]
    elif which == '3rd': 
        day = list_of_days[2]
    elif which == '4th': 
        day = list_of_days[3]
    elif which == '5th':
        if len(list_of_days) < 5: 
            raise MeetupDayException('invalid day')
        day = list_of_days[4]
    elif which == 'last': 
        day = list_of_days[-1]
    elif which == 'teenth':
        list_of_teenths = list(filter((lambda n: n >= 13 and n <= 19), list_of_days))
        if len(list_of_teenths) < 1:
            raise MeetupDayException('invalid day')
        day = list_of_teenths[0]
    else:
        raise MeetupDayException('invalid day')

    return date(year, month, day)

class MeetupDayException(Exception):
    pass