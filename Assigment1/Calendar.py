import os
import collections

'''

IMPORTANT NOTE: Do NOT change any of the function names or their signatures
(the parameters they take).
Your functions must behave exactly as described. Please check correctness by
running DocTests  included in function headers. You may not use any print or
input statements in your code.

Manage a calendar database.

A calendar is a dictionary keyed by date ("YYYY-MM-DD") with value being a list
of strings, the events on the specified date.

Example:
calendar["2017-10-12"] # is a list of events on "2017-10-12"

calendar["2017-10-12"]==["Eye doctor", "lunch with sid", "dinner with jane"]
'''


# -----------------------------------------------------------------------------
# Please implement the following calendar commands
# -----------------------------------------------------------------------------

def command_help():
    '''
    () -> str
    This function is already implemented. Please do not change it.
    Returns a help message for the system. That is...
    '''

    help = """
    Help for Calendar. The calendar commands are

    add DATE DETAILS               add the event DETAILS at the specified DATE
    show                           show all events in the claendar
    delete DATE NUMBER             delete the specified event (by NUMBER) from
                                   the calendar
    quit                           quit this program
    help                           display this help message

    Examples: user data follows command:

    command: add 2017-10-12 dinner with jane
    added

    command: show
        2017-10-12:
            0: Eye doctor
            1: lunch with sid
            2: dinner with jane
        2017-10-29:
            0: Change oil in blue car
            1: Fix tree near front walkway
            2: Get salad stuff, leuttice, red peppers, green peppers
        2017-11-06:
            0: Sid's birthday

    command: delete 2017-10-29 2
    deleted

    A DATE has the form YYYY-MM-DD, for example
    2017-12-21
    2016-01-02

    Event DETAILS consist of alphabetic characters,
    no tabs or newlines allowed.
    """
    return help


def command_add(date, event_details, calendar):
    '''
    (str, str, dict) -> str
    Add event_details to the list at calendar[date]
    Create date if it was not there

    date: A string date formatted as "YYYY-MM-DD"
    event_details: A string describing the event
    calendar: The calendar database
    return: empty string

    >>> calendar = {}
    >>> command_add("2017-02-28", "Python class", calendar)
    ''
    >>> calendar == {'2017-02-28': ['Python class']}
    True
    >>> command_add("2017-03-11", "CSCA08 test 2", calendar)
    ''
    >>> calendar == {'2017-03-11': ['CSCA08 test 2'], '2017-02-28':\
    ['Python class']}
    True
    >>> command_add("2017-03-11", "go out with friends after test", calendar)
    ''
    >>> calendar == {'2017-03-11': ['CSCA08 test 2', \
    'go out with friends after test'], '2017-02-28': ['Python class']}
    True
    >>>

    '''

    s = ""

    if date in calendar:
        calendar[date].append(event_details)
        save_calendar(calendar)
        return s and True
    else:
        calendar.update({date:[event_details]})
        save_calendar(calendar)
        return s and True

    # YOUR CODE GOES HERE



def command_show(calendar):
    '''
    (dict) -> str
    Returns the list of events for calendar sorted in increasing date order
    as a string, see examples below for a sample formatting
    calendar: the database of events

    Example:
    >>> calendar = {}
    >>> command_add("2017-02-12", "Eye doctor", calendar)
    ''
    >>> command_add("2017-02-12", "lunch with sid", calendar)
    ''
    >>> command_add("2017-03-29", "Change oil in blue car", calendar)
    ''
    >>> command_add("2017-02-12", "dinner with Jane", calendar)
    ''
    >>> command_add("2017-03-29", "Fix tree near front walkway", calendar)
    ''
    >>> command_add("2017-03-29", "Get salad stuff", calendar)
    ''
    >>> command_add("2017-05-06", "Sid's birthday", calendar)
    ''
    >>> command_show(calendar)
    "\n    2017-02-12:\n        0: Eye doctor\n        1: lunch with sid\n        2: dinner with Jane\n    2017-03-29:\n        0: Change oil in blue car\n        1: Fix tree near front walkway\n        2: Get salad stuff\n    2017-05-06:\n        0: Sid's birthday"
    '''
    # Hint: Don't use \t (the tab character) to indent, or DocTest will fail
    # in the above testcase.
    # Put 4 spaces before the date, 8 spaces before each item.


    s = '"'

    orderedCalendar = collections.OrderedDict(sorted(calendar.items()))



    for k,v in orderedCalendar.items():
        s = s +'\n' + k + ':'
        count =0
        for i in range(len(v)):
            s = s + '\n    ' + str(count) + ': ' + v[count]
            count = count+1
    return print(s+'"')


