"""
    This module will take in a json file of billionaires and output the
    youngest billionaire whose age is above 0. Thereby making you feel crappier
    about your current income.
"""


def age_check(json):
    """
    This function returns an dictionary object of the stats of the youngest
    billionaire older than 0 on the forbes billionaire list.
    """
    youngest = 80
    output = {}

    with open('forbes_billionaires_2016.json') as data_file:
        data = (json.loads(data_file.read()))

    for val in data:
        if val['age'] < youngest and val['age'] > 0:
            youngest = val['age']
            output = val
        else:
            pass
            return '{} is the youngest billionaire on this list with a fortune \
            made in {} and a networth of {}.' % output['name'], output['industry'], output['networth']
