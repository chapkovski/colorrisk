from otree.api import Currency as c, currency_range
from .pages import *
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        yield Choice, {'step': random.choice(Constants.DIFFICULTY_CHOICES)}
        yield Task, {'answer': random.randint(1, Constants.num_colors)}
        yield Results
