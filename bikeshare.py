import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_LIST = ['january', 'february', 'march','april','may', 'june','all']
DAYS_LIST = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

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
        
    city = input("Which city you would like to analyze? Please choose one of the following cities (chicago, new york city, washington) \n").lower()      
    while city not in CITY_DATA:
        print('Your input is invalid!')
        city = input("Which city you would like to analyze? Please choose one of the following cities (chicago, new york city, washington) \n").lower()
            
    print("you've entered: ", city)

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month you would like to analyse, please enter an input from January to June or "All" in case you want all of them \n').lower()
    while month not in MONTH_LIST:
        print('Your input is invalid!')
        month = input('Which month you would like to analyse, please enter an input from January to June or "All" in case you want all of them \n').lower()
        
    print("you've entered: ", month)   


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day you would like to analyse? or "All" in case you need the full week \n').lower()
    while day not in DAYS_LIST:
         print('Your input is invalid!')
         day = input('Which day you would like to analyse? or "All" in case you need the full week \n').lower()
        
    print("you've entered: ", day)

    print('-'*40)
    return city, month, day


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
   # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The Most Common Month is: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The Most Common day is: ', most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The Most Common Start Hour is:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    most_common_start_station = df['Start Station'].mode().values[0]
    print('The Most Common Start Station is: ', most_common_start_station)
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode().values[0]
    print('The Most Common End Station is: ', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station']+ " " + df['End Station']
    print('The Most Frequent Combination Of Start Station And End Station Trip is: \n', df['combination'].mode().values[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    try:
        df['total_duration'] = df['End Time'] - df['Start Time']
        total_time_travel = df['total_duration'].sum()
        print("Total travel time is: ", total_time_travel)
    except:
        print("couldn't load the total travel time as an error occured")

    # TO DO: display mean travel time
    try:
        Mean = df['total_duration'].mean()
        print("Mean travel time is: ", Mean)
    except:
        print("couldn't load the mean travel time as an error occured")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)  
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The counts of user types:\n', user_types)

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('The counts of user types:\n', gender_types)
    except:
        print('there is no data available for "Gender" in this city')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("The earliest year of birth is: ", df['Birth Year'].min())
        print("The most recent year of birth is: ", df['Birth Year'].max())
        print("The most common year of birth is: ", df['Birth Year'].mode().values[0])
    except:
        print('there is no data available for "Birth Year" in this city')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    end_loc = 5
    if view_data == 'yes':
        while end_loc <= df.shape[0] - 1:
            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5
            view_display = input("Do you wish to continue?: yes or no\n").lower()
            if view_display == 'no':
                break
           

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
