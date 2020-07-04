# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:46:16 2020

@author: petru
"""
#Organising Sorcery Society's Game Night
# 1. check availability of players
# 2. check which day most players are available
# 3. informing them of game night

# create a main list to house information on all our existing gamers
gamers = []

# create a function to append gamer entries that have the required keys “name”, “availability”, e.g. {"name":"Kara Danvers", "availability":["Friday", "Saturday", "Sunday"]}
# we'll name the parameters (gamer for 1 single gamer entry) and (valid_gamers for the list we are appending to)

def add_gamer(gamer, valid_gamers):
    if gamer.get("name") and gamer.get("availability"):
        valid_gamers.append(gamer)
    else:
        print("Gamer missing required information")       

# new gamer entry
kara_danvers = {"name":"Kara Danvers", "availability" : ["Friday", "Saturday", "Sunday"]}

# initiate add_gamer function to add new gamer to main list
add_gamer(kara_danvers, gamers)
add_gamer({"name":"Alex Danvers", "availability":["Monday", "Friday"]}, gamers)
add_gamer({"name":"Lena Luthor", "availability":["Saturday", "Sunday"]}, gamers)
add_gamer({"name":"Winnslow Schott", "availability":["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({"name":"James Olsen", "availability":["Wednesday", "Thursday", "Friday"]}, gamers)
add_gamer({"name":"Kelly Olsen", "availability":["Monday", "Tuesday", "Wednesday"]}, gamers)
add_gamer({"name":"Nia Nal", "availability":["Wednesday", "Thursday", "Friday"]}, gamers)
add_gamer({"name":"Querl Dox", "availability":["Wednesday", "Friday"]}, gamers)
add_gamer({"name":"Barry Allen", "availability":["Tuesday", "Wednesday", "Thursday"]}, gamers)
add_gamer({"name":"Iris West", "availability":["Tuesday", "Thursday"]}, gamers)
print(gamers)

# build a base day, availabilities counter with the count at 0
def build_daily_frequency_counter():
    return {"Monday":0, "Tuesday":0, "Wednesday":0, "Thursday":0, "Friday":0, "Saturday":0, "Sunday":0 }

daily_frequency_counter = build_daily_frequency_counter( )

# using the base counter we built, start to iterate the availability of each game and tally the counter
# the parameters are (the main list of gamers) and (the counter we are using)
def calculate_availability(valid_gamers, counter):
    for gamer in valid_gamers:
        for day in gamer['availability']:
            counter[day] += 1

calculate_availability(gamers, daily_frequency_counter)
#print(daily_frequency_counter)                                              

# create a function that picks the best day for game night, with one parameter (the counter)
def find_best_day(counter):
    best_avail = 0 
    for day, availability in counter.items():
        if availability > best_avail:
            best_day = day
            best_avail = availability
    return best_day

game_night = find_best_day(daily_frequency_counter)
print(game_night)

# create a function that generates a list of gamers names available on the day of game night, with the parameters (the main list) and (the best day)
# this is used in the emails send to gamers informing them about game night
def avail_on_day(valid_gamers, best_day):
    avail_gamers = []
    for gamer in valid_gamers:
        for value in gamer.values(): 
            if best_day in value:                                                   
                avail_gamers.append(gamer['name'])                           
    return avail_gamers

    # return [gamer for gamer in valid_gamers if best_day in gamer['availability’]]
    # you can use the above list comprehension if you want the name + availability

avail_game_night = avail_on_day(gamers, game_night)
print(avail_game_night)

# create variable for formatted email blast message
invite_email = """
Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week} and have a blast!

Magically Yours,
The Sorcery Society
"""

# create a function to send an invitation email for those who can make it to the chosen game night day, with the parameters (available attendees), (chosen day) and (the game)
def send_email(avail_attendees, chosen_day, game):
    for gamer in avail_attendees:
        print(invite_email.format(name = gamer, day_of_week = chosen_day, game = game))

send_email(avail_game_night, game_night, "Abruptly Goblins!")


# for gamers who couldn't attend, use list comprehension to sift them from the main list out into a separate list
# gamers who couldn't attend did not have the game night day in their available days
unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer['availability']]

# start a new day availability counter for those who couldn't attend for best day game night
# this counter will start at 0
second_night_avail_counter = build_daily_frequency_counter()
print(second_night_avail_counter)

# call the function that tallies the day availabilities of the remaining gamers
calculate_availability(unable_to_attend_best_night, second_night_avail_counter)
print(second_night_avail_counter)

# call the function to pick the best night tallied by the second counter
second_night = find_best_day(second_night_avail_counter)
print(second_night)

# create list of all the gamers available for the second game night picked
avail_second_game_night = avail_on_day(gamers, second_night)
# call the function to send them a notification email regardless if they are also avail for the best day game night
send_email(avail_second_game_night, second_night, "Abruptly Goblins!")

