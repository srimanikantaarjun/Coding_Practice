# https://leetcode.com/problems/defanging-an-ip-address/

# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".


class Solution:
    def defangIPaddr(self, address: str) -> str:
        a = address.replace(".", "[.]")
        return a


# More Pythonic solution

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))

# Faster than above solution but consumes extra space
