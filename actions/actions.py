# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

data_sheet = client.open_by_url(
    "https://docs.google.com/spreadsheets/d/1mCio8I0xCLp2vKQU9AkPyq80t43MGSDqjR3z-GCF9r0/edit#gid=1338220169").worksheet(
    "project latest")  # Comment out if bugs and uncomment line below
    # "project backup")  # Open the spreadhseet

transfer_picks_forward_sheet = client.open_by_url(
    # latest sheet below - comment out and replace with backup if data is broken/updating
    "https://docs.google.com/spreadsheets/d/1_rkHKgIPt3i_2uKr8kh5u4WZaYOLccNiiTx1xAaAo_Y/edit#gid=380389810").worksheet("Transfer Pick - FWD")  # Open the spreadhseet
    # backup sheet below - comment out and replace with latest if data is working
    # "https://docs.google.com/spreadsheets/d/1mCio8I0xCLp2vKQU9AkPyq80t43MGSDqjR3z-GCF9r0/edit#gid=1338220169").worksheet("Transfer Pick - FWD")  # Open the spreadhseet

transfer_picks_midfielder_sheet = client.open_by_url(
    # latest sheet below - comment out and replace with backup if data is broken/updating
    "https://docs.google.com/spreadsheets/d/1_rkHKgIPt3i_2uKr8kh5u4WZaYOLccNiiTx1xAaAo_Y/edit#gid=380389810").worksheet(
    "Transfer Pick - MID")  # Open the spreadhseet
    # backup sheet below - comment out and replace with latest if data is working
    # "https://docs.google.com/spreadsheets/d/1mCio8I0xCLp2vKQU9AkPyq80t43MGSDqjR3z-GCF9r0/edit#gid=1338220169").worksheet("Transfer Pick - MID")  # Open the spreadhseet

transfer_picks_defender_sheet = client.open_by_url(
    # latest sheet below - comment out and replace with backup if data is broken/updating
    "https://docs.google.com/spreadsheets/d/1_rkHKgIPt3i_2uKr8kh5u4WZaYOLccNiiTx1xAaAo_Y/edit#gid=380389810").worksheet(
    "Transfer Pick - DEF")  # Open the spreadhseet
    # backup sheet below - comment out and replace with latest if data is working
    # "https://docs.google.com/spreadsheets/d/1mCio8I0xCLp2vKQU9AkPyq80t43MGSDqjR3z-GCF9r0/edit#gid=1338220169").worksheet("Transfer Pick - DEF")  # Open the spreadhseet

transfer_picks_goalkeeper_sheet = client.open_by_url(
    # latest sheet below - comment out and replace with backup if data is broken/updating
    "https://docs.google.com/spreadsheets/d/1_rkHKgIPt3i_2uKr8kh5u4WZaYOLccNiiTx1xAaAo_Y/edit#gid=380389810").worksheet(
    "Transfer Pick - GK")  # Open the spreadhseet
    # backup sheet below - comment out and replace with latest if data is working
    # "https://docs.google.com/spreadsheets/d/1mCio8I0xCLp2vKQU9AkPyq80t43MGSDqjR3z-GCF9r0/edit#gid=1338220169").worksheet("Transfer Pick - GK")  # Open the spreadhseet

def overall_most_goals():
    top_num_of_goals = data_sheet.cell(714, 2).value
    top_first_name = data_sheet.cell(714, 3).value
    if top_first_name is None:
        top_first_name = ''
    top_last_name = data_sheet.cell(714, 4).value

    return top_num_of_goals, top_first_name, top_last_name


def overall_most_assists():
    top_num_of_assists = data_sheet.cell(719, 2).value
    top_first_name = data_sheet.cell(719, 3).value
    if top_first_name is None:
        top_first_name = ''
    top_last_name = data_sheet.cell(719, 4).value

    return top_num_of_assists, top_first_name, top_last_name

