import json


def process_message(message, window):
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
        print(time, msg1, score, msg2)

    except json.JSONDecodeError:
        print("接收到的消息不是有效的 JSON 格式:", message)