# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_random_response

my_chat = ChatBot(
    'ChartRobot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    response_selection_method=get_random_response,
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
    ],
    input_adapter='chatterbot.input.VariableInputTypeAdapter',
    output_adapter='chatterbot.output.OutputAdapter',
    database='./database.sqlite3',
    read_only=True
)


def get_answer(content):
    response = my_chat.get_response(content)
    if isinstance(response, str):
        return response
    return response.text