def overall_most_points_total():
    top_num_of_points_total = data_sheet.cell(724, 2).value
    top_first_name = data_sheet.cell(724, 3).value
    if top_first_name is None:
        top_first_name = ''
    top_last_name = data_sheet.cell(724, 4).value

    return top_num_of_points_total, top_first_name, top_last_name

def overall_most_points_gw():
    top_num_of_points_gw = data_sheet.cell(729, 2).value
    top_first_name = data_sheet.cell(729, 3).value
    if top_first_name is None:
        top_first_name = ''
    top_last_name = data_sheet.cell(729, 4).value

    return top_num_of_points_gw, top_first_name, top_last_name

def overall_most_in_form():
    top_in_form = data_sheet.cell(734, 2).value
    top_first_name = data_sheet.cell(734, 3).value
    if top_first_name is None:
        top_first_name = ''
    top_last_name = data_sheet.cell(734, 4).value

    return top_in_form, top_first_name, top_last_name

def overall_most_clean_sheets():
    top_num_of_clean_sheets = data_sheet.cell(739, 2).value
    top_first_name = data_sheet.cell(739, 3).value
    if top_first_name is None:
        top_first_name = ''
    top_last_name = data_sheet.cell(739, 4).value

    return top_num_of_clean_sheets, top_first_name, top_last_name

def overall_most_transferred_out_gw():
    top_transferred_out_gw = data_sheet.cell(744, 2).value
    top_first_name = data_sheet.cell(744, 3).value
    if top_first_name is None:
        top_first_name = ''
    top_last_name = data_sheet.cell(744, 4).value

    return top_transferred_out_gw, top_first_name, top_last_name

def overall_most_transferred_in_gw():
    top_transferred_in_gw = data_sheet.cell(749, 2).value
    top_first_name = data_sheet.cell(749, 3).value
    if top_first_name is None:
        top_first_name = ''
    top_last_name = data_sheet.cell(749, 4).value

    return top_transferred_in_gw, top_first_name, top_last_name

def overall_most_points_per_game():
    top_points_per_game = data_sheet.cell(754, 2).value
    top_first_name = data_sheet.cell(754, 3).value
    if top_first_name is None:
        top_first_name = ''
    top_last_name = data_sheet.cell(754, 4).value

    return top_points_per_game, top_first_name, top_last_name

def get_player_query_row(player_query):
    player_query = player_query.title()

    # handle names beginning with 'Mc' properly e.g. McBurnie or McGoldrick
    if player_query[0:2] == "Mc" or player_query[0:2] == "mc":
        mc = "Mc"
        temp = player_query[2:].title()
        player_query = mc + temp

    player_cell = data_sheet.find(player_query)
    query_row = player_cell.row
    query_col = player_cell.col

    player_row = data_sheet.row_values(query_row)
    first_name = player_row[41]
    last_name = player_row[42]
    team_name = player_row[6]
    goals = player_row[8]
    assists = player_row[9]
    cost = player_row[3]
    selection = player_row[7]
    gameweek_points = player_row[11]
    total_points = player_row[12]
    next_fixture = player_row[37]

    if first_name == last_name:         # players with nicknames fix e.g. Allan, Fred, Jorginho, etc.
        first_name = ""
    elif first_name == ("" or " "):     # duplicate surnames fix e.g. Reece James, Daniel James, etc.
        first_name = last_name[0]

    goal_formatting_text = "goals"
    if goals == "":
        goals = 0
    elif goals == '1':
        goal_formatting_text = "goal"

    assist_formatting_text = "assists"
    if assists == "":
        assists = 0
    elif assists == '1':
        assist_formatting_text = "assist"

    point_formatting_text = "points"
    if gameweek_points == "":
        gameweek_points = 0
    elif gameweek_points == '1':
        point_formatting_text = "point"

    return player_row, first_name, last_name, team_name, goals, assists, cost, selection, gameweek_points, \
        total_points, next_fixture, goal_formatting_text, assist_formatting_text, point_formatting_text

