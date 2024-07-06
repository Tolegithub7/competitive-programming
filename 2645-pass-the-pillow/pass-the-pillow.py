class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cur_pos = 1
        cur_time = 0
        dir = 1
        while cur_time < time:
            if 0 < cur_pos + dir <= n:
                cur_pos += dir
                cur_time += 1
            else:
                dir *= -1
        return cur_pos