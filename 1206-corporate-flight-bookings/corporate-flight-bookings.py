class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # ps = [[0] * n for _ in range(n)]
        # for i in range(len(bookings)):
        #     for m in range(bookings[i][0], bookings[i][1]+1):
        #         ps[i][m-1] = bookings[i][2]
        # ps1 = [0] * n
        # for i in range(n):
        #     for j in range(n):
        #         ps1[j] += ps[i][j]
        # return ps1

        track = [0]*(n+1)
        for f, l, s in bookings:
            track[f-1] += s
            track[l] -= s
        for _ in range(1, n+1):
            track[_] += track[_-1]
        return track[:-1]