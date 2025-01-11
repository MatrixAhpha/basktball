import json
import pandas as pd
import asyncio
import websockets
import sys

connected_clients = set()
sent_data_log = []


def diff(time1, time2):
    try:
        minutes1, seconds1, microseconds1 = map(int, time1.split(":"))
        minutes2, seconds2, microseconds2 = map(int, time2.split(":"))
        total_seconds1 = minutes1 * 60 + seconds1
        total_seconds2 = minutes2 * 60 + seconds2
        return abs(total_seconds1 - total_seconds2)
    except ValueError:
        raise ValueError("时间格式不正确，请确保格式为 MM:SS:000000")


def to_json(raw_data):
    lines = raw_data.strip().split('\n')
    data_dict = {}
    for line in lines:
        parts = line.split(maxsplit=1)
        if len(parts) == 2:
            key, value = parts
        else:
            key, value = parts[0], None
        if len(data_dict) == 0 and value and ':' in value:
            time_parts = value.split(':')
            if len(time_parts) == 3:
                value = ':'.join(time_parts[:2])
        data_dict[key] = value
    limited_dict = dict(list(data_dict.items())[:4])
    json_data = json.dumps(limited_dict, ensure_ascii=False, indent=4)
    sent_data_log.append(json_data)
    return json_data


async def broadcast(data_send):
    if connected_clients:
        await asyncio.gather(*(client.send(data_send) for client in connected_clients))


async def read_stream(file_path):
    data = pd.read_excel(file_path, header=None)
    i = 0
    while i + 1 < len(data):
        current_row = data.iloc[i]
        next_row = data.iloc[i + 1]

        first_col = str(current_row[0]).strip()
        next_col = str(next_row[0]).strip()

        if first_col.startswith("第") and first_col.endswith("节"):
            await broadcast(to_json(str(data.iloc[i]).strip()))
            i += 1
            await broadcast(to_json(str(data.iloc[i]).strip()))
            i += 1
            await broadcast(to_json(str(data.iloc[i]).strip()))

        if next_col.startswith("第"):
            i += 1
            continue

        else:
            current_time = str(data.iloc[i][0])
            next_time = str(data.iloc[i + 1][0])
            await asyncio.sleep(diff(current_time, next_time) / 2)
            await broadcast(to_json(str(data.iloc[i + 1]).strip()))

        i += 1


async def websocket_handler(websocket):
    client_address = websocket.remote_address
    print(f"新客户端尝试连接: {client_address}")

    connected_clients.add(websocket)
    print(f"客户端已连接: {client_address}")

    try:
        for record in sent_data_log:
            await websocket.send(record)
        await websocket.wait_closed()
    except Exception as e:
        print(f"客户端 {client_address} 连接中出现错误: {e}")
    finally:
        print(f"客户端断开连接: {client_address}")
        connected_clients.remove(websocket)


async def main():
    if len(sys.argv) != 3:
        print("用法: python script.py <文件名> <端口号>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        port = int(sys.argv[2])
    except ValueError:
        print("端口号必须为整数")
        sys.exit(1)

    print(f"启动 WebSocket 服务器，文件: {file_path}，端口: {port}")

    server = await websockets.serve(websocket_handler, "localhost", port)
    try:
        while True:
            sent_data_log.clear()
            await read_stream(file_path)
    except KeyboardInterrupt:
        print("服务器已停止")
    finally:
        server.close()
        await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
