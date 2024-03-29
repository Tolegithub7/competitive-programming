class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # skill.sort()
        # chemistry = 0
        # for i in range(0, len(skill)//2):
        #     chemistry += (skill[i]*skill[len(skill)-1-i])
        # if len(skill)<=2:
        #     return skill[0]*skill[1]
        # if len(skill) % 2 == 0 and skill[i] == skill[len(skill)-1-i] and len(skill)>2:
        #     return chemistry
        # else:
        #     return -1
        
        skill.sort()
        # lst = []
        lt, rt = 0, len(skill)-1
        const = skill[lt] + skill[rt]
        chem = 0
        while lt<rt:
            const1 = skill[lt] + skill[rt]
            che = skill[lt] * skill[rt]
            if const1 != const:
                return -1 
                break
            # lst.append([skill[lt], skill[rt]])
            lt += 1
            rt -= 1
            chem += che
        return chem

