'''top 200 csv reader for drafting'''
from Tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import csv

Tk().withdraw()
file = askopenfilename()

file_name = os.path.basename(file)

available_player_list = []

with open(file, 'r') as transactions:
    csv_reader = csv.DictReader(transactions)

    player_info_list = []
    player_chosen = []

    for item in csv_reader:
        rank = item['Rk']
        player = item['Player']
        position = item['Pos']
        team = item['Team']
        bye = item['Bye']
        player_info = 'Rank|{} Player|{} Team|{} Position|{} Bye|{}'.format(rank, player, position, team, bye)
        player_info_list.append(player_info)
        available_player_list.append(player)

def search_player(name):
    with open(file, 'r') as transactions:
        csv_reader = csv.DictReader(transactions)
        for item in csv_reader:
            player_name = item['Player']
            if name in player_name:
                rank = item['Rk']
                player_name = item['Player']
                position = item['Pos']
                team = item['Team']
                bye = item['Bye']
                player_info = 'Rank|{} Player|{} Team|{} Position|{} Bye|{}'.format(rank, player, position, team, bye)
                return rank, player_name, position, team, bye, player_info

def add_team_player(player):
    try:
        my_team.append(player)
    except:
        error = 'error'
        # print error
    try:
        available_player_list.remove(player)
    except:
        error = 'error'
        # print error

def remove_team_player(player):
    try:
        my_team.remove(player)
    except:
        error = 'error'
        # print error
    try:
        available_player_list.append(player)
    except:
        error = 'error'
        # print error

def top_players(players):
    top_players_list = []
    for name in players:
        rank, player_name, position, team, bye, player_info = search_player(name)
        info = 'Rank|{}-{} -{} -{} Bye|{}'.format(rank, player_name, position, team, bye)
        top_players_list.append(info)
    return top_players_list

# print player_info_list
# print player_chosen

# add, remove, new, close = raw_input('add, remove, new, close').split()
print available_player_list

my_team = []

input_name = True

while input_name:
    print 'Top 5 available {}'.format(top_players(available_player_list[:5]))
    input_name = raw_input('Player name : ')
    rank, player_name, position, team, bye, player_info = search_player(input_name)
    print 'Rank|{} Player|{} Team|{} Position|{} Bye|{}'.format(rank, player_name, position, team, bye)
    if player_name in available_player_list:
        print '{} available.'.format(player_name)
        options = raw_input('(a)Add player to team. (d)delete from available.')
        if options == 'a':
            # new_player = search_player(input_name)
            add_team_player(player_name)
            print '{} added to team.'.format(player_name)
        if options == 'd':
            available_player_list.remove(player_name)
        continue
    if player_name not in available_player_list:
        print '{} is not available.'.format(player_name)
        options = raw_input('(r)remove from team, (a)add to available.')
        if options == 'r':
            remove_team_player(player_name)
            print '{} removed from team.'.format(player_name)
        if options == 'a':
            available_player_list.append(player_name)
else:
    print 'My Team {}'.format(my_team)

print 'Still avaliable {}'.format(available_player_list)

# path = os.path.expandvars('{0}\{1}.csv'.format(new_folder,schedule_name))
# csvfile = open(path, 'w')
# spamwriter = csv.writer(csvfile)
# spamwriter.writerow(['Name', 'Type', 'Header'])

















