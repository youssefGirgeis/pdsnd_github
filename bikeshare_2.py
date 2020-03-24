import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    cities = ['chicago', 'new york city', 'washington'] # list of the three cities
    # the loop below to get and check user's input (city)
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n')
        if city.lower() not in cities: # check if city entered by the user is in the lis above
            print('Please enter the correct city name (Chicago, New York City, or Washington)')
        else:
            city = city.replace(' ', '_') # for new york city's case 
            break
    
    choices = ['month', 'day', 'both', 'none'] # list of filters 
    while True:
        choice = input('Would like to filter the date by "month", "day", "both", or not at all? Type "none" for no time filter\n')
        if choice.lower() not in choices: #check if the filter entered by the user in list of filers above
            print('Please enter the correct filter name (month, day, both, none)')
        else:
            break 
    
    if choice.lower() == 'both':

    # TO DO: get user input for month (all, january, february, ... , june)
        month = check_month() # calling the function check_month
        day = check_day() # calling the function check_day

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    elif choice.lower() == 'month':
        month = check_month()
        day = ''
    elif choice.lower() == 'day':
        day = check_day()
        month = ''
    elif choice.lower() == 'none':
        month = ''
        day = ''

    print('-'*40)
    return city, month, day

def check_month():
    """
    get and check the month entered by the user

    Returns 
        the month to filter the dataframe
    """

    months = ['january', 'february', 'march', 'april', 'may', 'june'] # list of the six months
    while True:
        month = input('Which month? January, February, March, April, May, or June?\n')
        if month.lower() not in months:
            print('Please enter the correct month name (January, February, March, April, May, or June)')
        else:
            break
    return month

def check_day():
    """
    get and check the day entered by the user

    Returns
        day of the week to filter the dataframe 
    """

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] # list of days of week
    while True:
        day = input('which day? monday, tuesday, wednesday, thursday, friday, saturday, sunday\n')
        if day.lower() not in days:
            print('Please enter the correct day (monday, tuesday, wednesday, thursday, friday, saturday, sunday)')
        else:
            break
    return day 

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    months = ['january', 'february', 'march', 'april', 'may', 'june']

    filename = city.lower()+'.csv' # file to load the dataframe from
    df = pd.read_csv(filename) # loading the dataframe

    df['End Time'] = pd.to_datetime(df['End Time']) #convert "End Time column" to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time']) #convert "Start Time" column to datetime
    df['month'] = df['Start Time'].dt.month # create a new column "month" in the df
    df['day'] = df['Start Time'].dt.weekday_name #create a new column "day" in the df
    df['hour'] = df['Start Time'].dt.hour #create a new column "hour" in the df

    

    if day == '' and len(month) > 0: # if the user chooses to filter by month only
        month_number = months.index(month.lower())+1 # get the number of the month
        df = df[(df['month'] == month_number)]
    elif month == '' and len(day) > 0: # if the user chooses to filter by day only
        df = df[df['day'] == day.title()]
    elif len(month) > 0 and len(day) > 0: # if the user chooses to filter by both
        month_number = months.index(month.lower())+1 # get the number of the month
        df = df[(df['month'] == month_number) & (df['day'] == day.title())]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month: ', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('The most common day: ', df['day'].mode()[0])

    # TO DO: display the most common start hour
    print('The most common start hour: ', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most commonly used end station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_station'] = df['Start Station'] + '-' + df['End Station']
    start_end_station = df['start_end_station'].mode()[0].split('-')
    print('The most frequent combination of start station and end station: ', start_end_station[0] + ' and ' + start_end_station[1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: ', df['Trip Duration'].sum()) # the sum of column "Trip duration"

    # TO DO: display mean travel time
    print('Average travel time: ', df['Trip Duration'].mean()) # average of the trip duration 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts()) # displays counts of user types (customer or subscriber)

    # TO DO: Display counts of gender

    if 'Gender' in df.columns: # in case user chooses washington
        print(df.Gender.value_counts()) # displays the counts of gender

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns: # in case user chooses washington
        print('The most common year of birth: ', df['Birth Year'].mode()[0])
        print('The earliest year of birth', df['Birth Year'].min())
        print('The most recent year of birth: ', df['Birth Year'].max())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    """
    View sample of the raw data in the daraframe
    """
    while True:
        show = input('would you like to view individual trip? "yes" or "no"\n') # if user wants to view raw data
        if show.lower() == 'yes':
            print(df.sample(5).to_string())
        else:
            break

def main():
    while True:
        city, month, day = get_filters() # get city, month, day
        df = load_data(city, month, day) # load dataframe
        time_stats(df) # calaculate time stats
        station_stats(df) # calculate stations stats
        trip_duration_stats(df) #calculate trip duaration 
        user_stats(df) #calculate user stats

        view_data(df) 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
