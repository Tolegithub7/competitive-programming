class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        for char in path + '/':
            if char == "/":
                if cur == "..":
                    if stack: stack.pop()
                elif cur != "" and cur != ".": stack.append(cur)
                cur = ''
            else:
                cur += char
        return '/'+'/'.join(stack)
        # stack = []
        # cur = ""
        # for char in path + '/':
        #     if char == '/':
        #         if cur == '..':
        #             if stack: stack.pop()
        #         elif cur != '' and cur != '.': stack.append(cur)
        #         cur = ''
        #     else: 
        #         cur += char 
        # return '/'+"/".join(stack) 


        # stack = []
        # cur = ""
        # for c in path + "/":
        #     if c == "/":
        #         if cur == "..":
        #             if stack:
        #                 stack.pop()
        #         elif cur != "" and cur != ".":
        #             stack.append(cur)
        #         cur = ""
        #     else :
        #         cur += c
        # return "/" + "/".join(stack)
        
        # path_arr = path.split('/')
        # new_path = []
        # for folder in path_arr:
        #     if folder == ".." and len(new_path) > 0:
        #         new_path.pop(-1)
        #     elif folder != "." and folder != "" and folder != "..":
        #         new_path.append(folder)
        # return "/" + "/".join(new_path)
        