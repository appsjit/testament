class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backTrack(s='', lp=0, rp=0):
            ##print(s+'  '+str(lp)+' '+str(rp))
            if len(s) == 2 * n:
                result.append(s)
                return
            if lp < n:  ## Fill left ( for n
                backTrack(s + '(', lp + 1, rp)

            if rp < lp:  ## Fill right ) to match left lp
                backTrack(s + ')', lp, rp + 1)

        backTrack()
        ##print(result)
        return result

        ## Create List of numbers 1 to 4
        ## fList = range(1,p*2 + 1)
        ## arrange all 4 numbers in all combination
        ## replace even with lp and odd with rp
