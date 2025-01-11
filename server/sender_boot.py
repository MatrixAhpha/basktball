import subprocess
import os
import time

# 定义要启动的 sender.py 脚本及其参数
scripts = [
    ("server/sender.py", "server/event_stream1.xlsx", "6789"),
    ("server/sender.py", "server/event_stream2.xlsx", "6790")
]

processes = []

try:
    for index, (script, file_name, port) in enumerate(scripts):
        # 构建命令行参数
        cmd = ["python", script, file_name, port]
        print(f"启动脚本: {cmd}")

        # 启动子进程
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        processes.append(process)

        # 如果是第一个脚本，启动后等待10秒
        if index == 0:
            time.sleep(10)

    # 等待所有子进程完成
    for process in processes:
        stdout, stderr = process.communicate()
        if stdout:
            print(stdout.decode())
        if stderr:
            print(stderr.decode())
except KeyboardInterrupt:
    print("检测到键盘中断，正在终止子进程...")
    for process in processes:
        process.terminate()
    print("所有子进程已终止。")
except Exception as e:
    print(f"发生错误: {e}")
