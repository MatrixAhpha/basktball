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
        self.event_manager = None

    def __str__(self):
        return (f"2分球得分: {self.two_points}, 3分球得分: {self.three_points}, "
                f"犯规数: {self.fouls}, 盖帽数: {self.blocks}, 篮板数: {self.rebounds}")

    def set_event_manager(self, event_manager):
        self.event_manager = event_manager

    def add_two_points(self):
        self.two_points += 2
        self.event_manager.two_points.emit()

    def add_three_points(self):
        self.three_points += 3

    def add_foul(self):
        self.fouls += 1

    def add_block(self):
        self.blocks += 1

    def add_rebound(self):
        self.rebounds += 1
