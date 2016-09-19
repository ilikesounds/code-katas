"""
    This module will take in a json file of billionaires and output the
    youngest billionaire whose age is above 0. Thereby making you feel crappier
    about your current income.
"""

import json


def age_check():
    """
    This function returns an dictionary object of the stats of the youngest
    billionaire older than 0 on the forbes billionaire list.
    """
    youngest = 80
    output = {}

    with open('../data/forbes_billionaires_2016.json') as data_file:
        data = (json.loads(data_file.read()))

    for val in data:
        if val['age'] < youngest and val['age'] > 0:
            youngest = val['age']
            output = val
        else:
            pass
    nw = str(output['net_worth (USD)'])[0:3]
    nw = float(nw[0:2] + '.' + nw[2:3])
    result = '{} is the youngest billionaire on this list with a fortune made \
from {} and a networth of {:.1f} billion dollars.'.format(
            output['name'],
            output['source'],
            nw
            )
    return result

if __name__ == '__main__':
    age_check()
