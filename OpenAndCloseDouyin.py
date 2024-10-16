import os
import GetTime
def open_douyin():
    # 抖音客户端的安装路径 (请根据实际情况修改)
    douyin_path = r"C:\Program Files\ByteDance\douyin\x64\4.5.202\douyin.exe"

    # 检查路径是否存在
    if not os.path.exists(douyin_path):
        print("抖音路径无效，请检查安装路径。")
        return

    # 打开抖音客户端
    os.startfile(douyin_path)
    print(fr"抖音客户端已启动。{GetTime.gettime()}")

def close_douyin():
    # 假设抖音客户端的进程名称为 "Douyin.exe" (根据实际情况修改)
    process_name = "douyin.exe"

    # 使用 taskkill 命令关闭抖音进程
    command = f"taskkill /F /IM {process_name}"
    os.system(command)
    print("抖音客户端已关闭。")
