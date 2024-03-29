class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chem, lt, rt = 0, 0, len(skill)-1
        const = skill[lt] + skill[rt]
        while lt<rt:
            const1 = skill[lt] + skill[rt]
            che = skill[lt] * skill[rt]
            if const1 != const:
                return -1 
                break
            lt += 1
            rt -= 1
            chem += che
        return chem

