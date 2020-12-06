class Gematria:
    _HEBREW_LETTERS = [
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
        ]
    _REVERSED_HEBREW_LETTERS = _HEBREW_LETTERS[::-1]

    def number_to_hebrew(self, number: int) -> str:
        """
        Convert number to Hebrew letter(s)

        Examples:
            2  = "ב"
            47 = "מז"
        """
        if number <= 0:
            raise Exception("Number must be bigger than zero")
        if number >= 1000:
            raise Exception("Number bigger than 999 is not supported yet")

        remainder = number
        heb_sum = ""
        while remainder > 0:
            for heb_letter, val in self._REVERSED_HEBREW_LETTERS:
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
