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
                message = (f"I couldn't find the player you're looking for. Please try again, and make sure you pronounced or spelled their name correctly.")        
    
           
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
                message = (f"I couldn't find the player you're looking for. Please try again, and make sure you pronounced or spelled their name correctly.")        

           
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
                message = (f"I couldn't find the player you're looking for. Please try again, and make sure you pronounced or spelled their name correctly.")        

                    
           
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
                message = (f"I couldn't find the player you're looking for. Please try again, and make sure you pronounced or spelled their name correctly.")        
           
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
                message = (f"I couldn't find the player you're looking for. Please try again, and make sure you pronounced or spelled their name correctly.")        
    
           
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
                message = (f"I couldn't find the player you're looking for. Please try again, and make sure you pronounced or spelled their name correctly.")        
           
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
                message = (f"I couldn't find the player you're looking for. Please try again, and make sure you pronounced or spelled their name correctly.")        
           
        dispatcher.utter_message(text=message)

        return []