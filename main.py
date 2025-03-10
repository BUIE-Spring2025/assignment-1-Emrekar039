def int_to_roman(num):

    roman = ''

    if num // 1000 >= 1:
        roman = roman + (num // 1000) * 'M'
        num = num - num // 1000 * 1000

    if num // 500 >=1:
        if num // 100 == 9:
            roman += 'CM'
            num -= 900
        else :
            roman += 'D'
            num -= 500

    if num // 100 >=1:
        if num // 100 == 4:
            roman += 'CD'
            num -= 400
        if num // 10 == 9:
            roman = roman + num // 100 * 'XC'
            num -= 90
        else:
            roman += (num //100) * 'C'
            num -= (num // 100) * 100

        
    if num // 50 >=1 :
        if num // 10 == 9:
            roman += 'XC'
            num -= 90
        else:
            roman = roman + (num // 50) * 'L'
            num = num - (num // 50) * 50

    if  num // 10 >=1 and num // 10 < 4:
        roman = roman + (num // 10) * 'X'
        num = num - num // 10 * 10

    if num == 9:
        roman += 'IX'
    if num <=8 and num >=5:
        roman += 'V' + (num % 5) * 'I'     
    if num == 4:
        roman += 'IV'
    if num <= 3:
        roman += (num % 5) * 'I'

    
    return roman
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
