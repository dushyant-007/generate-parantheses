class Solution:
    def generateParenthesis(self, n: int) :
        prev = {'()':1}
        next = {}
        if n == 1 :
            next = prev
            return list(next.keys())
        for i in range(2, n+1):
            next = {}
            for key in prev:
                #print(key)
                for i in range(len(key)):
                    new_string = key[:i] + '()' + key[i:]
                    next[new_string] = 1
            prev = next
        return list(prev.keys())