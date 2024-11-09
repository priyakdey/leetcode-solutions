"""
1507. Reformat Date

Given a date string in the form Day Month Year, where:

- Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
- Month is in the set
  {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
- Year is in the range [1900, 2100].

Convert the date string to the format YYYY-MM-DD, where:

- YYYY denotes the 4 digit year.
- MM denotes the 2 digit month.
- DD denotes the 2 digit day.
"""
from typing import Dict


class Solution:
    def reformatDate(self, date: str) -> str:
        months: Dict[str, int] = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

        curr: int = 0
        while curr < len(date) and 48 <= ord(date[curr]) <= 57:
            curr += 1

        if curr == len(date):
            raise Exception("invalid date format")

        try:
            dd = int(date[: curr])
        except ValueError:
            raise Exception("invalid date")

        # skip over the letters and the space
        curr += 3

        if curr >= len(date):
            raise Exception("invalid date format")

        month: str = date[curr: curr + 3]
        if month not in months:
            raise Exception("invalid month")
        mm = months[month]

        # skip over the space
        curr += 4
        if curr >= len(date):
            raise Exception("invalid date format")

        try :
            year = int(date[curr:])
        except ValueError:
            raise Exception("invalid year")

        return f"{year}-{mm}-{dd}"
