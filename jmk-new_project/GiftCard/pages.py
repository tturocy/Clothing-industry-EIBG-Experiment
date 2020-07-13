
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Instructions3(Page):
    form_model = 'player'
class GiftCard1(Page):
    form_model = 'player'
    form_fields = ['GiftCard1']
class GiftCard2(Page):
    form_model = 'player'
    form_fields = ['GiftCard2', 'RankingAgreement', 'RAWhy']
class Finish(Page):
    form_model = 'player'
page_sequence = [Instructions3, GiftCard1, GiftCard2, Finish]