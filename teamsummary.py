# TODO: Make dates customizable, support Chicago/New York two teams situation.
from pybaseball import batting_stats_range, pitching_stats

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
        'Angels':'Anaheim',
        'Mets':'New York',
        'Phillies':'Philadelphia',
        'Marlins':'Miami',
        'Braves':'Atlanta',
        'Nationals':'Washington',
        'Cardinals':'St Louis',
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

def retrieve_stats(team):
    batting = batting_stats_range('2019-04-01', '2019-09-14')
    pitching = pitching_stats(2019)

    print("***** BATTING STATS *****")
    print(batting[batting['Tm'] == city][['Name', 'PA', 'OPS', 'BA', 'OBP', 'SLG', 'HR']].sort_values('PA', ascending=False))

    print("")

    print("***** PITCHING STATS *****")
    print(pitching[pitching['Team'] == team][['Name', 'IP', 'WAR', 'FIP']].sort_values('IP', ascending=False))

team = None

while team is None:
    print("For which team would you like to retrieve data? (Enter the team nickname, not the city.)")
    team = input("> ")

    if team in teams.keys():
        city = teams[team]
        print(f"Looking up data for the {team} of {city}. This will just take a moment...")
        retrieve_stats(team)
        print("Would you like to retrieve data for another team? (Enter 'Y' or 'N'.)")
        rerun = input("> ")
        if rerun == 'Y':
            team = None
        else:
            print("Have a great day!")
    else:
        print("That is not a team!")
        team = None
