from pojo.Statistics import Statistics


class Match:
    """
    比赛类，包含主队和客队的名称、图标、比分、时间及技术统计。
    """

    def __init__(self, home_team, away_team, current_time="00:00", current_score=(0, 0), window=None):
        self.home_team = home_team  # 主队名称
        self.away_team = away_team  # 客队名称
        self.window = window  # 新增 window 属性

        # 主队和客队图标
        self.home_team_icon = f"assets/{home_team}.jpg"
        self.away_team_icon = f"assets/{away_team}.jpg"

        self.time = current_time  # 当前时间 (aa:bb)
        self.score = current_score  # 当前比分 (主队:客队)

        # 主队和客队技术统计
        self.home_team_stats = Statistics()
        self.away_team_stats = Statistics()

    def update_teams(self, home_team, away_team):
        """
        更新主队和客队的名称及图标。
        """
        self.home_team = home_team
        self.away_team = away_team
        self.home_team_icon = f"assets/{home_team}.jpg"
        self.away_team_icon = f"assets/{away_team}.jpg"

    def __str__(self):
        return (f"比赛时间: {self.time}, 比分: {self.score}\n"
                f"主队: {self.home_team}, 图标: {self.home_team_icon}\n"
                f"客队: {self.away_team}, 图标: {self.away_team_icon}\n"
                f"主队技术统计: {self.home_team_stats}\n"
                f"客队技术统计: {self.away_team_stats}")

    def set_window(self, window):
        self.window = window
