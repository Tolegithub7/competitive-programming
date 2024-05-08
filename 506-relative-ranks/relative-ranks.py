class Solution:
  def findRelativeRanks(self, score: List[int]) -> List[str]:
    sorted_scores = sorted(score, reverse=True)
    rank_dict = {}
    for i, s in enumerate(sorted_scores):
        if i == 0:
            rank_dict[s] = "Gold Medal"
        elif i == 1:
            rank_dict[s] = "Silver Medal"
        elif i == 2:
            rank_dict[s] = "Bronze Medal"
        else:
            rank_dict[s] = str(i + 1)
    result = []
    for s in score:
        result.append(rank_dict[s])
    return result