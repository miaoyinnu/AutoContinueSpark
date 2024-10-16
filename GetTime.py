from datetime import datetime

# 获取当前时间
def gettime():
    current_time = datetime.now()
    return current_time.strftime("%Y-%m-%d, %I:%M:%S %p")

# 打印当前时间
# print("当前时间是:", current_time)
