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
    oldest_diff = 80
    current_oldest = 80
    output = {}
    output2 = {}

    with open('../data/forbes_billionaires_2016.json') as data_file:
        data = (json.loads(data_file.read()))

    for val in data:
        if val['age'] < youngest and val['age'] > 0:
            youngest = val['age']
            output = val
        elif val['age'] < 80:
            oldest_diff = 80 - val['age']
            if current_oldest < oldest_diff and val['age'] > 0:
                current_oldest = oldest_diff
                output2 = val
    nw = str(output['net_worth (USD)'])[0:3]
    nw = float(nw[0:2] + '.' + nw[2:3])
    nw2 = str(output2['net_worth (USD)'])[0:3]
    nw2 = float(nw2[0:2] + '.' + nw2[2:3])
    result1 = '{} is the youngest billionaire on this list with a fortune made \
    from {} and a net worth of {:.1f} billion dollars.'.format(
            output['name'],
            output['source'],
            nw
            )
    result2 = '{} is the oldest billionaire under 85 on this list with a\
    fortune made from {} and a net worth of {:.1f} billion dollars.'.format(
            output2['name'],
            output2['source'],
            nw
            )
    return result1, result2

if __name__ == '__main__':
    age_check()
