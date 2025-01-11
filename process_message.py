import json
import re

from match_singleton import MatchSingleton


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
    try:
        c_home_score, c_away_score = map(int, score.split("-"))
    except ValueError:
        raise ValueError("Invalid score format, expected 'int:int'.\nscore:{}".format(msg1))
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
    # 更新比赛比分和时间
    match.score = (c_home_score, c_away_score)
    match.time = time


def process_message(message):
    """
    处理接收到的 JSON 消息，将其解析为键值对变量
    """
    print(message)
    match = MatchSingleton.get_instance()
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
        if re.match(r"^\d+-\d+$", score):
            addup(time, msg1, score, msg2)
        elif time == "时间":
            match.update_teams(msg1, msg2)
        elif re.match(r"^第[1-4]节$", time):
            match.set_quarter(time)
        if msg1 != "NaN":
            print(msg1)
        if msg2 != "NaN":
            print(msg2)
        print(match)

        match.window.event_managers["bottom"].update.emit()

    except json.JSONDecodeError:
        print("接收到的消息不是有效的 JSON 格式:", message)
