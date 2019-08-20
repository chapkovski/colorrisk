from otree.api import Currency as c, currency_range
from .pages import *
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        yield Choice, {'choice': random.randint(0, 16)}
        yield Task, {'task': random.randint(0, 16)}
        yield Results
