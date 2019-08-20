from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Choice(Page):
    form_model = 'player'
    form_fields = ['step']

    def vars_for_template(self) -> dict:
        colors = [{'hue': i, 'saturation': Constants.saturation, 'lightness': Constants.lightness} for i in
                  self.player.get_max_colors()]
        payoffs = Constants.payoffs
        choices = self.get_form()["step"]
        return {'colorset': zip(colors, payoffs, choices)}

    def before_next_page(self):
        self.player.generate_colors()


class Task(Page):
    form_model = 'player'
    form_fields = ['answer']

    def vars_for_template(self) -> dict:
        step = 1
        return {'colors': [step * i for i in range(1, 17)]}

    def before_next_page(self):
        self.player.set_answered_color()
        self.player.set_payoff()


class Results(Page):
    pass


page_sequence = [
    Choice,
    Task,
    Results
]
