
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'GiftCard'
    players_per_group = None
    num_rounds = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    GiftCard1 = models.StringField(
        choices=[['1', 'A'], ['2', 'B'], ['3', 'C'], ['4', 'D'], ['5', 'E']],
        label="Which retailer's gift card would you most prefer?",
        widget=widgets.RadioSelectHorizontal
    )
    GiftCard2 = models.StringField(
        choices=[['1', 'A - Komodo'], ['2', 'B - ASOS'], ['3', 'C - Next'],
                 ['4', 'D - H&M'], ['5', 'E - Boohoo']],
        label="Which retailer's gift card would you most prefer?",
        widget=widgets.RadioSelectHorizontal
    )
    RankingAgreement = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Do you agree with the ethical rankings of the retailers?',
        widget=widgets.RadioSelectHorizontal
    )
    RAWhy = models.LongStringField(blank=True, label='If not, why not?')