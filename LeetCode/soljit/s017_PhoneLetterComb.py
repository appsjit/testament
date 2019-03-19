class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def buildRec(generatedComb, remDigit):
            if len(remDigit) == 0:
                result.append(generatedComb)
            else:
                ##print(remDigit[1:])
                for x in phone[remDigit[0]]:
                    buildRec(generatedComb + x, remDigit[1:])

        if (digits == ''):
            return []

        buildRec("", digits)

        return result
