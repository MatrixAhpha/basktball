import json
from enum import Enum

from match_singleton import MatchSingleton


class Event(Enum):
    FOUL = "犯规"
    TWO_POINTS = "2分进球"
    THREE_POINTS = "3分进球"
    FREE_THROW = "罚球"
    BLOCK = "盖帽"
    OUT_OF_BOUNDS = "球出界"


class Team(Enum):
    HOME = "主队"
    AWAY = "客队"


class BallPossession(Enum):
    HOME = "主队"
    AWAY = "客队"


def update_team_stats(team, event):
    if event == Event.TWO_POINTS:
        team.two_points += 2
    elif event == Event.THREE_POINTS:
        team.three_points += 3
    elif event == Event.FREE_THROW:
        team.free_throws += 1
    elif event == Event.FOUL:
        team.fouls += 1
    elif event == Event.BLOCK:
        team.blocks += 1
    elif event == Event.OUT_OF_BOUNDS:
        team.out_of_bounds += 1


def addup(time, msg1, score, msg2):
    """
    处理接收到的 JSON 消息，将其解析为键值对变量
    """
    match = MatchSingleton.get_instance()
    if msg1 == "NaN":
        team_stats = match.away_team_stats
        msg = msg2
    else:
        team_stats = match.home_team_stats
        msg = msg1
    if score != "NaN":
        try:
            c_home_score, c_away_score = map(int, score.split("-"))
        except ValueError:
            raise ValueError("Invalid score format, expected 'int:int'.\nscore:{}".format(msg1))
        # 更新比赛比分和时间
        match.score = (c_home_score, c_away_score)
        # 判断事件
        if "命中" in msg:
            if c_away_score + c_home_score - match.score[0] - match.score[1] == 2:
                team_stats.add_two_points()
            else:
                team_stats.add_three_points()
        elif "犯规" in msg:
            team_stats.add_foul()
        elif "封盖" in msg:
            team_stats.add_block()
        elif "篮板" in msg:
            team_stats.add_rebound()
    match.time = time


def process_message(message):
    """
    处理接收到的 JSON 消息，将其解析为键值对变量
    """
    try:
        # 将 JSON 字符串转换为字典
        message_dict = json.loads(message)

        # 提取前四个键值对
        keys = list(message_dict.keys())
        key1, key2, key3, key4 = (keys + [None] * 4)[:4]  # 确保始终有 4 个键
        time = message_dict.get(key1, None)
        msg1 = message_dict.get(key2, None)
        score = message_dict.get(key3, None)
        msg2 = message_dict.get(key4, None)
        addup(time, msg1, score, msg2)
        if msg1 != "NaN":
            print(msg1)
        if msg2 != "NaN":
            print(msg2)
        match = MatchSingleton.get_instance()
        print(match)

    except json.JSONDecodeError:
        print("接收到的消息不是有效的 JSON 格式:", message)
