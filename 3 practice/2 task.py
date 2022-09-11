def season(month):
    if month == 12 or month <= 2:
        return 'White snow fell outside the window'
    elif month < 5:
        return '"Birds sang beautiful songs'
    elif month < 8:
        return 'The sun shone brighter than ever'
    elif month < 11:
        return 'The harvest was incredible'
    else:
        return False


month = int(input('enter the number of month:\n'))
print(season(month))
