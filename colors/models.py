from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from .fields import PickleField
import random

author = 'Alexis Belianin, Philipp Chapkovski, Gregory Chernov, HSE-Moscow'

doc = """
Risk elicitation via picking the color difficulty
"""


class Constants(BaseConstants):
    name_in_url = 'colors'
    players_per_group = None
    num_rounds = 10
    min_step = 1.5
    num_rows = 4
    num_columns = 4
    num_colors = num_rows * num_columns
    num_difficulty_choices = 10
    step_of_steps = 1
    DIFFICULTY_CHOICES = []
    for i in range(num_difficulty_choices):
        DIFFICULTY_CHOICES.append(min_step + i * step_of_steps)
    payoffs = list(range(num_difficulty_choices + 1, 1, -1))  # quick lazy fix for payoffs for now
    payoff_dict = dict(zip(DIFFICULTY_CHOICES, payoffs))  # that's an ugly lazy way of doing things. Should be replaced
    hue = 10  # these three parameters define starting color
    saturation = 100
    lightness = 64
    start_color = {'hue': hue, 'saturation': saturation, 'lightness': lightness}
    payoff_if_fail = c(0)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    step = models.FloatField(doc='That defines step level for the gradient', choices=Constants.DIFFICULTY_CHOICES,
                             widget=widgets.RadioSelect)
    answer = models.IntegerField(doc='choice of the user which color is todo color')
    answered_color = models.FloatField(doc='what color correspond to a participant answer')
    todo_num = models.IntegerField(doc='a question (color id that should be guessed)')
    todo_color = models.FloatField(doc='a question (color value that should be guessed)')
    colors = PickleField(null=True)

    def get_max_colors(self):
        return [Constants.hue + Constants.num_colors * i for i in Constants.DIFFICULTY_CHOICES]

    def set_answered_color(self):
        # we correct for minus 1 because numbers are shown starting from 1
        self.answered_color = self.colors[self.answer - 1]

    def set_payoff(self):
        if self.answer == self.todo_num:
            self.payoff = Constants.payoff_dict[self.step]
        else:
            self.payoff = Constants.payoff_if_fail

    def generate_colors(self):
        ub = Constants.hue + Constants.num_colors * self.step
        self.colors = [random.uniform(Constants.hue, ub) for _ in range(Constants.num_colors)]
        self.todo_num = random.choice(range(1, Constants.num_colors + 1))
        self.todo_color = self.colors[self.todo_num - 1]
