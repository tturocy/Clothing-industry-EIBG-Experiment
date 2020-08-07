
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    form_model = 'player'
class Instructions1(Page):
    form_model = 'player'
    form_fields = ['Example', 'ExampleTF']
class Survey1(Page):
    form_model = 'player'
    form_fields = ['Attitude1', 'SDB1', 'SubjectiveNorm1', 'SDB2', 'Intention1', 'SDB3', 'PBC1', 'SDB4', 'Attitude42']
class Survey2(Page):
    form_model = 'player'
    form_fields = ['Intention2', 'SDB5', 'SubjectiveNorm2', 'SDB7', 'PBC2', 'SDB6', 'Attitude2', 'SDB8', 'Attitude32']
class Survey3(Page):
    form_model = 'player'
    form_fields = ['Plan1', 'SDB9', 'SubjectiveNorm3', 'SDB10', 'PBC3', 'SDB11', 'Attitude3', 'SDB12', 'Attitude22']
class Survey4(Page):
    form_model = 'player'
    form_fields = ['Intention4', 'SDB13', 'Attitude4', 'SDB14', 'SubjectiveNorm4', 'SDB15', 'PBC4', 'SDB16', 'SubjectiveNorm5', 'SDB17', 'SDB18', 'Attitude12']
class Survey5(Page):
    form_model = 'player'
    form_fields = ['Plan2', 'Intention11', 'Age', 'Gender', 'Ethnicity', 'Income', 'PastBehaviour']

page_sequence = [Introduction, Instructions1, Survey1, Survey2, Survey3, Survey4, Survey5]