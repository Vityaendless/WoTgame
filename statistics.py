class Statistic():
    """statistics"""

    def __init__(self):
        """statistic initialization"""
        self.reset_statistic()
        self.lives_marker = True
        with open('high_score.txt', 'r') as file:
            self.high_score = int(file.readline())

    def reset_statistic(self):
        """reset statistic"""
        self.moiraine_lives = 2
        self.score = 0