def command_delete(date, entry_number, calendar):
    '''
    (str, int, dict) -> str
    Delete the entry at calendar[date][entry_number]
    If calendar[date] is empty, remove this date from the calendar.
    If the entry does not exist, do nothing
    date: A string date formatted as "YYYY-MM-DD"
    entry_number: An integer indicating the entry in calendar[date] to delete
    calendar: The calendar database
    return: a string indicating any errors, "" for no errors

    Example:

    >>> calendar = {}
    >>> command_add("2017-02-28", "Python class", calendar)
    ''
    >>> calendar == {'2017-02-28': ['Python class']}
    True
    >>> command_add("2017-03-11", "CSCA08 test 2", calendar)
    ''
    >>> calendar == {'2017-03-11': ['CSCA08 test 2'], '2017-02-28':\
    ['Python class']}
    True
    >>> command_add("2017-03-11", "go out with friends after test", calendar)
    ''
    >>> calendar == {'2017-03-11': ['CSCA08 test 2', \
    'go out with friends after test'], '2017-02-28': ['Python class']}
    True
    >>> command_delete("2015-01-01", 1, calendar)
    '2015-01-01 is not a date in the calendar'
    >>> command_delete("2017-03-11", 3, calendar)
    'There is no entry 3 on date 2017-03-11 in the calendar'
    >>> command_delete("2017-02-28", 0, calendar)
    ''
    >>> calendar == {'2017-03-11': ['CSCA08 test 2', \
    'go out with friends after test']}
    True
    >>> command_delete("2017-03-11", 0, calendar)
    ''
    >>> calendar == {'2017-03-11': ['go out with friends after test']}
    True
    >>> command_delete("2017-03-11", 0, calendar)
    ''
    >>> calendar == {}
    True

    '''



    # check if the calendar has the key
    def has_key(value):
        key = calendar.get(value)
        if key is not None:                         # if the value of the key passed is NOT equal to null( means DOES have the key) returns True
            return True
        else:
            return False                            # if the value of the key passed IS equal to NULL returns False


    if has_key(date):                               # if the function is True
        values = calendar.get(date)                 # returns the values of this key in a list


        if len(values) > 1:                         # if the value passed is more we need to loop through to find the index we need to delete
            num = 0                                 # init a count to keep track of the loop
            for i in range(len(values)):            # then loop trough the values on a list
                if int(entry_number) == num:         # when the value passed is equal to the current index on the loop
                    values.remove(values[num])      #remove that value from the list
                    num = num + 1
                    save_calendar(calendar)
                    return ""
                else:
                    return"There is no entry "+ str(entry_number) +" on date 2017-03-11 in the calendar"

        else:
            calendar.pop(date)
            save_calendar(calendar)
            return ""
    else:
        return date+" is not a date in the calendar"



# -----------------------------------------------------------------------------
# Functions dealing with calendar persistence
# -----------------------------------------------------------------------------

'''
The calendar is read and written to disk.

...

date_i is "YYYY-MM-DD"'
description can not have tab or new line characters in them.

 
'''


def save_calendar(calendar):
    '''
    (dict) -> bool
    Save calendar to 'calendar.txt', overwriting it if it already exists.

    The format of calendar.txt is the following:

    date_1:description_1\tdescription_2\t...\tdescription_n\n
    date_2:description_1\tdescription_2\t...\tdescription_n\n
    date_3:description_1\tdescription_2\t...\tdescription_n\n
    date_4:description_1\tdescription_2\t...\tdescription_n\n
    date_5:description_1\tdescription_2\t...\tdescription_n\n

    Example: The following calendar...

        2017-02-28:
            0: Python class
        2017-03-11:
            0: CSCA08 test 2
            1: go out with friends after test

    appears in calendar.txt as ...

    2017-02-28:Python class
    2017-03-11:CSCA08 test 2    go out with friends after test

    calendar: dictionary containing a calendar
    return: True if the calendar was saved.
    Normally we should return False otherwise, however we have not
    learned yet how to handle errors. Therefore there will be no testing
    for cases when the save_calendar operation can fail. Also there is no
    need to provide error handling code. You may if you like, however
    no extra credit will be given, and additionally, you may have to
    explain to the grader/instructor in full how did you do the handling.
    '''
    # YOUR CODE GOES HERE

    with open("calendar.txt", 'w') as file:
        for key in sorted(calendar):
                file.write(key + ":" + ",".join(calendar[key]) + "\n")