def transfer_pick_fun(position):
    position_text_format = ""
    search_range = 0
    sheet = ""
    if position == "FWD":
        position_text_format = "forward"
        search_range = 10
        sheet = transfer_picks_forward_sheet
    elif position == "MID":
        position_text_format = "midfielder"
        search_range = 10
        sheet = transfer_picks_midfielder_sheet
    elif position == "DEF":
        position_text_format = "defender"
        search_range = 20
        sheet = transfer_picks_defender_sheet
    elif position == "GK":
        position_text_format = "goalkeeper"
        search_range = 20
        sheet = transfer_picks_goalkeeper_sheet

    row_numbers_of_trns_picks = []

    for i in range(2, search_range):
        if sheet.cell(i, 6).value == position and len(row_numbers_of_trns_picks) < 1:
            len(row_numbers_of_trns_picks)
            row_numbers_of_trns_picks.append(i)

    row_num_of_top_pick = row_numbers_of_trns_picks[0]

    transfer_pick_top_first_name = sheet.cell(row_num_of_top_pick, 1).value
    transfer_pick_top_last_name = sheet.cell(row_num_of_top_pick, 2).value
    transfer_pick_top_fd_index = sheet.cell(row_num_of_top_pick, 3).value
    transfer_pick_top_cost = sheet.cell(row_num_of_top_pick, 4).value
    transfer_pick_top_selection = sheet.cell(row_num_of_top_pick, 14).value
    transfer_pick_team_name = sheet.cell(row_num_of_top_pick, 7).value
    transfer_pick_goals = sheet.cell(row_num_of_top_pick, 15).value
    transfer_pick_assists = sheet.cell(row_num_of_top_pick, 16).value
    transfer_pick_next_fixture = sheet.cell(row_num_of_top_pick, 8).value
    transfer_pick_clean_sheets = sheet.cell(row_num_of_top_pick, 17).value

    return position_text_format, transfer_pick_top_first_name, transfer_pick_top_last_name, \
        transfer_pick_top_fd_index, transfer_pick_top_cost, transfer_pick_top_selection, transfer_pick_team_name, \
        transfer_pick_goals, transfer_pick_assists, transfer_pick_next_fixture, transfer_pick_clean_sheets


class ActionHelloWorld(Action):

    def name(self) -> Text:
         return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("I am from action.py file")
        dispatcher.utter_message(text="Hello World! (first action python code!)")

        return []

class ActionStrikerMostPoints(Action):

    def name(self) -> Text:
         return "action_striker_most_points"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("I am from action.py file")
        dispatcher.utter_message(text="The striker with the most points is Harry Kane.")

        return []

class ActionPlayerTotalPointsQuery(Action):

    def name(self) -> Text:
         return "action_player_total_points_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."

        for e in entities:
            if e['entity'] == 'player':
                name = e['value']

            try:
                player_query_row, player_query_first_name, player_query_last_name, player_query_team_name, player_query_goals, \
                    player_query_assists, player_query_cost, player_query_selection, player_query_gameweek_points, \
                    player_query_total_points, player_query_next_fixture, goal_text, assist_text, point_text = get_player_query_row(name)

                message = (f'{player_query_first_name} {player_query_last_name} has {player_query_total_points} points in total.')
            
            except gspread.exceptions.CellNotFound:
                message = (f"I couldn't find the player you're looking for. Please try again, and make sure you pronounced or spelled their name correctly.")        

                    
           
        dispatcher.utter_message(text=message)

        return []

