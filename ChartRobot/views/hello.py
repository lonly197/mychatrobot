# -*- coding: utf-8 -*-

from datetime import datetime
from sanic import Sanic, Blueprint
from sanic.views import HTTPMethodView
from sanic.response import text
from ChartRobot.helper import get_answer

blueprint = Blueprint('index', url_prefix='/')


class Index(HTTPMethodView):
    async def get(self, request):
        return text('hello world!')


class ChatBot(HTTPMethodView):
    async def get(self, request):
        ask = request.args.get('ask')
        if ask:
            answer = get_answer(ask)
            return text(answer)
        else:
            return text('你说了什么？')


blueprint.add_route(Index.as_view(), '/')
blueprint.add_route(ChatBot.as_view(), '/chat')
