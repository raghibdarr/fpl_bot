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
    

           # """
            if name == "vardy":
                # message = "Jamie Vardy has 66 points."
                message = (
                    f'{name} has 66 points.' )
            if name == "chilwell":
                # message = "Ben Chilwell has 56 points."
                message = (
                    f'{name} has 56 points.' )
            if name == "Kane":
                # message = "Harry Kane has 86 points."
                
                test = data_sheet.find(name)
                query_row = test.row
                query_col = test.col
                # print(query_row, query_col)

                player_query_row = data_sheet.row_values(query_row)
                player_query_first_name = player_query_row[41]
                player_query_last_name = player_query_row[42]

                player_query_goals = player_query_row[8]
                goal_text = "goals"
                if player_query_goals == "":
                    player_query_goals = 0
                elif player_query_goals == '1':
                    goal_text = "goal"

                player_query_assists = player_query_row[9]
                assist_text = "assists"
                if player_query_assists == "":
                    player_query_assists = 0
                elif player_query_assists == '1':
                    assist_text = "assist"

                message = (
                    f'Player is {player_query_first_name} {player_query_last_name}. '
                    f'He has {player_query_goals} {goal_text} and {player_query_assists} {assist_text}.')
                    
                # message = (f'{name} has 86 points.' )

            if name == "de bruyne":
                # message = "Kevin De Bruyne has 39 points."
                message = (
                    f'{name} has 39 points.' )
           # """
        dispatcher.utter_message(text=message)

        return []


