
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class RETInstructions(Page):
    form_model = 'player'
class RealEffortTask1(Page):
    form_model = 'player'
    form_fields = ['Matrix1']
    timeout_seconds = 30
    timer_text = 'Time left'
class RealEffortTask2(Page):
    form_model = 'player'
    form_fields = ['Matrix2']
    timeout_seconds = 30
    timer_text = 'Time left'
class RealEffortTask3(Page):
    form_model = 'player'
    form_fields = ['Matrix3']
    timeout_seconds = 30
    timer_text = 'Time left'
class RealEffortTask4(Page):
    form_model = 'player'
    form_fields = ['Matrix4']
    timeout_seconds = 30
    timer_text = 'Time left'
class RealEffortTask5(Page):
    form_model = 'player'
    form_fields = ['Matrix5']
    timeout_seconds = 30
    timer_text = 'Time left'
class RETSummary(Page):
    form_model = 'player'
page_sequence = [
    RETInstructions,
    RealEffortTask1,
    RealEffortTask2,
    RealEffortTask3,
    RealEffortTask4,
    RealEffortTask5,
    RETSummary
]