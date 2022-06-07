import time
import pandas as pd
import  numpy as np
pd.set_option("Display.max_columns",None)

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York city': 'new_york_city.csv',
              'Washington': 'washington.csv' }
def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Please note that chicago has additional gender and birth years ")
    city="Empty"
    month="Empty"
    day="Empty"
    validmonths=["January","February","March","April","May","June","July","August","September","October","November","December"]
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while(city=="Empty"):
        city = input("Please Enter the name of a City (Chicago/New York/Washington)=")
        if city.capitalize()=="Chicago" or city.capitalize()=="New York" or city.capitalize()=="Washington" or city.capitalize()=="all":
          break
        else:
          print("Invalid City Name")
          city="Empty"

    # get user input for month (all, january, february, ... , june)
    while(month=="Empty"):
        month=input("Enter a Value for month=")
        if month.capitalize() in validmonths:
            break
        else:
            month="Empty"
            print("Please enter a valid month")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    valid_weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    while(day=="Empty"):
        day=input("Please Enter the Day to filter=")
        if day.capitalize() in valid_weekdays:
            break
        else:
            print("Invalid week day detected")
            day = "Empty"

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
    df=pd.read_csv(CITY_DATA[city.title()])
    df["Start Time"]=pd.to_datetime(df["Start Time"])
    df["Month"]=df["Start Time"].dt.month
    df["day of week"]=df["Start Time"].dt.day_name()
    if month!='all':
        months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        month=months.index(month.title())+1
        df=df[df["Month"]==month]
    if day!="all":
        df=df[df["day of week"]==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    #display the most common month
    most_common_month=df["Month"].mode()[0]
    print("The most common month is ="+str(months[most_common_month-1]))


    # display the most common day of week
    print("The most common Day of week is= "+df["day of week"].mode()[0])

    # display the most common start hour
    df["Hour"]=df["Start Time"].dt.hour
    most_common_hour=df["Hour"].mode()[0]
    print("The most common hour is="+str(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station=df["Start Station"].mode()[0]
    print("The most common used start station is="+most_common_start_station)

    # display most commonly used end station
    most_common_end_station=df["End Station"].mode()[0]
    print("The most common used end station is="+most_common_end_station)

    # display most frequent combination of start station and end station trip
    df["Start-End Stations"]=df["Start Station"]+" - "+df["End Station"]
    most_common_start_end_station_combination = df["Start-End Stations"].mode()[0]
    print("Most common Start-End combination="+most_common_start_end_station_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df["Trip Duration"].sum()
    print("Total Travel time= "+str(total_travel_time)+" Seconds")

    # display mean travel time
    mean_travel_time=df["Trip Duration"].mean()
    print("Mean Travel Time= "+str(mean_travel_time)+" Seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types=df["User Type"].value_counts()
    print("Distribution of each user type=\n "+str(user_types))

    print("Didn't Find User Type as a column in this DataFrame")

    if "Gender" in df:
    # Display counts of gender
        gender_types=df["Gender"].value_counts()
        print("Distribution for Each gender=\n "+str(gender_types))
    # Display earliest, most recent, and most common year of birth
    else:
        print("Didn't Find Gender as a column in this DataFrame")

    if "Birth Year" in df:
        earliest_birth_year = str(int(df['Birth Year'].min()))
        print("Earliest Detected birth year="+ earliest_birth_year)
        recent_birth_year=str(int(df["Birth Year"].max()))
        print("Recent birth year= "+recent_birth_year)
        most_common_birth_year=df["Birth Year"].mode()[0]
        print("Most common birth year= "+str(int(most_common_birth_year)))
    else:
        print("No Such Column with name Birth Year was found in the DataFrame")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data_output(starting_index,df):

    while True:
        for i in range(starting_index,len(df.index)):
            print("\n")
            print(str(df.iloc[starting_index:starting_index+5])+"\n")
            starting_index += 5  #Incrementing by 5
            choice = input("Do you want to keep printing the next 5 rows?[y/n]=")
            if choice=='y':
                continue
            else:
                break
        break
    return  starting_index
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data_output(0,df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
