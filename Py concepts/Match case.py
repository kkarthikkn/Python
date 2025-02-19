#match_case (similar to case stmt)

def weekday(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:     # _  --> Wildcard
            return "Invalid"


def weekend(day):
    match day:
        case 'Sunday' | 'Saturday':
            return "It's Weekend"
        case 'Monday' | 'Tuesday'| 'Wednesday'| 'Thursday'| 'Friday':
            return "It's Weekday"
        case _:
            return "Invalid"


week=int(input("Enter the number: "))
day= weekday(week)
print(day)
print(weekend(day))
#print(result)