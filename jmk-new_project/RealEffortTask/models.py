
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'RealEffortTask'
    players_per_group = None
    num_rounds = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    Matrix1 = models.IntegerField(label='How many zeroes are in the table?')
    Matrix2 = models.IntegerField(label='How many zeroes are in the table?')
    Matrix3 = models.IntegerField(label='How many zeroes are in the table?')
    Matrix4 = models.IntegerField(label='How many zeroes are in the table?')
    Matrix5 = models.IntegerField(label='How many zeroes are in the table?')