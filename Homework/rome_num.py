def decode_rome(r):
    dec = [0]
    d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for el in r:
        dec.append(d[el])
    return dec

def rome_2_dec(r):
    a = decode_rome(r)
    a = a[::-1]
    dec = 0
    i = 0
    while i < len(a) - 1:
        if a[i] <= a[i + 1]:
           dec += a[i]
           i += 1
        else:
            dec += a[i] - a[i + 1]
            i += 2

    return dec


def dec_2_rome(a):
    rome = ''
    for i in range(a):
        if a - 1000 >= 0:
            rome = rome + 'M'
            a -= 1000
        elif a - 999 > 0:
            rome = rome + 'IM'
            a -= 999
        elif a - 990 >= 0:
            rome = rome + 'XM'
            a -= 990
        elif a - 950 >= 0:
            rome = rome + 'LM'
            a -= 950
        elif a - 900 >= 0:
            rome = rome + 'CM'
            a -= 900
        elif a - 500 >= 0:
            rome = rome + 'D'
            a -= 500
        elif a - 499 > 0:
            rome = rome + 'ID'
            a -= 499
        elif a - 490 >= 0:
            rome = rome + 'XD'
            a -= 490
        elif a - 450 >= 0:
            rome = rome + 'LD'
            a -= 450
        elif a - 400 >= 0:
            rome = rome + 'CD'
            a -= 400
        elif a - 100 >= 0:
            rome = rome + 'C'
            a -= 100
        elif a - 99 > 0:
            rome = rome + 'IC'
            a -= 99
        elif a - 90 >= 0:
            rome = rome + 'XC'
            a -= 90
        elif a - 50 >= 0:
            rome = rome + 'L'
            a -= 50
        elif a - 40 >= 0:
            rome = rome + 'XL'
            a -= 40
        elif a - 10 >= 0:
            rome = rome + 'X'
            a -= 10
        elif a - 9 >= 0:
            rome = rome + 'IX'
            a -= 9
        elif a - 8 >= 0:
            rome = rome + 'VIII'
            a -= 8
        elif a - 7 >= 0:
            rome = rome + 'VII'
            a -= 7
        elif a - 6 >= 0:
            rome = rome + 'VI'
            a -= 6
        elif a - 5 >= 0:
            rome = rome + 'V'
            a -= 5
        elif a - 4 >= 0:
            rome = rome + 'IV'
            a -= 4
        elif a - 1 >= 0:
            rome = rome + 'I'
            a -= 1

    return rome


a = input()
b = a.split('+')

x = rome_2_dec(b[0])
y = rome_2_dec(b[1])

summ = x + y
print(dec_2_rome(summ))
