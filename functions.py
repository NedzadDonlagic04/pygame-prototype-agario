from math import sqrt, pow

def getPercent(total, percent):
    if percent < 1 or percent > 100:
        percent = 50

    percent = total * percent / 100
    return round(percent)

def getDistance(offSetX1, offSetY1, offSetX2, offSetY2):
    a = offSetX2 - offSetX1
    b = offSetY2 - offSetY1
    return sqrt(pow(a, 2) + pow(b, 2))