class ActionPlayerGoalsQuery(Action):

    def name(self) -> Text:
         return "action_player_goals_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."

        for e in entities:
            if e['entity'] == 'player':
                name = e['value']

            try:
                player_query_row, player_query_first_name, player_query_last_name, player_query_team_name, player_query_goals, \
                    player_query_assists, player_query_cost, player_query_selection, player_query_gameweek_points, \
                    player_query_total_points, player_query_next_fixture, goal_text, assist_text, point_text = get_player_query_row(name)

                message = (f'{player_query_first_name} {player_query_last_name} has scored {player_query_goals} {goal_text}.')

            except gspread.exceptions.CellNotFound:
                    try:
                        if len(test_query.split()) > 1:
                            test_query = test_query.split(' ')[1]
                        
                        player_query_row, player_query_first_name, player_query_last_name, player_query_team_name, player_query_goals, \
                            player_query_assists, player_query_cost, player_query_selection, player_query_gameweek_points, \
                            player_query_total_points, player_query_next_fixture, goal_text, assist_text, point_text = get_player_query_row(name)

                        message = (f'{player_query_first_name} {player_query_last_name} has scored {player_query_goals} {goal_text}.')
                        pass
                    except gspread.exceptions.CellNotFound:
                        message = (f"I couldn't find the player you're looking for. Please try again, and make sure you pronounced or spelled their name correctly.")        

            except gspread.exceptions.APIError:
                message = (f"Sorry, I can't take any more requests for now. Please try again in a few minutes.")        
    
           
        dispatcher.utter_message(text=message)

        return []

class ActionPlayerAssistsQuery(Action):

    def name(self) -> Text:
         return "action_player_assists_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."


        for e in entities:
            if e['entity'] == 'player':
                name = e['value']

            try:
                player_query_row, player_query_first_name, player_query_last_name, player_query_team_name, player_query_goals, \
                    player_query_assists, player_query_cost, player_query_selection, player_query_gameweek_points, \
                    player_query_total_points, player_query_next_fixture, goal_text, assist_text, point_text = get_player_query_row(name)

                message = (f'{player_query_first_name} {player_query_last_name} has {player_query_assists} {assist_text}.')

            except gspread.exceptions.CellNotFound:
                    try:
                        if len(test_query.split()) > 1:
                            test_query = test_query.split(' ')[1]
                        
                        player_query_row, player_query_first_name, player_query_last_name, player_query_team_name, player_query_goals, \
                            player_query_assists, player_query_cost, player_query_selection, player_query_gameweek_points, \
                            player_query_total_points, player_query_next_fixture, goal_text, assist_text, point_text = get_player_query_row(name)

                        message = (f'{player_query_first_name} {player_query_last_name} has {player_query_assists} {assist_text}.')
                        pass
                    except gspread.exceptions.CellNotFound:
                        message = (f"I couldn't find the player you're looking for. Please try again, and make sure you pronounced or spelled their name correctly.")        

            except gspread.exceptions.APIError:
                message = (f"Sorry, I can't take any more requests for now. Please try again in a few minutes.")        

        dispatcher.utter_message(text=message)

        return []

class ActionPlayerCostQuery(Action):

    def name(self) -> Text:
         return "action_player_cost_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."


        for e in entities:
            if e['entity'] == 'player':
                name = e['value']

            try:
                player_query_row, player_query_first_name, player_query_last_name, player_query_team_name, player_query_goals, \
                    player_query_assists, player_query_cost, player_query_selection, player_query_gameweek_points, \
                    player_query_total_points, player_query_next_fixture, goal_text, assist_text, point_text = get_player_query_row(name)

                message = (f"{player_query_first_name} {player_query_last_name}'s price is £{player_query_cost} today.")       

            except gspread.exceptions.CellNotFound:
                    try:
                        if len(test_query.split()) > 1:
                            test_query = test_query.split(' ')[1]
                        
                        player_query_row, player_query_first_name, player_query_last_name, player_query_team_name, player_query_goals, \
                        player_query_assists, player_query_cost, player_query_selection, player_query_gameweek_points, \
                        player_query_total_points, player_query_next_fixture, goal_text, assist_text, point_text = get_player_query_row(name)

                        message = (f"{player_query_first_name} {player_query_last_name}'s price is £{player_query_cost} today.")       
                        pass
                    except gspread.exceptions.CellNotFound:
                        message = (f"I couldn't find the player you're looking for. Please try again, and make sure you pronounced or spelled their name correctly.")        

            except gspread.exceptions.APIError:
                message = (f"Sorry, I can't take any more requests for now. Please try again in a few minutes.") 
           
        dispatcher.utter_message(text=message)

        return []

