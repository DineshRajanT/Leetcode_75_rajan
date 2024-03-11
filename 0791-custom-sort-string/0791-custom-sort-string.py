class Solution:
    def customSortString(self, order: str, s: str) -> str:
        customOrder = {}
        for i in range(len(order)):
            customOrder[order[i]] = i

        orderStr = ["" for _ in range(len(order))]
        unorderStr = ""

        for char in s:
            if char in customOrder:
                orderStr[customOrder[char]] += char
            else:
                unorderStr += char

        orderNewStr = ""
        for part in orderStr:
            orderNewStr += part

        return orderNewStr + unorderStr

