import json

import pandas as pd
import time

# 读取 Excel 文件
file_path = "event_stream.xlsx"
data = pd.read_excel(file_path, header=None)


def diff(time1, time2):
    try:
        # 分解时间字符串
        minutes1, seconds1, microseconds1 = map(int, time1.split(":"))
        minutes2, seconds2, microseconds2 = map(int, time2.split(":"))

        # 将时间转换为总秒数
        total_seconds1 = minutes1 * 60 + seconds1
        total_seconds2 = minutes2 * 60 + seconds2

        # 计算差值
        return abs(total_seconds1 - total_seconds2)
    except ValueError:
        raise ValueError("时间格式不正确，请确保格式为 MM:SS:000000")


def send_col(raw_data):
    """
    将原始字符串解析为 JSON 格式，仅保留前 4 个键值对，并打印
    """
    # 将字符串按行分割
    lines = raw_data.strip().split('\n')

    # 提取键值对
    data_dict = {}
    for line in lines:
        parts = line.split(maxsplit=1)  # 按首个空格分割成两部分
        if len(parts) == 2:
            key, value = parts
        else:
            key, value = parts[0], None
        data_dict[key] = value

    # 保留前 4 个键值对
    limited_dict = dict(list(data_dict.items())[:4])

    # 转换为 JSON 格式并输出
    json_str = json.dumps(limited_dict, ensure_ascii=False, indent=4)
    print(json_str)


def read_stream():
    # 遍历表格内容
    i = 0
    while i + 1 < len(data):
        current_row = data.iloc[i]
        next_row = data.iloc[i + 1]

        first_col = str(current_row[0]).strip()
        next_col = str(next_row[0]).strip()
        stage = first_col

        # 检测阶段开始标志
        if first_col.startswith("第") and first_col.endswith("节"):
            send_col(str(data.iloc[i]).strip())
            i += 1
            send_col(str(data.iloc[i]).strip())
            i += 1
            send_col(str(data.iloc[i]).strip())

        # 检测阶段结束标志
        if next_col.startswith("第"):
            i += 1
            continue

        # 读取下一行时间差
        else:
            current_time = str(data.iloc[i][0])
            next_time = str(data.iloc[i + 1][0])
            time.sleep(diff(current_time, next_time) / 50)
            # 打印下一行内容
            send_col(str(data.iloc[i + 1]).strip())

        i += 1


if __name__ == "__main__":
    while 1:
        read_stream()

