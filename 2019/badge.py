"""
red orange yellow green blue purple

each line is 18 chars long

3 char chunks divided by 3


"""

from pprint import pprint

badge = [b'yygybpgrrybggrggro',
         b'ybprpygoygrgrpygoy',
         b'ypyybprpyopoypyybo',
         b'grrgrrybpgryypoybp',
         b'rpyyoyybogorgoygyo',
         b'rpygrbgoggyygyygrr',
         b'ybpoobrpyoppgorybp',
         b'ybogoyrpyypbgrgyby',
         b'rpygrggryrpyypoybp',
         b'goygoyypggryyporpy',
         b'goyypyypggoorpyypr',
         b'ybogoroobrpyyyrypy',
         b'ybprpygrbybogorgoy',
         b'gyorpygopypggrrgrr',
         b'rpyybyybprpygrggry',
         b'rpyyopybogoyrpyogy',
         b'oopoyooyroobrpyopb',
         b'grggorrpygoyypyybp',
         b'rpygryybpgyrgoyrpy',
         b'googoyybpgrbrpyypo',
         b'grgrpygoygrgrpyypy',
         b'goygoygrbogboopoop',
         b'yppgryypbyprgrogyr',
         b'ypryproobybggrrgog',
         b'ybyoopoyooggoopppp']

table = bytes.maketrans(b'roygbp',
                        b'012345')

trbadge = []
for row in badge:
    newrow = []
    row = row.translate(table)
    for i in range(0, 18, 3):
        try:
            n = int(row[i:i + 3], 6)
        except ValueError as e:
            print(e)
            print("row {}, i {}".format(row, i))
        newrow.append(n)
    trbadge.append(newrow)

pprint(trbadge)

for row in trbadge:
    for n in row:
        print(chr(n), end='')

print()

"""
the above gives a url, which if trimmed (the ppp doesn't match the pattern):
http://www.knjfmxff.club/19/

at first, it displayed a list of people. I've added their birthdays:

Long Distance Puzzle

Ada Lovelace        12/10/1815
Neal Stephenson     10/31/1959
Charles Babbage     12/26/1791
Nikola Tesla        07/10/1856
Stephen Hawking     01/08/1942
Niklaus Wirth       02/15/1934
Galileo Galilei     02/15/1564
Al Gore             03/31/1948
Marie Curie         11/07/1867
Daniel Trejo        05/16/1944
Aristotle           06/19/0384 (BC)

adding the digits of the birthdays multiple times...

"""

bdays = ["12101815",
         "10311959",
         "12261791",
         "07101856",
         "01081942",
         "02151934",
         "02151564",
         "03311948",
         "11071867",
         "05161944",
         "06190384"]


def sumdigits(s):
    s = str(s)
    sum = 0
    for c in s:
        sum += int(c)
    return sum

for bday in bdays:
    sum = sumdigits(bday)
    while sum > 9:
        sum = sumdigits(sum)
    print(sum, end="")
print()


"""
the above gives us a phone number.

12217762434

this number is incorrect. We aren't sure if the algorithm is correct. the page changed to
give us
13217792124

when called, it gives this url:
https://iesnah.com/z/
"""
