# Uses python3
import sys

def get_powerset(pstr):
    # write your code here
    result = []

    def traver(psstr,dep):
        if(dep >= len(psstr)):
            result.append(psstr)
            return

        traver(psstr,dep + 1)


    traver("",0)
    return result



if __name__ == '__main__':
    ##input = sys.stdin.read()
    str = str(input())
    print(get_powerset(str))
