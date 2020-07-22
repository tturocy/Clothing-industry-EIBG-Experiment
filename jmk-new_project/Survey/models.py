from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''


class Constants(BaseConstants):
    name_in_url = 'Survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

likert_choices = [
    ['1', 'Strongly Disagree'],
    ['2', 'Disagree'],
    ['3', 'Neither Agree or Disagree'],
    ['4', 'Agree'],
    ['5', 'Strongly Agree']
]

class Player(BasePlayer):
    SubjectiveNorm1 = models.StringField(
        choices=likert_choices,
        label="Those who are important to me have purchased from an ethical "
              "clothing retailer in the last month from home",
        widget=widgets.RadioSelectHorizontal
    )
    Intention1 = models.StringField(
        choices=likert_choices,
        label="I intended on purchasing from an ethical clothing retailer "
              "over the last month when at home",
        widget=widgets.RadioSelectHorizontal
    )
    Intention2 = models.StringField(
        choices=likert_choices,
        label="I have tried to purchase from an ethical clothing retailer "
              "over the last month from home",
        widget=widgets.RadioSelectHorizontal
    )
    Plan1 = models.StringField(
        choices=likert_choices,
        label="I made a plan to buy from an ethical clothing retailer "
              "from home in the last month",
        widget=widgets.RadioSelectHorizontal
    )
    Intention4 = models.StringField(
        choices=likert_choices,
        label="I wanted to purchase from an ethical clothing retailer "
              "from home in the last month",
        widget=widgets.RadioSelectHorizontal
    )
    SubjectiveNorm2 = models.StringField(
        choices=likert_choices,
        label="My family has purchased from an ethical clothing retailer "
              "in the last month from home",
        widget=widgets.RadioSelectHorizontal
    )
    SubjectiveNorm3 = models.StringField(
        choices=likert_choices,
        label="Those who are important to me think I should purchase from "
              "an ethical clothing retailer when I've been at home in the "
              "last month",
        widget=widgets.RadioSelectHorizontal
    )
    SubjectiveNorm4 = models.StringField(
        choices=likert_choices,
        label="I have felt pressure from society in the last month to purchase "
              "from an ethical clothing retailer when at home",
        widget=widgets.RadioSelectHorizontal
    )
    SubjectiveNorm5 = models.StringField(
        choices=likert_choices,
        label="My friends think I should purchase from an ethical clothing "
              "retailer",
        widget=widgets.RadioSelectHorizontal
    )
    PBC1 = models.StringField(
        choices=likert_choices,
        label="It would have been easy for me to purchase from an ethical "
              "clothing retailer from home in the last month",
        widget=widgets.RadioSelectHorizontal
    )
    PBC2 = models.StringField(
        choices=likert_choices,
        label="I have had complete control over being able to purchase from "
              "an ethical clothing retailer from home in the last month",
        widget=widgets.RadioSelectHorizontal
    )
    PBC3 = models.StringField(
        choices=likert_choices,
        label="It would have been challenging to purchase from an ethical "
              "clothing retailer from home in the last month",
        widget=widgets.RadioSelectHorizontal
    )
    PBC4 = models.StringField(
        choices=likert_choices,
        label="If I wanted to, I could have purchased from an ethical "
              "clothing retailer from home in the last month",
        widget=widgets.RadioSelectHorizontal
    )
    PBC5 = models.StringField(
        choices=likert_choices,
        label="It has been up to me whether I have bought from an ethical "
              "clothing retailer from home in the last month",
        widget=widgets.RadioSelectHorizontal
    )
    Age = models.IntegerField(blank=True, label='What is your age?')
    Gender = models.StringField(blank=True,
                                choices=[['1', 'Male'], ['2', 'Female'], ['3', 'Other']],
                                label="What is your gender?",
                                widget=widgets.RadioSelectHorizontal)
    Ethnicity = models.StringField(
        blank=True,
        choices=[
            ['1', 'White (English / Welsh / Scottish / Northern Irish / British / Irish / Gypsy or Irish Traveller/Other)'],
            ['2',
             'Mixed / Multiple ethnic groups (White and Black Caribbean / White and Black African / White and Asian / Other)'],
            ['3', 'Asian / Asian British (Indian / Pakistani / Bangladeshi / Chinese / Other)'],
            ['4', 'Black / Black British (African / Caribbean / Other)']],
        label="What is your ethnicity?",
        widget=widgets.RadioSelect
    )
    Income = models.StringField(
        blank=True,
        choices=[['1', '£0 - £21,000'], ['2', '£21,001 - £31,000'], ['3', '£31,001 - £41,000'],
                 ['4', '£41,001 - £51,000'], ['5', '£51,001 - £61,000'],
                 ['6', '£61,001 - £71,000'], ['7', '£71,001+']],
        label="What is your total out-of-term time household income?",
        widget=widgets.RadioSelect
    )
    PastBehaviour = models.StringField(
        choices=[['1', 'Never'], ['2', 'Sometimes'], ['3', 'Half the time'], ['4', 'Mostly'], ['5', 'Always']],
        label='When you buy clothes, how often do you buy them from ethical clothing retailers?',
        widget=widgets.RadioSelectHorizontal
    )
    Intention11 = models.StringField(
        choices=likert_choices,
        label='I intended on purchasing from an ethical clothing retailer over the last month when at home',
        widget=widgets.RadioSelectHorizontal
    )
    Attitude1 = models.StringField(
        choices=likert_choices,
        label='For me, to have purchased slow fashion from an ethical clothing retailer would be good',
        widget=widgets.RadioSelectHorizontal
    )
    Attitude2 = models.StringField(
        choices=likert_choices,
        label="The impact on the environment caused by purchasing from "
              "ethical clothing retailers would be good",
        widget=widgets.RadioSelectHorizontal
    )
    Attitude3 = models.StringField(
        choices=likert_choices,
        label="The impact on employee welfare caused by purchasing "
              "from ethical clothing retailers would be good",
        widget=widgets.RadioSelectHorizontal
    )
    Attitude4 = models.StringField(
        choices=likert_choices,
        label="The impact on animal welfare caused by purchasing "
              "from ethical clothing retailers would be good",
        widget=widgets.RadioSelectHorizontal
    )
    SDB1 = models.BooleanField(
        label='Before voting I thoroughly investigate the qualifications of all the candidates',
        widget=widgets.RadioSelectHorizontal
    )
    SDB2 = models.BooleanField(
        label='I never hesitate to go out of my way to help someone in trouble',
        widget=widgets.RadioSelectHorizontal
    )
    SDB3 = models.BooleanField(
        label='It is sometimes hard for me to go on with my work if I am not encouraged',
        widget=widgets.RadioSelectHorizontal
    )
    SDB4 = models.BooleanField(
        label='On occasion I have had doubts about my ability to succeed in life',
        widget=widgets.RadioSelectHorizontal
    )
    SDB5 = models.BooleanField(
        label="I sometimes feel resentful when I don't get my way",
        widget=widgets.RadioSelectHorizontal
    )
    SDB6 = models.BooleanField(
        label="No matter who I'm talking to, I'm always a good listener",
        widget=widgets.RadioSelectHorizontal
    )
    SDB7 = models.BooleanField(
        label="I'm always willing to admit it when I make a mistake",
        widget=widgets.RadioSelectHorizontal
    )
    SDB8 = models.BooleanField(
        label='There have been occasions when I felt like smashing things',
        widget=widgets.RadioSelectHorizontal
    )
    SDB9 = models.BooleanField(
        label='There have been times when I was quite jealous of the good fortune of others',
        widget=widgets.RadioSelectHorizontal
    )
    SDB10 = models.BooleanField(
        label='I never make a long trip without checking the safety of my car',
        widget=widgets.RadioSelectHorizontal
    )
    SDB11 = models.BooleanField(
        label='I sometimes think when people have a misfortune they only got what they deserved',
        widget=widgets.RadioSelectHorizontal
    )
    SDB12 = models.BooleanField(
        label="I have never deliberately said something that hurt someone's feelings",
        widget=widgets.RadioSelectHorizontal
    )
    SDB13 = models.BooleanField(
        label="When I don't know something I don't at all mind admitting it",
        widget=widgets.RadioSelectHorizontal
    )
    SDB14 = models.BooleanField(
        label='I am always courteous, even to people who are disagreeable',
        widget=widgets.RadioSelectHorizontal
    )
    SDB15 = models.BooleanField(
        label='At times I have really insisted on having things my own way',
        widget=widgets.RadioSelectHorizontal
    )
    SDB16 = models.BooleanField(
        label='I like to gossip at times',
        widget=widgets.RadioSelectHorizontal
    )
    SDB17 = models.BooleanField(
        label='I would never think of letting someone else be punished for my wrongdoings',
        widget=widgets.RadioSelectHorizontal
    )
    SDB18 = models.BooleanField(
        label='I can remember "playing sick" to get out of something',
        widget=widgets.RadioSelectHorizontal
    )
    Attitude12 = models.StringField(
        choices=likert_choices,
        label='For me, to have purchased slow fashion from an ethical clothing retailer would be effective',
        widget=widgets.RadioSelectHorizontal
    )
    Attitude22 = models.StringField(
        choices=likert_choices,
        label="The impact on the environment caused by purchasing from "
              "ethical clothing retailers would be effective",
        widget=widgets.RadioSelectHorizontal
    )
    Attitude32 = models.StringField(
        choices=likert_choices,
        label="The impact on employee welfare caused by purchasing from "
              "ethical clothing retailers would be effective",
        widget=widgets.RadioSelectHorizontal
    )
    Attitude42 = models.StringField(
        choices=likert_choices,
        label="The impact on animal welfare caused by purchasing from "
              "ethical clothing retailers would be effective",
        widget=widgets.RadioSelectHorizontal
    )
    Plan2 = models.StringField(
        choices=likert_choices,
        label="I have taken steps to purchase from ethical clothing "
              "retailers from home in the last month",
        widget=widgets.RadioSelectHorizontal
    )
