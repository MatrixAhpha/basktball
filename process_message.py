import json


def update_team_stats(team_stats, score_diff):
    if score_diff == 2:
        team_stats.two_points += 2
    elif score_diff == 3:
        team_stats.three_points += 3


def addup(time, msg1, score, msg2, match):
    """
    处理接收到的 JSON 消息，将其解析为键值对变量
    """
    try:
        c_home_score, c_away_score = map(int, score.split("-"))
    except ValueError:
        raise ValueError("Invalid score format, expected 'int:int'.")
    # 计算分差
    home_score_diff = c_home_score - match.score[0]
    away_score_diff = c_away_score - match.score[1]

    # 更新主队得分
    if home_score_diff > 0:
        update_team_stats(match.home_team_stats, home_score_diff)

    # 更新客队得分
    if away_score_diff > 0:
        update_team_stats(match.away_team_stats, away_score_diff)

    # 更新比赛比分
    match.score = (c_home_score, c_away_score)


def process_message(message, window, match):
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
        addup(time, msg1, score, msg2, match)
        if msg1 != "NaN":
            print(msg1)
        if msg2 != "NaN":
            print(msg2)
        print(match)

    except json.JSONDecodeError:
        print("接收到的消息不是有效的 JSON 格式:", message)
