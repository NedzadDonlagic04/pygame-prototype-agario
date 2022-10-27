def getPercent(total, percent):
    if percent < 1 or percent > 100:
        percent = 50

    percent = total * percent / 100
    return round(percent)