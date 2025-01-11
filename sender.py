import json
import pandas as pd
import asyncio
import websockets

# 读取 Excel 文件
file_path = "event_stream.xlsx"
data = pd.read_excel(file_path, header=None)
connected_clients = set()
sent_data_log = []


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


def to_json(raw_data):
    """
    将原始字符串解析为 JSON 格式，仅保留前 4 个键值对。
    如果第一个键值对的值为 aa:bb:cc 格式，仅保留 aa:bb。
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

        # 检查第一个键值对的值是否为 aa:bb:cc 格式
        if len(data_dict) == 0 and value and ':' in value:
            time_parts = value.split(':')
            if len(time_parts) == 3:
                value = ':'.join(time_parts[:2])  # 保留前两部分

        data_dict[key] = value

    # 保留前 4 个键值对
    limited_dict = dict(list(data_dict.items())[:4])

    # 转换为 JSON 格式
    return json.dumps(limited_dict, ensure_ascii=False, indent=4)


async def broadcast(data_send):
    # 向所有客户端广播
    if connected_clients:
        await asyncio.gather(*(client.send(data_send) for client in connected_clients))


async def read_stream():
    # 遍历表格内容
    i = 0
    while i + 1 < len(data):
        current_row = data.iloc[i]
        next_row = data.iloc[i + 1]

        first_col = str(current_row[0]).strip()
        next_col = str(next_row[0]).strip()

        # 检测阶段开始标志
        if first_col.startswith("第") and first_col.endswith("节"):
            await broadcast(to_json(str(data.iloc[i]).strip()))
            i += 1
            await broadcast(to_json(str(data.iloc[i]).strip()))
            i += 1
            await broadcast(to_json(str(data.iloc[i]).strip()))

        # 检测阶段结束标志
        if next_col.startswith("第"):
            i += 1
            continue

        # 读取下一行时间差
        else:
            current_time = str(data.iloc[i][0])
            next_time = str(data.iloc[i + 1][0])
            await asyncio.sleep(diff(current_time, next_time) / 3)
            # 打印下一行内容
            await broadcast(to_json(str(data.iloc[i + 1]).strip()))
            sent_data_log.append(to_json(str(data.iloc[i + 1]).strip()))

        i += 1


async def websocket_handler(websocket):
    # 客户端连接处理
    client_address = websocket.remote_address
    print(f"新客户端尝试连接: {client_address}")

    connected_clients.add(websocket)
    print(f"客户端已连接: {client_address}")

    try:
        # 如果有历史记录，逐条发送给新连接的客户端
        for record in sent_data_log:
            await websocket.send(record)
        await websocket.wait_closed()
    except Exception as e:
        print(f"客户端 {client_address} 连接中出现错误: {e}")
    finally:
        print(f"客户端断开连接: {client_address}")
        connected_clients.remove(websocket)


async def main():
    # 启动 WebSocket 服务器
    await websockets.serve(websocket_handler, "localhost", 6789)
    # 启动数据流读取任务
    while True:
        sent_data_log.clear()
        await read_stream()


if __name__ == "__main__":
    asyncio.run(main())
