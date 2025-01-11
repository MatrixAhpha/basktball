from pojo.Statistics import Statistics


class Team_Statistics(Statistics):
    """
    技术统计类，包含队伍的比赛统计信息。
    """

    def __init__(self, two_points=0, three_points=0, fouls=0, blocks=0, rebounds=0):
        # 初始化父类属性
        super().__init__(two_points, three_points, fouls, blocks, rebounds)
        # 初始化事件管理器
        self.event_manager = None

    def set_event_manager(self, event_manager):
        self.event_manager = event_manager

    def add_two_points(self):
        self.two_points += 2
        self.event_manager.two_points.emit()

    def add_three_points(self):
        self.three_points += 3
        self.event_manager.three_points.emit()

    def add_foul(self):
        self.fouls += 1
        self.event_manager.foul.emit()

    def add_block(self):
        self.blocks += 1
        self.event_manager.block.emit()

    def add_rebound(self):
        self.rebounds += 1
