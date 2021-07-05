from collections import OrderedDict


HEBREW_LETTERS: OrderedDict = OrderedDict([
    ("א", 1),
    ("ב", 2),
    ("ג", 3),
    ("ד", 4),
    ("ה", 5),
    ("ו", 6),
    ("ז", 7),
    ("ח", 8),
    ("ט", 9),
    ("י", 10),
    ("כ", 20),
    ("ל", 30),
    ("מ", 40),
    ("נ", 50),
    ("ס", 60),
    ("ע", 70),
    ("פ", 80),
    ("צ", 90),
    ("ק", 100),
    ("ר", 200),
    ("ש", 300),
    ("ת", 400)
])


def to_hebrew(number: int) -> str:
    """
    Convert number to Hebrew letter(s).

    Examples:
        to_hebrew(2)  # => "ב"
        to_hebrew(47) # => "מז"
    """
    if number <= 0:
        raise Exception("Number must be bigger than zero")
    if number >= 1000:
        raise Exception("Number bigger than 999 is not yet supported")

    remainder = number
    heb_sum = ""
    while remainder > 0:
        for heb_letter, val in reversed(HEBREW_LETTERS.items()):
            if (val <= remainder):
                if remainder == 15:
                    heb_sum += "טו"
                    remainder = 0
                elif remainder == 16:
                    heb_sum += "טז"
                    remainder = 0
                else:
                    heb_sum += heb_letter
                    remainder -= val
                break
    return heb_sum


def to_number(hebrew: str) -> int:
    """
    Convert Hebrew letters to number. Ignore Non-Hebrew letters.

    Examples:
        to_number("ב")  # => 2
        to_number("מז") # => 47
    """
    sum = 0
    for letter in hebrew:
        sum += HEBREW_LETTERS.get(letter, 0)
    return sum
