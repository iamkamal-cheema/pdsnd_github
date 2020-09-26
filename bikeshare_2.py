
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
    User_message = "Please check your input and enter a valid response"
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("We have data on chicago, new york city and washington; Pick a city and input the name:").lower()
        if city in ['new york city', 'washington', 'chicago']:
            break
        else:
            print(User_message)

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Narrow it dowan to a specific month? You may enter any of the first six months in a year or enter 'all':").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print(User_message)

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("Narrow it down to a specific day? Input specific day or else type 'all':").lower()
        if day in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
            break
        else:
            print(User_message)


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
     # loading data file into a dataframe
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

   # extract month and day from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filtering by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        All_months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = All_months.index(month) + 1

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

    # display the most common month
    print("Most common month for traveling: ", df['month'].mode()[0], "\n")

    # display the most common day of week
    print("Most common day for traveling: ", df['day_of_week'].mode()[0], "\n")

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("Most common start hour ", df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most commonly used start station: ", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("Most commonly used end station: ", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['Start_end'] = df['Start Station'] + " and " + df['End Station']
    print("Most frequent combination of start station and end station trip: ", df['Start_end'].mode()[0])



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

      # display total travel time
    print("Total travel time: ", df['Trip Duration'].sum(), "\n")

    # display mean travel time
    print("Total mean time:", df['Trip Duration'].mean())



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    UserType = df.groupby(['User Type'])['User Type'].count()
    print(UserType, "\n")
    if city != 'washington':
        # Display counts of gender
        gender_count = df.groupby(['Gender'])['Gender'].count()
        print(gender_count)
        # Display earliest, most recent, and most common year of birth
        early_birth = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        recent_birth = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        common_birth = df['Birth Year'].mode()[0]
        print("The earliest year of birth is ", early_birth, "\n")
        print("The most recent year of birth is ", recent_birth, "\n")
        print("The most common year of birth is ", common_birth, "\n")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    counter = 1
    while True:
        data_dump = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if data_dump.lower() == 'yes':
            print(df[counter:counter+5])
            counter += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
