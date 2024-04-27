

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            if i != "../":
                if i != "./":
                    stack.append(i)
            else:
                if stack: stack.pop()
        return len(stack)

        # idx = 0
        # for i in range(len(logs)):
        #     if logs[i] == "../" :
        #         if idx > 0: idx -= 1
        #     elif logs[i] == "./": pass
        #     else:
        #         idx += 1
        # return idx

        # stack = []
        # for i in range(len(logs)):
        #     if logs[1] == '../': return 0
        #     if logs[i] == "../" and stack :
        #         return len(stack)
        #     elif logs[i] == "./":
        #         pass
        #     else:
        #         stack.append(logs[i])

 

        # index = 0
        # fl = []
        # while (index < len(fl)):
        #     if logs[index] == "./":
        #         pass
        #     elif logs[index] == "../":
        #         if len(fl) > 0:
        #             fl.pop()
        #     else:
        #         fl.append(logs[index])
        #     i += 1
        # return len(fl)