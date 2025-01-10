# match_singleton.py
from pojo.Match import Match


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
