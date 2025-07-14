class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        i = 0
        n = len(command)
        while i < n:
            if command[i] =='G':
               ans.append('G') 
               i += 1

            elif i + 1 < n and command[i: i + 2] =='()':
                ans.append('o')
                i += 2
            elif i + 3 < n and command[i : i + 4] == '(al)':
                ans.append('al')
                i += 4
            else:
                ans.append(command[i])
                i += 1
        return ''.join(ans)
