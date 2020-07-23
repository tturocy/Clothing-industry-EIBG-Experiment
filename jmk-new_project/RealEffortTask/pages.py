
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

    def before_next_page(self):
        if self.player.Matrix1 == 29:
            self.player.payoff += c(0.10)
        else:
            self.player.payoff += c(0.00)


class RealEffortTask2(Page):
    form_model = 'player'
    form_fields = ['Matrix2']
    timeout_seconds = 30
    timer_text = 'Time left'

    def before_next_page(self):
        if self.player.Matrix2 == 35:
            self.player.payoff += c(0.10)
        else:
            self.player.payoff += c(0.00)


class RealEffortTask3(Page):
    form_model = 'player'
    form_fields = ['Matrix3']
    timeout_seconds = 30
    timer_text = 'Time left'

    def before_next_page(self):
        if self.player.Matrix3 == 30:
            self.player.payoff += c(0.10)
        else:
            self.player.payoff += c(0.00)


class RealEffortTask4(Page):
    form_model = 'player'
    form_fields = ['Matrix4']
    timeout_seconds = 30
    timer_text = 'Time left'

    def before_next_page(self):
        if self.player.Matrix4 == 27:
            self.player.payoff += c(0.10)
        else:
            self.player.payoff += c(0.00)


class RealEffortTask5(Page):
    form_model = 'player'
    form_fields = ['Matrix5']
    timeout_seconds = 30
    timer_text = 'Time left'

    def before_next_page(self):
        if self.player.Matrix5 == 28:
            self.player.payoff += c(0.10)
        else:
            self.player.payoff += c(0.00)


class RETSummary(Page):
    form_model = 'player'

    def vars_for_template(self):
        correct = [ self.player.Matrix1 == 29,
                    self.player.Matrix2 == 35,
                    self.player.Matrix3 == 30,
                    self.player.Matrix4 == 27,
                    self.player.Matrix5 == 28 ]
        return {'payoffs': [c(0.10) if v else c(0.0)
                            for v in correct]}

    def before_next_page(self):
        self.participant.vars['part2_earnings'] = self.player.payoff


page_sequence = [
    RETInstructions,
    RealEffortTask1,
    RealEffortTask2,
    RealEffortTask3,
    RealEffortTask4,
    RealEffortTask5,
    RETSummary
]