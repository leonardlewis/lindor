# TODO: Make season customizable

import pandas as pd
from pybaseball import batting_stats, pitching_stats

pd.set_option('display.max_rows', 500)

teams = {
        'Indians':'Cleveland',
        'Twins':'Minnesota',
        'White Sox':'Chicago',
        'Royals':'Kansas City',
        'Tigers':'Detroit',
        'Yankees':'New York',
        'Red Sox':'Boston',
        'Orioles':'Baltimore',
        'Rays':'Tampa Bay',
        'Blue Jays':'Toronto',
        'Astros':'Houston',
        'Athletics':'Oakland',
        'Rangers':'Texas',
        'Mariners':'Seattle',
        'Angels':'Los Angeles',
        'Mets':'New York',
        'Phillies':'Philadelphia',
        'Marlins':'Miami',
        'Braves':'Atlanta',
        'Nationals':'Washington',
        'Cardinals':'St\. Louis',
        'Cubs':'Chicago',
        'Pirates':'Pittsburgh',
        'Reds':'Cincinnati',
        'Brewers':'Milwaukee',
        'Giants':'San Francisco',
        'Dodgers':'Los Angeles',
        'Diamondbacks':'Arizona',
        'Padres':'San Diego',
        'Rockies':'Colorado'
        }

def retrieve_stats(team, year):
    batting = batting_stats(year)
    pitching = pitching_stats(year)

    team_batting = batting[batting['Team'] == team][['Name', 'PA', 'WAR', 'wRC+', 'AVG', 'OBP', 'SLG', 'OPS', 'HR']].sort_values('PA', ascending=False)

    print("***** BATTING STATS *****")
    print(team_batting)

    print("")

    team_pitching = pitching[pitching['Team'] == team][['Name', 'IP', 'WAR', 'FIP']].sort_values('IP', ascending=False)

    print("***** PITCHING STATS *****")
    print(team_pitching)

team = None
year = None

while team is None:
    print("For which team would you like to retrieve data? (Enter the team nickname, not the city.)")
    team = input("> ")
    if team not in teams.keys():
        print("That is not a team!")
        team = None
    else:
        while year is None:
            print("For which year would you like to retrieve data? (Enter YYYY)")
            year = input("> ")
            city = teams[team]
            print(f"Looking up data for the {year} {team} of {city}. This will just take a moment...")
            retrieve_stats(team, year)
            print("Would you like to retrieve data for another team? (Enter 'Y' or 'N'.)")
            rerun = input("> ")
            if rerun == 'Y':
                team = None
                year = None
            else:
                print("Have a great day!")
