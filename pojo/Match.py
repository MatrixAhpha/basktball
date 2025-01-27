from PyQt6.QtWidgets import QLabel

from pojo.Team_Statistics import Team_Statistics


class MatchSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        """
        获取 Match 的单例实例
        """
        if MatchSingleton._instance is None:
            MatchSingleton._instance = Match(None, None)
        return MatchSingleton._instance


class Match:
    """
    比赛类，包含主队和客队的名称、图标、比分、时间及技术统计。
    """

    def __init__(self, home_team, away_team, current_time="00:00", current_score=(0, 0), window=None, quarter="第1节"):
        self.home_team = home_team  # 主队名称
        self.away_team = away_team  # 客队名称
        self.window = window  # 新增 window 属性

        # 主队和客队图标
        self.home_team_icon = f"assets/{home_team}.jpg"
        self.away_team_icon = f"assets/{away_team}.jpg"

        self.time = current_time  # 当前时间 (aa:bb)
        self.score = current_score  # 当前比分 (主队:客队)

        # 主队和客队技术统计
        self.home_team_stats = Team_Statistics()
        self.away_team_stats = Team_Statistics()

        self.quarter = quarter
        self.new_event = None

    def update_teams(self, home_team, away_team):
        """
        更新主队和客队的名称及图标。
        """
        self.home_team = home_team
        self.away_team = away_team
        self.home_team_icon = f"assets/{home_team}.png"
        self.away_team_icon = f"assets/{away_team}.png"

    def __str__(self):
        return (f"比赛时间: {self.time}, 比分: {self.score}\n"
                f"当前节次: {self.quarter}\n"
                f"主队: {self.home_team}, 图标: {self.home_team_icon}\n"
                f"客队: {self.away_team}, 图标: {self.away_team_icon}\n"
                f"主队技术统计: {self.home_team_stats}\n"
                f"客队技术统计: {self.away_team_stats}"
                f"最新事件: {self.new_event}")

    def set_window(self, window):
        self.window = window
        self.home_team_stats.set_event_manager(window.event_managers["main_court"])
        self.away_team_stats.set_event_manager(window.event_managers["sub_court"])

    def set_quarter(self, quarter):
        self.quarter = quarter

    def get_icon(self, court):
        if court == self.window.findChild(QLabel, "main_court"):
            return self.home_team_icon
        elif court == self.window.findChild(QLabel, "sub_court"):
            return self.away_team_icon

    def clear(self):
        """
        重置比赛的所有数据。
        """
        self.home_team = ""
        self.away_team = ""
        self.home_team_icon = ""
        self.away_team_icon = ""
        self.time = "00:00"
        self.score = (0, 0)
        self.quarter = "第1节"
        self.new_event = None
        self.home_team_stats.clear()  # 重置主队技术统计
        self.away_team_stats.clear()  # 重置客队技术统计