def load_calendar():
    '''
    () -> dict
    Load calendar from 'calendar.txt'. If calendar.txt does not exist,
    create and return an empty calendar. For the format of calendar.txt
    see save_calendar() above. Please observe there are cases when
    the load_calendar operation can fail. There is no
    need to provide error handling code. You may if you like, however
    no extra credit will be given, and additionally, you may have to
    explain to the grader/instructor in full how did you do the handling.
    In case you decide to do error handling, you must return an empty
    calendar in case of various errors.

    return: calendar.

    '''

    # YOUR CODE GOES HERE
    file = "calendar.txt"
    if os.path.isfile(file):  # if the file exist    !
        calendar = {}  # create an empty dictionary
        if os.stat(file).st_size is not 0:  # if there is any content in the calendar.txt
            with open("calendar.txt", "r") as file:  # open it
                for line in file:  # loop
                    result = line.split(":")  # split the line by: where after : will be the values and before the key
                    result2 = result[1].replace("\n", "")
                    result3 =result2.split(",")
                    calendar.update({result[0]: result3})  # update the calendar with the values on the file

    else:
        calendar = {}  # if the file does not exist create an empty calendar

    return calendar  # return the calendar


# -----------------------------------------------------------------------------
# Functions dealing with parsing commands
# -----------------------------------------------------------------------------


def is_command(command):
    '''
    (str) -> bool
    Return whether command is indeed a command, that is, one of
    "add", "delete", "quit", "help", "show"
    You are not allowed to use regular expressions in your implementation.
    command: string
    return: True if command is one of ["add", "delete", "quit", "help", "show"]
    false otherwise
    Example:
    >>> is_command("add")
    True
    >>> is_command(" add ")
    False
    >>> is_command("List")
    False

    '''

    if command == "add" or command == "help" or command == "quit" or command == "delete" or command == "show":
        return True
    else:
        return False
    pass


def is_calendar_date(date):
    '''
    (str) -> bool
    Return whether date looks like a calendar date
    date: a string
    return: True, if date has the form "YYYY-MM-DD" and False otherwise
    You are not allowed to use regular expressions in your implementation.
	Also you are not allowed to use isdigit() or similar functions.

    Example:

    >>> is_calendar_date("15-10-10") # invalid year
    False
    >>> is_calendar_date("2015-10-15")
    True
    >>> is_calendar_date("2015-5-10") # invalid month
    False
    >>> is_calendar_date("2015-15-10") # invalid month
    False
    >>> is_calendar_date("2015-05-10")
    True
    >>> is_calendar_date("2015-10-55") # invalid day
    False
    >>> is_calendar_date("2015-55") # invalid format
    False
    >>> is_calendar_date("jane-is-gg") # YYYY, MM, DD should all be digits
    False

    Note: This does not validate days of the month, or leap year dates.

    >>> is_calendar_date("2015-04-31") # True even though April has only 30 days.
    True

    '''
    # Algorithm: Check length, then pull pieces apart and check them. Use only
    # basic string
    # manipulation, comparisons, and type conversion. Please do not use any
    # powerful date functions
    # you may find in python libraries.
    # 2015-10-12
    # 0123456789

    # YOUR CODE GOES HERE

    # check if there is the format date is right in general

    if len(date) == 10:
        dateList = date.split("-")
        year = dateList[0]
        month = dateList[1]
        day = dateList[2]
        if is_natural_number(year) and len(year) == 4:
            if is_natural_number(month) and len(month) == 2:
                monthInt = int(month)
                if monthInt > 0 and monthInt <= 12:
                    if is_natural_number(day) and len(day) == 2:
                        dayInt = int(day)
                        if dayInt > 0 and dayInt < 32:
                            return True
                        else:
                            return False
                else:
                    return False
            else:
                return False


        else:
            return False

    else:
        return False


