# This file has a few mistakes and some things I forgot to put in.
# When I run it I don't get anything... can you fix it so I
# get asked for my vacation spot, and get a recommendation?
# Hint:
# Start at the bottom and work upwards.


vacation_spots = ['Tahoe', 'Hawaii', 'New York', 'Mexico']
seasons = ['spring', 'summer', 'fall', 'winter', 'autumn']

weather_patterns = {
    'spring': 'rain',
    'summer': 'sun',
    'fall': 'wind',
    'winter': 'snow',
    'autumn':'wind'

}

activities = {
    'rain': 'visiting museums',
    'wind': 'kiteboarding',
    'sun': 'sunbathing',
    'snow': 'skiing'
}


def best_vacation_spot(weather_type):
    # Look at the weather type and return the vacation spot that
    # is the best for that weather.
    # You can use this mapping:
    if weather_type=='snow':
        vacation_spot='Tahoe'
        return 'Tahoe'
    elif weather_type=='wind':
        vacation_spot='Hawaii'
        return 'Hawaii'
    elif weather_type=='rain':
        vacation_spot='New York'
        return 'New York'
    elif weather_type=='sun':
        vacation_spot='Mexico'
        return 'Mexico'
    else:
        return "Stay at home"


def vacation_activity(weather_type):
    # Look up the vacation activity from activities
    # and return just the activity itself
    activity= activities[weather_type]
    return activity


def get_my_vacation():

    season = raw_input("What season do you want to travel? ").lower()

    # check if season is in the seasons list
    if season not in seasons:
        print "Sorry, that isn't a season. I can't help you."
        quit()
    # look up the weather type for that season
    weather = weather_patterns[season]

    # get the best vacation spot for that type
    vacation_spot = best_vacation_spot(weather)

    # get the best vacation activity for that type
    vacay_activity=vacation_activity(weather)

    print "You should travel to {}, where you can spend your time {}!".format(vacation_spot, vacay_activity)


def main():
    print "Welcome to the Vacation-o-Matic!"
    get_my_vacation()



if __name__=="__main__":
    main()