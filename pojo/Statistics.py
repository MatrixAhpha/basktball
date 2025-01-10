class Statistics:
    """
    技术统计类，包含队伍的比赛统计信息。
    """
    def __init__(self, two_points=0, three_points=0, fouls=0, blocks=0, rebounds=0):
        self.two_points = int(two_points)  # 2分球得分
        self.three_points = int(three_points)  # 3分球得分
        self.fouls = int(fouls)  # 犯规数
        self.blocks = int(blocks)  # 盖帽数
        self.rebounds = int(rebounds)  # 篮板数

    def __str__(self):
        return (f"2分球得分: {self.two_points}, 3分球得分: {self.three_points}, "
                f"犯规数: {self.fouls}, 盖帽数: {self.blocks}, 篮板数: {self.rebounds}")