def is_natural_number(str):
    '''
    (str) -> bool
    Return whether str is a string representation of a natural number,
    that is, 0,1,2,3,...,23,24,...1023, 1024, ...
    In CS, 0 is a natural number
    param str: string
    return: True if num is a string consisting of only digits. False otherwise.
    Example:

    >>> is_natural_number("0")
    True
    >>> is_natural_number("05")
    True
    >>> is_natural_number("2015")
    True
    >>> is_natural_number("9 3")
    False
    >>> is_natural_number("sid")
    False
    >>> is_natural_number("2,192,134")
    False

    '''
    # Algorithm:
    # Check that the string has length > 0
    # Check that all characters are in ["0123456789"]

    # YOUR CODE GOES HERE

    try:
        int(str)
        return True
    except ValueError:
        return False


def parse_command(line):
    '''
    (str) -> list
    Parse command and arguments from the line. Return a list
    [command, arg1, arg2, ...]
    Return ["error", ERROR_DETAILS] if the command is not valid.
    Return ["help"] otherwise.
    The valid commands are

    1) add DATE DETAILS
    2) show
    3) delete DATE NUMBER
    4) quit
    5) help

    line: a string command
    return: A list consiting of [command, arg1, arg2, ...].
    Return ["error", ERROR_DETAILS], if
    line can not be parsed.

    Example:
    >>> parse_command("add 2015-10-21 budget meeting")
    ['add', '2015-10-21', 'budget meeting']
    >>> parse_command("")
    ['help']
    >>> parse_command("not a command")
    ['help']
    >>> parse_command("help")
    ['help']
    >>> parse_command("add")
    ['error', 'add DATE DETAILS']
    >>> parse_command("add 2015-10-22")
    ['error', 'add DATE DETAILS']
    >>> parse_command("add 2015-10-22 Tims with Sally.")
    ['add', '2015-10-22', 'Tims with Sally.']
    >>> parse_command("add 2015-10-35 Tims with Sally.")
    ['error', 'not a valid calendar date']
    >>> parse_command("show")
    ['show']
    >>> parse_command("show calendar")
    ['error', 'show']
    >>> parse_command("delete")
    ['error', 'delete DATE NUMBER']
    >>> parse_command("delete 15-10-22")
    ['error', 'delete DATE NUMBER']
    >>> parse_command("delete 15-10-22 1")
    ['error', 'not a valid calendar date']
    >>> parse_command("delete 2015-10-22 3,14")
    ['error', 'not a valid event index']
    >>> parse_command("delete 2015-10-22 314")
    ['delete', '2015-10-22', '314']
    >>> parse_command("quit")
    ['quit']

    '''

    # HINT: You can first split, then join back the parts of
    # the final argument.
    # YOUR CODE GOES HERE

    errorList = ["error", ""]
    if line =="not a command" or line == "help":
        command_help()
        ans = ["help"]
        return ans
    elif line == "add":
        errorList[1] = "add DATE DETAILS"
        return errorList
    elif line == "quit":
        ans = ["quit"]
        return ans
    elif line == "show":
        ans = ["show"]
        return ans
    elif line == "delete":
        errorList[1] = "delete DATE NUMBER"
        return errorList
    elif line == "show calendar":
        errorList[1] = "show"
        return errorList
    else:
        lineList = line.split()
        final = len(lineList)
        if final > 1:
            description = " ".join(lineList[2:final])
            list = [lineList[0], lineList[1], description]
            if list[0] == "add":
                if is_command(list[0]) == True:
                    if list[2] != "":
                        if is_calendar_date(list[1]) == True:
                            if list[1] != "":
                                command_add(list[1], list[2], load_calendar())
                                return list
                            else:
                                errorList[1] = "add DATE DETAILS"
                                return errorList
                        else:
                            errorList[1]= "not a valid calendar date"
                            return errorList
                    else:
                        errorList[1] = "add DATE DETAILS"
                        return errorList
            elif is_command(list[0]) == True:
                if list[2] != "" and list[0] == "delete" :
                    if is_calendar_date(list[1]):
                        if is_natural_number(list[2]):
                            listresult =[list[0],list[1],list[2]]
                            parse_command(command_delete(list[1],list[2],load_calendar()))
                            return listresult
                        else:
                            errorList[1] = "not a valid event index"
                            return errorList
                    else:
                        errorList[1] = "not a valid calendar date"
                        return errorList
                else:
                    errorList[1] = "delete DATE NUMBER"
                    return errorList

        else:

            command_help()
            ans = ["help"]
            return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
