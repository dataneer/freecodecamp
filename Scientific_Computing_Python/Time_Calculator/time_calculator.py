
"""
Write a function named `add_time` that takes in two required
parameters and one optional parameter:
* a start time in the 12-hour clock format (ending in AM or PM)
* a duration time that indicates the number of hours and minutes
* (optional) a starting day of the week, case insensitive

The function should add the duration time to the start time and
return the result.

If the result will be the next day, it should show `(next day)`
after the time. If the result will be more than one day later,
it should show `(n days later)` after the time, where "n" is
the number of days later.

If the function is given the optional starting day of the
week parameter, then the output should display the day of
the week of the result. The day of the week in the output
should appear after the time and before the number of days
later.

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
"""

def add_time(start, duration, weekday=None):

    # we need four variables that need the respective times added to them
    start_hour = 0
    start_min = 0
    dur_hour = 0
    dur_min = 0

    # --- convert start and duration to military time ---

    # check if the start is AM or PM meridian

    # make a list of start time for result of ['##:##', **]
    start_list = start.split(' ')
    # split the start ''##:##'' into seperate numbers and convert to integers
    # resulting ['##', '##'] and adding to variables
    start_time = start_list[0].split(':')

    # store the military starting hour in a variable
    # store the starting min in a variable
    start_hour = start_hour + int(start_time[0])
    start_min = start_min + int(start_time[1])

    # if PM add +12 else append to a variable converting to military time
    if 'PM' in start_list[1]:
        start_hour = int(start_time[0]) + 12
    else:
        start_hour = int(start_time[0])

    # --- calculate a new time based on input duration ---

    # store the duration hour and minute in variables
    duration_list = duration.split(':')
    dur_hour = int(duration_list[0])
    dur_min = int(duration_list[1])

    # check to see if another hour should be added based on minutes
    # Example: if start min is 50 and dur min is 20 that results in
    # 70 which should become 60 and 10 and then the 60 adds a 1
    # to start hour omg this is so overwhelming

    # first add the hours
    # we need add hours to make caluclations in optional weekday
    # argument section
    add_hour = start_hour + dur_hour

    # create new_hour integer variable and append
    # also check if add hours is between 0 or 24
    new_hour = int()
    if add_hour > 24:
        new_hour = add_hour - 24
    else:
        new_hour = add_hour

    # logic: start minute + duration minutes
    # we need add minutes to make calculations in option weekday
    # argument section
    add_minute = start_min + dur_min

    # if the new minute is greater than to or equal 60 add 1 to
    # new hour and subtract 60 from new_minute
    new_minute = add_minute
    if new_minute >= 60:
        new_hour = new_hour + 1
        # this line of code is necessary to calculate
        # if add_hour > 24 and add_hour < 48:
        add_hour = add_hour + 1
        new_minute = new_minute - 60

    # ensure new_hour is between 0 or 24
    # this section of code has to run after adding start and duration
    # minute because it may add 1 to 24
    if new_hour > 24:
        new_hour = new_hour % 24

    # --- get the result in military time but then tranform ---
    # --- back into resulting meridian time ---


    # if new_hour greater than or equal to 13 meridian is PM
    # also subtract 12 from new_hour
    # else meridian is  AM

    # this part is wack but idk how else I would do it
    meridian = str()
    if new_hour == 12 and add_minute > 60:
        meridian = 'PM'
    elif new_hour == 24 and add_minute > 60:
        meridian = 'AM'
    elif new_hour >= 13:
        meridian = 'PM'
    else:
        meridian = 'AM'

    # change new_hour from military time back to civilian time
    if new_hour >= 13:
        new_hour = new_hour - 12


    # condition of return x days later if duration is greater than 24
    # this calculates ow many x days later it is
    div_dur_hour = 0
    if dur_hour > 12 and 'PM' in start_list[1]:
        # add 12 to account for additional 12 hours
        dur_hour = dur_hour + 12
        div_dur_hour = round(dur_hour / 24)
    elif dur_hour > 24 and 'AM' in start_list[1]:
        div_dur_hour = round(dur_hour / 24)

    # if add_hour is between 24 and 48 return (next day)
    if add_hour > 24 and add_hour < 48:
        new_time = '{}:{:02d} {} (next day)'.format(
                    new_hour, new_minute, meridian)
    # else div_dur_hour does not equal 0 that means it's at least more than
    # 48 hours regardless AM or PM
    elif div_dur_hour != 0:
        new_time = '{}:{:02d} {} ({} days later)'.format(
                    new_hour, new_minute, meridian, div_dur_hour)
    else:
        new_time = '{}:{:02d} {}'.format(
                    new_hour, new_minute, meridian)

    # --- optional weekday argument ---

    # check if optional weekday is inputted and save that weekday
    # string into a variable

    # create a weekday list to index through
    weekday_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday']

    # run this entire section code on condition that weekday argument
    # is inputted by user
    # stores secondary argument as a string and capitalize correctly
    # so we can compare the string to weekday list index
    if weekday is not None:
        weekday_str = str(weekday).capitalize()

        # store weekday_list index in an element by matching string
        for i in weekday_list:
            if i in weekday_str:
                start_index = weekday_list.index(weekday_str)

        # now we have to figure based on new how if the result should
        # return '(next day)' or '(x days later)'

        # NOTE:
        # A problem I really faced was I wasn't sure how to go from
        # an end index to the beginning such as:
        # in the state date was Saturday and ended on Sunday
        # Do I have to use negative indexing somehow if the
        # variable is over 6?
        # How would I know how much to subtract?

        # Ok so I should think of my list on an inverse?
        # Saturday is weekday_list[6] and also weekday_list[-1]
        # Sunday is weekday_list[0] and also weekday_list[-7]
        # Maybe I'm just overthinking and need to subtract enough
        # based no the positive index

        # . . .

        # After some time of struggling my more intelligent friend helped
        # me at this part

        # I have to use quotient and mod to return the index I need from
        # weekday_list

        # use already established variables of add_hour and add_minute to
        # do the same calculations which isn't efficeint I know but
        # I'm already down this road and I don't want to re-Write
        # the code and we need an u

        # First we need a hour variable that's added the start and duration hours
        # and we first see if minute is more than 60 then add 1 hour to
        # index hour which we have set at the already calucated add_hour
        index_hour = add_hour
        if add_minute > 60:
            index_hour = index_hour + 1

        # Now we need to get the quotient of index hour divided by 24 hours
        # // operator is floor division
        quotient_hour = index_hour // 24

        # Sum start_index and quotient hours
        sum_start_quot = start_index + quotient_hour

        # Find the mod of sum_start_quot divded by 7 days in a weekday
        # this is the end index and will work even if the start is end
        # of the week like Friday or Saturday
        end_index = sum_start_quot % 7

        new_day = weekday_list[end_index]

        # return new_day into the new_time results
        # determine if the index falls on the next day by subtracting them
        # end_index and start_index to see if equals 1

        if end_index - start_index == 1 or end_index - start_index == -6    :
            new_time = '{}:{:02d} {}, {} (next day)'.format(
                    new_hour, new_minute, meridian, new_day)
        # else
        elif div_dur_hour != 0:
            new_time = '{}:{:02d} {}, {} ({} days later)'.format(
                    new_hour, new_minute, meridian, new_day, div_dur_hour)
        else:
            new_time = '{}:{:02d} {}, {}'.format(
                    new_hour, new_minute, meridian, new_day)

    # send the result of the function back to the caller
    return new_time

print('add_time("2:59 AM", "24:00", "saturDay")')
print(add_time("2:59 AM", "24:00", "saturDay"))
