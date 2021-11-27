class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        ## R stands for row kind of Y axis
        ## C stands for column kind of X axis
        locR = 0
        locC = 0
        ## Direction
        dirR = 1
        dirC = 0
        ctr = 0

        while ctr < 5:
            for instr in instructions:
                if instr == 'G':
                    locR += dirR
                    locC += dirC
                elif instr == 'L':
                    ## N 1,0
                    ## S -1,0
                    ## E 0,1
                    ## W 0,-1
                    ## Assuming from North 1,0 if we take Left Turn
                    ## Location should be 0, 1
                    ## To make 0, 1 we need to swap and change sign
                    dirR, dirC = dirC, -1 * dirR
                elif instr == 'R':
                    dirR, dirC = -1 * dirC, dirR

            if (locR == 0 and locC == 0):
                return True
            else:
                ctr += 1

        return False
