import Calendar as calendar
from Calendar import *

# ----------------------------------------------------------------------------
# Functions dealing with the user. This is the calendar application.
# Please do use input and print as needed in order to provide a
# nice and meaningful user interaction with your application.
# ----------------------------------------------------------------------------


def user_interface():
    '''
    Load calendar.txt and then interact with the user. The user interface
    operates as follows, the text after command: is the command entered by the
    user.
    calendar loaded
    command: add 2017-10-21 budget meeting
    added
    command: add 2017-10-22 go to the gym
    added
    command: add 2017-10-23 go to the gym
    added
    command: add 2017-11-01 Make sure to submit csc108 assignment 2
    added
    command: add 2017-12-02 Make sure to submit csc108 assignment 3
    added
    command: add 2017-11-06 Term test 2
    added
    command: add 2017-10-29 Get salad stuff,lettuce, red peppers, green peppers
    added
    command: add 2017-11-06 Sid's birthday
    added
    command: show

        2017-10-21:
            0: budget meeting
        2017-10-22:
            0: go to the gym
        2017-10-23:
            0: go to the gym
        2017-10-29:
            0: Get salad stuff, leuttice, red peppers, green peppers
        2017-11-01:
            0: Make sure to submit csc108 assignment 2
        2017-11-06:
            0: Term test 2
            1: Sid's birthday
        2017-12-02:
            0: Make sure to submit csc108 assignment 3
    command: delete 2017-10-29 0
    deleted
    command: delete 2015-12-03 0
    2015-12-03 is not a date in the calendar
    command: delete 2017-12-02 0
    deleted
    command: show

        2017-10-21:
            0: budget meeting
        2017-10-22:
            0: go to the gym
        2017-10-23:
            0: go to the gym
        2017-11-01:
            0: Make sure to submit csc108 assignment 2
        2017-11-06:
            0: Term test 2
            1: Sid's birthday
    command: quit
    calendar saved

    :return: None
    '''




    def menu():
        print("<------------ CALENDAR APP -------------->")
        print()
        print("1)- ADD an event in the calendar")
        print("2)- SHOW the events in the calendar")
        print("3)- DELETE an event in the calendar")
        print("4)- QUIT the calendar")
        print("5)- HELP the program")
        print()

        print("Welcome to Calendar app. Please enter your command above")

        dic = calendar.load_calendar()
        while (True):
            cmd = input("Command:")
            split = calendar.parse_command(cmd)
            if calendar.is_command(split[0]):
                if split[0] == "add":
                    calendar.command_add(split[1], split[2], dic)
                    print("added")
                elif cmd == "save":
                    calendar.save_calendar(dic)
                    print("calendar saved")
                elif split[0] == "show":
                    print(calendar.command_show(dic))
                elif split[0] == "delete":
                    returnStr = calendar.command_delete(split[1], split[2], dic)
                    if returnStr == "":
                        print("deleted")
                    else:
                        print(returnStr)
                elif split[0] == "quit":
                    calendar.save_calendar(dic)
                    print("calendar saved")
                    return
                else:
                    print(calendar.command_help())

            elif split[0] == "error":
                print(split[1])

    menu()



if __name__ == "__main__":
    user_interface()