class ActionPlayerSelectionQuery(Action):

    def name(self) -> Text:
         return "action_player_selection_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."


        for e in entities:
            if e['entity'] == 'player':
                name = e['value']

            try:
                player_query_row, player_query_first_name, player_query_last_name, player_query_team_name, player_query_goals, \
                    player_query_assists, player_query_cost, player_query_selection, player_query_gameweek_points, \
                    player_query_total_points, player_query_next_fixture, goal_text, assist_text, point_text = get_player_query_row(name)

                message = (f'{player_query_first_name} {player_query_last_name} has been selected by {player_query_selection}% of FPL players.')

            except gspread.exceptions.CellNotFound:
                    try:
                        if len(test_query.split()) > 1:
                            test_query = test_query.split(' ')[1]
                        
                        player_query_row, player_query_first_name, player_query_last_name, player_query_team_name, player_query_goals, \
                            player_query_assists, player_query_cost, player_query_selection, player_query_gameweek_points, \
                            player_query_total_points, player_query_next_fixture, goal_text, assist_text, point_text = get_player_query_row(name)

                        message = (f'{player_query_first_name} {player_query_last_name} has been selected by {player_query_selection}% of FPL players.')       
                        pass
                    except gspread.exceptions.CellNotFound:
                        message = (f"I couldn't find the player you're looking for. Please try again, and make sure you pronounced or spelled their name correctly.")        

            except gspread.exceptions.APIError:
                message = (f"Sorry, I can't take any more requests for now. Please try again in a few minutes.")         
           
        dispatcher.utter_message(text=message)

        return []

class ActionPlayerGameweekPointsQuery(Action):

    def name(self) -> Text:
         return "action_player_gameweek_points_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."


        for e in entities:
            if e['entity'] == 'player':
                name = e['value']

            try:
                player_query_row, player_query_first_name, player_query_last_name, player_query_team_name, player_query_goals, \
                    player_query_assists, player_query_cost, player_query_selection, player_query_gameweek_points, \
                    player_query_total_points, player_query_next_fixture, goal_text, assist_text, point_text = get_player_query_row(name)

                message = (f'{player_query_first_name} {player_query_last_name} got {player_query_gameweek_points} {point_text} this week.')

            except gspread.exceptions.CellNotFound:
                    try:
                        if len(test_query.split()) > 1:
                            test_query = test_query.split(' ')[1]
                        
                        player_query_row, player_query_first_name, player_query_last_name, player_query_team_name, player_query_goals, \
                            player_query_assists, player_query_cost, player_query_selection, player_query_gameweek_points, \
                            player_query_total_points, player_query_next_fixture, goal_text, assist_text, point_text = get_player_query_row(name)

                        message = (f'{player_query_first_name} {player_query_last_name} got {player_query_gameweek_points} {point_text} this week.')       
                        pass
                    except gspread.exceptions.CellNotFound:
                        message = (f"I couldn't find the player you're looking for. Please try again, and make sure you pronounced or spelled their name correctly.")        

            except gspread.exceptions.APIError:
                message = (f"Sorry, I can't take any more requests for now. Please try again in a few minutes.")         
    
           
        dispatcher.utter_message(text=message)

        return []

