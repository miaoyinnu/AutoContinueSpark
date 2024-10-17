from datetime import datetime

# 获取当前时间
def get_time():
    current_time = datetime.now()
    return current_time.strftime("%Y-%m-%d, %I:%M:%S %p")

