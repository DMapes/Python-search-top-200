'''top 200 csv reader for drafting'''
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import csv
import datetime
from difflib import get_close_matches
from csv_top_200_info_v2 import *
# from HTML_parser_v6 import *

today = datetime.datetime.today()
today_formatted = today.strftime('%Y.%m.%d')
# today_formatted = today.strftime('%Y.%m.%d %I.%M%p')

Tk().withdraw()
file = askopenfilename()

file_name = os.path.basename(file)
file_path = os.path.dirname(file)
user_path = os.path.expandvars('%userprofile%\Desktop')

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

print ('Top 200 Players: {}'.format(available_player_list))

input_name = True

while input_name:
    input_name = input('Search: ')
    if input_name == 'help':
        print (' (5)Top 5 Available.\n (draft)Show drafted.\n (t)Show team.\n (qb)Top 5 QB.\n (rb)Top 5 RB.\n (wr)Top 5 WR.\n (te)Top 5 TE.\n (d)Top 5 DEF.\n (k)Top 5 K.\n (i)Import Team\n (all)All Available Players.\n (c)Create backup\n (close)Close')
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
            drafted_players.append(d)
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
        input_name = True
    elif input_name == '':
        print (' (5)Top 5 Available.\n (draft)Show drafted.\n (t)Show team.\n (qb)Top 5 QB.\n (rb)Top 5 RB.\n (wr)Top 5 WR.\n (te)Top 5 TE.\n (d)Top 5 DEF.\n (k)Top 5 K.\n (i)Import Team\n (all)All Available Players.\n (c)Create backup\n (close)Close')
        # print ('Blank Search Closing....')
        # input_name = input('To continue choose an option.')
        input_name = True
        # break

    elif input_name == 'close':
        print ('closing now...')
        input_name = False
        break

    # multi_search(input_name)
    # name_1, name_2, name_3 = multi_search(input_name)
    # options = input('choose 1,2,3__')
    # if options == "1":
    #     input_name = name_1
    # elif options == "2":
    #     input_name = name_2
    # elif options == "3":
    #     input_name = name_3

    try:
        multi_search(input_name)
        # name_1, name_2, name_3 = multi_search(input_name)
        # options = input('choose 1,2,3__')
        # if options == "1":
        #     input_name = name_1
        # elif options == "2":
        #     input_name = name_2
        # elif options == "3":
        #     input_name = name_3

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

# input_backup = input('Create Backup Files? (y/n)')
# if input_backup == 'y':
new_backup_folder = backup_folder()
if len(my_team) > 0:
    team_csv()
if len(drafted_players) > 0:
    drafted_csv()
    # print(f'Files created at {new_backup_folder}')