class ActionPlayerNextFixtureQuery(Action):

    def name(self) -> Text:
         return "action_player_next_fixture_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."

        
        for e in entities:
            if e['entity'] == 'player':
                name = e['value']

            try:
                player_query_row, player_query_first_name, player_query_last_name, player_query_team_name, player_query_goals, \
                    player_query_assists, player_query_cost, player_query_selection, player_query_gameweek_points, \
                    player_query_total_points, player_query_next_fixture, goal_text, assist_text, point_text = get_player_query_row(name)

                message = (f'{player_query_first_name} {player_query_last_name} is playing {player_query_next_fixture} next.')
            
            except gspread.exceptions.CellNotFound:
                    try:
                        if len(test_query.split()) > 1:
                            test_query = test_query.split(' ')[1]
                        
                        player_query_row, player_query_first_name, player_query_last_name, player_query_team_name, player_query_goals, \
                            player_query_assists, player_query_cost, player_query_selection, player_query_gameweek_points, \
                            player_query_total_points, player_query_next_fixture, goal_text, assist_text, point_text = get_player_query_row(name)

                        message = (f'{player_query_first_name} {player_query_last_name} got {player_query_gameweek_points} {point_text} this week.')       
                        pass
                    except gspread.exceptions.CellNotFound:
                        message = (f'{player_query_first_name} {player_query_last_name} is playing {player_query_next_fixture} next.')        

            except gspread.exceptions.APIError:
                message = (f"Sorry, I can't take any more requests for now. Please try again in a few minutes.")        
           
        dispatcher.utter_message(text=message)

        return []

class ActionPlayerTeamNameQuery(Action):

    def name(self) -> Text:
         return "action_player_team_name_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."

        
        for e in entities:
            if e['entity'] == 'player':
                name = e['value']

            try:
                player_query_row, player_query_first_name, player_query_last_name, player_query_team_name, player_query_goals, \
                    player_query_assists, player_query_cost, player_query_selection, player_query_gameweek_points, \
                    player_query_total_points, player_query_next_fixture, goal_text, assist_text, point_text = get_player_query_row(name)

                message = (f'{player_query_first_name} {player_query_last_name} plays for {player_query_team_name}.')

            except gspread.exceptions.CellNotFound:
                    try:
                        if len(test_query.split()) > 1:
                            test_query = test_query.split(' ')[1]
                        
                        player_query_row, player_query_first_name, player_query_last_name, player_query_team_name, player_query_goals, \
                            player_query_assists, player_query_cost, player_query_selection, player_query_gameweek_points, \
                            player_query_total_points, player_query_next_fixture, goal_text, assist_text, point_text = get_player_query_row(name)

                        message = (f'{player_query_first_name} {player_query_last_name} got {player_query_gameweek_points} {point_text} this week.')       
                        pass
                    except gspread.exceptions.CellNotFound:
                        message = (f'{player_query_first_name} {player_query_last_name} plays for {player_query_team_name}.')        

            except gspread.exceptions.APIError:
                message = (f"Sorry, I can't take any more requests for now. Please try again in a few minutes.")     
           
        dispatcher.utter_message(text=message)

        return []


class ActionTransferPickForward(Action):

    def name(self) -> Text:
         return "action_transfer_pick_forward"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."

        try:
            fwd_position = "FWD"
            fwd_text_format, fwd_pick_top_first_name, fwd_pick_top_last_name, fwd_pick_top_fd_index, fwd_pick_top_cost, \
                fwd_pick_top_selection, fwd_pick_team_name,  fwd_pick_goals, fwd_pick_assists, fwd_pick_next_fixture, \
                fwd_pick_clean_sheets = transfer_pick_fun(fwd_position)

            message = ( f"The {fwd_text_format} you should sign this gameweek is {fwd_pick_top_first_name} "
                        f"{fwd_pick_top_last_name} from {fwd_pick_team_name}. His FD index is {fwd_pick_top_fd_index}, "
                        f"which is the highest, meaning he has the best form and the easiest upcoming 5 fixtures. His cost today is "
                        f"{fwd_pick_top_cost}, and he's been selected by {fwd_pick_top_selection}% of FPL players. He's scored "
                        f"{fwd_pick_goals} goals, has {fwd_pick_assists} assists, and his next match is {fwd_pick_next_fixture}.")

        except gspread.exceptions.APIError:
            message = "Sorry, I can't take any more requests for now. Please try again in a few minutes."
           
        dispatcher.utter_message(text=message)

        return []

