"""
468. Validate IP Address

Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" 
if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 
and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0"
are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" 
are invalid IPv4 addresses.


A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

- 1 <= xi.length <= 4
- xi is a hexadecimal string which may contain digits, lowercase English letter 
  ("a" to "f") and upper-case English letters ("A" to "F").
- Leading zeros are allowed in xi.

For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and
"2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, 
while "2001:0db8:85a3::8A2E:037j:7334" and 
"02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.
"""


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            return self.is_valid_ipv4(queryIP)
        elif ":" in queryIP:
            return self.is_valid_ipv6(queryIP)
        else:
            return "Neither"

    @staticmethod
    def is_valid_ipv4(queryIP: str) -> str:
        if queryIP.count(".") != 3:
            return "Neither"

        for part in queryIP.split("."):
            if len(part) == 0 or (len(part) > 1 and part[0] == "0") or len(part) > 3:
                return "Neither"
            number = 0
            for ch in part:
                if not ch.isdigit():
                    return "Neither"
                number = number * 10 + ord(ch) - 48
            if number > 255:
                return "Neither"

        return "IPv4"

    @staticmethod
    def is_valid_ipv6(queryIP: str) -> str:
        if queryIP.count(":") != 7:
            return "Neither"

        hex_digit = {
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
        }

        for part in queryIP.split(":"):
            if len(part) == 0 or len(part) > 4:
                return "Neither"
            for ch in part:
                if ch not in hex_digit:
                    return "Neither"

        return "IPv6"
