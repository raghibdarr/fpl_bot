# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


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
            
            if name == "vardy":
                message = "Jamie Vardy has 66 points."
            if name == "chilwell":
                message = "Ben Chilwell has 56 points."
            if name == "kane":
                message = "Harry Kane has 86 points."
            if name == "de bruyne":
                message = "Kevin De Bruyne has 39 points."

        dispatcher.utter_message(text=message)

        return []