class ActionTransferPickMidfielder(Action):

    def name(self) -> Text:
         return "action_transfer_pick_midfielder"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."

        try:
            mid_position = "MID"
            mid_text_format, mid_pick_top_first_name, mid_pick_top_last_name, mid_pick_top_fd_index, mid_pick_top_cost, \
                mid_pick_top_selection, mid_pick_team_name, mid_pick_goals, mid_pick_assists, mid_pick_next_fixture, \
                mid_pick_clean_sheets = transfer_pick_fun(mid_position)

            message = ( f"The {mid_text_format} you should sign this gameweek is {mid_pick_top_first_name} {mid_pick_top_last_name} from "
                        f"{mid_pick_team_name}. His FD index is {mid_pick_top_fd_index}, which is the highest, meaning he has the best "
                        f"form and the easiest upcoming 5 fixtures. His cost today is {mid_pick_top_cost}, and he's been selected by "
                        f"{mid_pick_top_selection}% of FPL players. He's scored {mid_pick_goals} goals, has {mid_pick_assists} assists, "
                        f"and his next match is {mid_pick_next_fixture}.")

        except gspread.exceptions.APIError:
            message = "Sorry, I can't take any more requests for now. Please try again in a few minutes."
           
        dispatcher.utter_message(text=message)

        return []


class ActionTransferPickDefender(Action):

    def name(self) -> Text:
         return "action_transfer_pick_defender"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."

        try:
            def_position = "DEF"
            def_text_format, def_pick_top_first_name, def_pick_top_last_name, def_pick_top_fd_index, def_pick_top_cost, \
                def_pick_top_selection, def_pick_team_name, def_pick_goals, def_pick_assists, def_pick_next_fixture, \
                def_pick_clean_sheets = transfer_pick_fun(def_position)

            message = ( f"The {def_text_format} you should sign this gameweek is {def_pick_top_first_name} {def_pick_top_last_name} from "
                        f"{def_pick_team_name}. His FD index is {def_pick_top_fd_index}, which is the highest, meaning he has the best "
                        f"form and the easiest upcoming 5 fixtures. His cost today is {def_pick_top_cost}, and he's been selected by "
                        f"{def_pick_top_selection}% of FPL players. He has {def_pick_clean_sheets} clean sheets and his next match is "
                        f"{def_pick_next_fixture}.")

        except gspread.exceptions.APIError:
            message = "Sorry, I can't take any more requests for now. Please try again in a few minutes."
           
        dispatcher.utter_message(text=message)

        return []

class ActionTransferPickGoalkeeper(Action):

    def name(self) -> Text:
         return "action_transfer_pick_goalkeeper"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."

        try:
            gk_position = "GK"
            gk_text_format, gk_pick_top_first_name, gk_pick_top_last_name, gk_pick_top_fd_index, gk_pick_top_cost, \
                gk_pick_top_selection, gk_pick_team_name, gk_pick_goals, gk_pick_assists, gk_pick_next_fixture, \
                gk_pick_clean_sheets = transfer_pick_fun(gk_position)

            message = ( f"The {gk_text_format} you should sign this gameweek is {gk_pick_top_first_name} {gk_pick_top_last_name} from "
                        f"{gk_pick_team_name}. His FD index is {gk_pick_top_fd_index}, which is the highest, meaning he has the best "
                        f"form and the easiest upcoming 5 fixtures. His cost today is {gk_pick_top_cost}, and he's been selected by "
                        f"{gk_pick_top_selection}% of FPL players. He has {gk_pick_clean_sheets} clean sheets and his next match is "
                        f"{gk_pick_next_fixture}.")

        except gspread.exceptions.APIError:
            message = "Sorry, I can't take any more requests for now. Please try again in a few minutes."
           
        dispatcher.utter_message(text=message)

        return []

