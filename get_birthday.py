from datetime import datetime, timedelta
from operator import itemgetter

def get_birthdays_per_week(birthdays_list):
    today = datetime.today().date()
    congrat_list = []
    congrat_list_sorted = {}
    congrat_list_output = {}
    str_congrat = ''
    str_output = ''
    i = 0

    # get the list of birthdays for the current week
    for user in birthdays_list:
        birthdays_list_current_year = {}
        name = user["name"]
        birthday = datetime.strptime(user["birthday"],'%d.%m.%Y')
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year >= today:
            
            # check if the birth date is on weekdays
            check_day = birthday_this_year.strftime("%A")
            if check_day == 'Sunday':
                birthday_this_year = birthday_this_year + timedelta(days=1)
            if check_day == 'Saturday':
                birthday_this_year = birthday_this_year + timedelta(days=2)

            # check if the birth date is during the current week
            delta_days = (birthday_this_year - today).days
            if delta_days < 7:
                birthdays_list_current_year = {'name': name, 'birthday' : birthday_this_year} 
                congrat_list.append(birthdays_list_current_year)

    # get the sorted list of birthdays
    congrat_list_sorted = sorted(congrat_list, key=itemgetter('birthday')) 

    # get the dict with the names of the week in dict.key and user grouped by birthday usernames in dict.value
    for i in range(len(congrat_list_sorted)):
        value = congrat_list_sorted[i]['birthday'].strftime("%A")

        if value in congrat_list_output:
            congrat_list_output[value] += ', ' + congrat_list_sorted[i]['name']
        else:
            congrat_list_output[value] = congrat_list_sorted[i]['name']
        i += 1

    # convert of dict into output string
    for k, v in congrat_list_output.items():
        str_congrat = "".join(f"{k}: {v}")
        str_output += '\n' + str_congrat

    return congrat_list_output
 
