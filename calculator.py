import math

def yearsAmount(sumAmountOnDeposit: int, percent: int, sumAim: int)->int:
    if sumAmountOnDeposit<=0:
        raise Exception("Размер вклада должен быть больше 0")
    if percent<=0:
        raise Exception("% вклада должен быть больше 0")
    if sumAim<=0:
        raise Exception("Сумма для получения должна быть больше 0")
    if sumAim<sumAmountOnDeposit:
        raise Exception("Сумма для получения должна быть больше размера вклада")
    return math.ceil((sumAim-sumAmountOnDeposit)/(sumAmountOnDeposit*(percent/100)))