class ActionOverallMostGoals(Action):

    def name(self) -> Text:
         return "action_overall_most_goals"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."

        try:
            goal_num, name, surname = overall_most_goals()
            message = f"{name} {surname} is the top scorer with {goal_num} goals."

        except gspread.exceptions.APIError:
            message = "Sorry, I can't take any more requests for now. Please try again in a few minutes."
           
        dispatcher.utter_message(text=message)

        return []

class ActionOverallMostAssists(Action):

    def name(self) -> Text:
         return "action_overall_most_assists"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."

        try:
            assist_num, name, surname = overall_most_assists()
            message = f"{name} {surname} has the most assists with {assist_num} assists."

        except gspread.exceptions.APIError:
            message = "Sorry, I can't take any more requests for now. Please try again in a few minutes."
           
        dispatcher.utter_message(text=message)

        return []

class ActionOverallMostPointsTotal(Action):

    def name(self) -> Text:
         return "action_overall_most_points_total"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."

        try:
            points_total, name, surname = overall_most_points_total()
            message = f"{name} {surname} has the most points in total with {points_total} points."

        except gspread.exceptions.APIError:
            message = "Sorry, I can't take any more requests for now. Please try again in a few minutes."
           
        dispatcher.utter_message(text=message)

        return []

class ActionOverallMostPointsWeek(Action):

    def name(self) -> Text:
         return "action_overall_most_points_week"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."

        try:
            points_week, name, surname = overall_most_points_gw()
            message = f"{name} {surname} has the most points this week with {points_week} points."

        except gspread.exceptions.APIError:
            message = "Sorry, I can't take any more requests for now. Please try again in a few minutes."
           
        dispatcher.utter_message(text=message)

        return []

class ActionOverallMostInForm(Action):

    def name(self) -> Text:
         return "action_overall_most_in_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."

        try:
            form, name, surname = overall_most_in_form()
            message = f"{name} {surname} is the most in form player with a form of {form}."

        except gspread.exceptions.APIError:
            message = "Sorry, I can't take any more requests for now. Please try again in a few minutes."
           
        dispatcher.utter_message(text=message)

        return []

class ActionOverallMostCleanSheets(Action):

    def name(self) -> Text:
         return "action_overall_most_clean_sheets"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."

        try:
            clean_sheets, name, surname = overall_most_clean_sheets()
            message = f"{name} {surname} has the most clean sheets with {clean_sheets} cleansheets."

        except gspread.exceptions.APIError:
            message = "Sorry, I can't take any more requests for now. Please try again in a few minutes."
           
        dispatcher.utter_message(text=message)

        return []

class ActionOverallMostTransferredOutGW(Action):

    def name(self) -> Text:
         return "action_overall_most_transferred_out_gw"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."

        try:
            trans_out, name, surname = overall_most_transferred_out_gw()
            message = f"{name} {surname} is the most transferred out player this GW."

        except gspread.exceptions.APIError:
            message = "Sorry, I can't take any more requests for now. Please try again in a few minutes."
           
        dispatcher.utter_message(text=message)

        return []

class ActionOverallMostTransferredInGW(Action):

    def name(self) -> Text:
         return "action_overall_most_transferred_in_gw"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."

        try:
            trans_out, name, surname = overall_most_transferred_in_gw()
            message = f"{name} {surname} is the most transferred in player this GW."

        except gspread.exceptions.APIError:
            message = "Sorry, I can't take any more requests for now. Please try again in a few minutes."
           
        dispatcher.utter_message(text=message)

        return []

"""
class ActionOverallMostPointsPerGame(Action):

    def name(self) -> Text:
         return "action_overall_most_points_per_game"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Sorry, I wasn't able to understand you. If you're trying to ask me about a player, please make sure you pronounced or spelled their name correctly."

        try:
            points_per_game, name, surname = overall_most_points_per_game()
            message = f"{name} {surname} has the most points per game, with {points_per_game} points per game."

        except gspread.exceptions.APIError:
            message = "Sorry, I can't take any more requests for now. Please try again in a few minutes."
           
        dispatcher.utter_message(text=message)

        return []
"""