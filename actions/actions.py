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
    # "project latest")  # Comment out if bugs and uncomment line below
    "project backup")  # Open the spreadhseet

def get_player_query_row(player_query):
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

    if first_name == last_name:
        first_name = ""

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

    return player_row, first_name, last_name, team_name, goals, assists, cost, selection, gameweek_points, \
        total_points, next_fixture, goal_formatting_text, assist_formatting_text


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

class ActionPlayerPointsQuery(Action):

    def name(self) -> Text:
         return "action_player_points_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        
        for e in entities:
            if e['entity'] == 'player':
                name = e['value']

            player_query_row, player_query_first_name, player_query_last_name, player_query_team_name, player_query_goals, \
                player_query_assists, player_query_cost, player_query_selection, player_query_gameweek_points, \
                player_query_total_points, player_query_next_fixture, goal_text, assist_text = get_player_query_row(name)

            message = (f'{player_query_first_name} {player_query_last_name} has {player_query_total_points} points in total.')
                    
           
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

        
        for e in entities:
            if e['entity'] == 'player':
                name = e['value']

            player_query_row, player_query_first_name, player_query_last_name, player_query_team_name, player_query_goals, \
                player_query_assists, player_query_cost, player_query_selection, player_query_gameweek_points, \
                player_query_total_points, player_query_next_fixture, goal_text, assist_text = get_player_query_row(name)

            message = (f'{player_query_first_name} {player_query_last_name} has scored {player_query_goals} {goal_text}.')
                    
           
        dispatcher.utter_message(text=message)

        return []


