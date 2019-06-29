import os
import utility_functions as UF


def get_events_for_day(day, month, year):
    """
    Get event information for the events of the day
    :param day: day to query (int)
    :param month: month to query (int)
    :param year: year to query (int)
    :return: events (list)
    """
    # Type checking:
    UF.check_type(day, "int")
    UF.check_type(month, "int")
    UF.check_type(year, "int")

    # Querying information:
    command_string = "curl 'https://goffstownathletics.com/main/calendarDayAjax' -H 'origin: https://goffstownathletics.com' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9' -H 'x-requested-with: XMLHttpRequest' -H 'cookie: JSESSIONID=A437B190923E2C2C1845AF70D5346A7D.Main; erd=6B749E34B06E77B4303C2CF244678ECD; CALVIEW=month; CALDATE={m}/{d}/{y}; AWSALB=e/KIOyE3YhuKL9TvYnaun6DDc9LkzOc+G7+DLvkNdZ9KMu70lUN9dcxt0g5OwJoBLTJgglZ3Tk91OhPU7KZXRz9GUslWJ60RiMNq+6YgwEEwnvdQIGNPVfNKisoh' -H 'pragma: no-cache' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36' -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' -H 'accept: application/json, text/javascript, */*; q=0.01' -H 'cache-control: no-cache' -H 'authority: goffstownathletics.com' -H 'referer: https://goffstownathletics.com/main/calendar/' --data 'CalMonth={m}&CalYear={y}&CalDay={d}' --compressed".format(m=month, d=day, y=year)
    command = os.popen(command_string).read()

    # Cleaning output
    strip_l1 = command.strip(" ").strip("][")
    list_form = strip_l1.split("{")
    cleaned_elements = []
    for event in list_form:
        strip_l2 = event.strip(",").strip("}")
        cleaned_elements.append(strip_l2)
        print("\n" + strip_l2)
    return cleaned_elements


# Testing:
get_events_for_day(6, 6, 2019)


