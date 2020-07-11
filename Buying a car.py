def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    doubleMonth = month = savings = 0
    while startPriceNew > startPriceOld + savings:
        doubleMonth += 1
        if doubleMonth == 2:
            percentLossByMonth += 0.5
            doubleMonth = 0
        savings += savingperMonth
        startPriceNew = (startPriceNew / 100) * (100 - percentLossByMonth)
        startPriceOld = (startPriceOld / 100) * (100 - percentLossByMonth)
        month += 1
    return [month, round((startPriceOld + savings) - startPriceNew)]
