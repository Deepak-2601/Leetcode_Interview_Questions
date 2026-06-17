class Leaderboard(object):
    def __init__(self):
        self.scores = {}

    def addScore(self, playerId, score):
        if playerId in self.scores:
            self.scores[playerId] += score
        else:
            self.scores[playerId] = score

    def top(self, K):
        sorted_scores = sorted(self.scores.values(), reverse=True)
        return sum(sorted_scores[:K])

    def reset(self, playerId):
        if playerId in self.scores:
            del self.scores[playerId]

leaderboard = Leaderboard()
leaderboard.addScore(1, 5)
leaderboard.addScore(2, 10)
print(leaderboard.top(1))
leaderboard.reset(1)
print(leaderboard.top(1))
