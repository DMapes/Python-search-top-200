'''top 200 csv reader for drafting'''
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import csv
import datetime

today = datetime.datetime.today()
today_formatted = today.strftime('%Y.%m.%d')
# today_formatted = today.strftime('%Y.%m.%d %I.%M%p')

Tk().withdraw()
file = askopenfilename()

file_name = os.path.basename(file)
file_path = os.path.dirname(file)

available_player_list = []
drafted_players = []
player_info_list = []
my_team = []

with open(file, 'r') as transactions:
    csv_reader = csv.DictReader(transactions)
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
        drafted_players.append(player)
    except:
        error = 'error'
        # print error

def player_details(list):
    player_details_list = []
    for name in list:
        rank, player_name, position, team, bye, player_info = search_player(name)
        info = '{} - {}-{}-{} Bye|{}'.format(rank, player_name, position, team, bye)
        player_details_list.append(info)
    return player_details_list

def position_details(pos, players):
    position_details_list = []
    for name in players:
        rank, player_name, position, team, bye, player_info = search_player(name)
        if position == pos:
            info = '{} - {}-{}-{} Bye|{}'.format(rank, player_name, position, team, bye)
            position_details_list.append(info)
    return position_details_list[:5]

def backup_folder():
    location = os.path.expandvars('{}/{} Draft'.format(file_path, today_formatted))
    try:
        os.mkdir(location)
    except:
        error = 'File already exists'
    return location

def team_csv():
    team_path = os.path.join('{}/Team-{}'.format(new_backup_folder,file_name))
    with open(team_path, 'w') as team_csvfile:
        spamwriter = csv.writer(team_csvfile)
        spamwriter.writerow(['Rk', 'Player', 'Pos', 'Team', 'Bye'])
        for item in my_team:
            rank, player_name, position, team, bye, player_info = search_player(item)
            spamwriter.writerow([rank, player_name, position, team, bye])

def drafted_csv():
    drafted_path = os.path.join('{}/Drafted-{}'.format(new_backup_folder,file_name))
    with open(drafted_path, 'w') as team_csvfile:
        spamwriter = csv.writer(team_csvfile)
        spamwriter.writerow(['Rk', 'Player', 'Pos', 'Team', 'Bye'])
        for item in drafted_players:
            rank, player_name, position, team, bye, player_info = search_player(item)
            spamwriter.writerow([rank, player_name, position, team, bye])

def load_team():
    load_list = []
    team_file = askopenfilename()
    with open(team_file, 'r') as team_names:
        csv_reader = csv.DictReader(team_names)
        for item in csv_reader:
            load_list.append(item['Player'])
        return load_list

def player_available_options(player_name):
    print ('{} available.'.format(player_name))
    options = input('(a)Add player to team. (d)delete from available.')
    if options == 'a':
        add_team_player(player_name)
        print ('{} added to team.'.format(player_name))
    if options == 'd':
        available_player_list.remove(player_name)
        drafted_players.append(player_name)
    if options is False:
        input_name = True
        

def player_unavaiable_options(player_name):
    if player_name in my_team:
        print ('{} is on your Team.'.format(player_name))
        options = input('(r)remove from team')
    else:
        print ('{} is not available.'.format(player_name))
        options = input('(a)add to available')
    if options == 'r':
        remove_team_player(player_name)
        print ('{} removed from team.'.format(player_name))
    if options == 'a':
        available_player_list.append(player_name)
        drafted_players.remove(player_name)
    if options is False:
        input_name = True

print ('Top 200 Players: {}'.format(available_player_list))

input_name = True

while input_name:
    input_name = input('Search: ')
    if input_name == 'o':
        print (' (5)Top 5 Available.\n (draft)Show drafted.\n (t)Show team.\n (qb)Top 5 QB.\n (rb)Top 5 RB.\n (wr)Top 5 WR.\n (te)Top 5 TE.\n (d)Top 5 DEF.\n (k)Top 5 K.\n (i)Import Team\n (all)All Available Players.\n (c)Create backup')
        continue
    elif input_name == '1':
        player_name = ' '.join([str(elem) for elem in available_player_list[:1]]) 
        player_available_options(player_name)
    elif input_name == '5':
        print ('Top 5 available{}'.format(player_details(available_player_list[:5])))
        continue
    elif input_name == 't':
        print ('My Team : {}'.format(player_details(my_team)))
        continue
    elif input_name == 'draft':
        print ('Drafted Players : {}'.format(player_details(drafted_players)))
        continue
    elif input_name == 'qb':
        print ('Top 5 QB{}'.format(position_details('QB', available_player_list)))
        continue
    elif input_name == 'rb':
        print ('Top 5 RB{}'.format(position_details('RB', available_player_list)))
        continue
    elif input_name == 'wr':
        print ('Top 5 WR{}'.format(position_details('WR', available_player_list)))
        continue
    elif input_name == 'te':
        print ('Top 5 TE{}'.format(position_details('TE', available_player_list)))
        continue
    elif input_name == 'd':
        print ('Top 5 DEF{}'.format(position_details('DEF', available_player_list)))
        continue
    elif input_name == 'k':
        print ('Top 5 K{}'.format(position_details('PK', available_player_list)))
        continue
    elif input_name == 'i':
        print ('Choose team file first then drafted list file')
        team_list = load_team()
        for m in team_list:
            my_team.append(m)
            available_player_list.remove(m)
        drafted_list = load_team()
        for d in drafted_list:
            drafted_players.append(m)
            available_player_list.remove(d)
        print ('My Team : {}'.format(player_details(my_team)))
        continue
    elif input_name == 'all':
        print ('All still available {}'.format(player_details(available_player_list)))
        continue
    elif input_name == 'c':
        new_backup_folder = backup_folder()
        if len(my_team) > 0:
            team_csv()
        if len(drafted_players) > 0:
            drafted_csv()
        print(f'Files created at {new_backup_folder}')
    elif input_name == '':
        print ('Blank Search Closing....')
        break
    try:
        rank, player_name, position, team, bye, player_info = search_player(input_name)
        print ('Rank|{} Player|{} Team|{} Position|{} Bye|{}'.format(rank, player_name, position, team, bye))
        if player_name in available_player_list:
            player_available_options(player_name)
        elif player_name not in available_player_list:
            player_unavaiable_options(player_name)
    except:
        # print ('Search Again')
        input_name = True
else:
    stop = 'Stopping...'
    print (stop)

print ('My Team : {}'.format(player_details(my_team)))
# print ('Still available {}'.format(player_details(available_player_list)))

input_backup = input('(c)Create Backup Files?')
if input_backup == 'c':
    new_backup_folder = backup_folder()
    if len(my_team) > 0:
        team_csv()
    if len(drafted_players) > 0:
        drafted_csv()
    print(f'Files created at {new_backup_folder}')
