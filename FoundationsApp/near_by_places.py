"""
title: nesr_by_places
author: Phillip Hall
date: 2019-10-22 11:51
"""


THD_HQ_LatLong = {
    "MTC": {"lat":33.9179089,"long":-84.4976419},
    "SSC": {"lat":33.8652169,"long":-84.4842768},
    "Austin Tech Center": {"lat":30.4087195,"long":-97.6638078},
    "Dallas Tech Center": {"lat":32.91277,"long":-96.9872895}
}


def distance_formula(coordinates1={}, coordinates2={}):
    """
    d=(x2​−x1​)^2+(y2​−y1​)^2

    :param coordinates1: latlong dictionary
    :param coordinates2: latlong dictionary
    :return:
    """
    import math

    xs = (coordinates2['lat'] - coordinates1["lat"])**2
    ys = (coordinates2['long'] - coordinates1["long"])**2

    print(xs, ys, math.sqrt(xs+ys), sep='\n')


if __name__ == '__main__':
    distance_formula(THD_HQ_LatLong['MTC'], THD_HQ_LatLong['SSC'])