import pyautogui
import time
import OpenAndCloseDouyin as oc
import schedule
from datetime import datetime
def L():
    # 假设选择框的位置为 (x, y)
    x, y = 300, 400  # 这是你获取的坐标值

    # 移动鼠标到选择框的位置
    pyautogui.moveTo(x, y)
    time.sleep(5)
    # 点击选择框（左键单击）
    pyautogui.click()

def getPosition():
    while True:
        time.sleep(1)
        print(pyautogui.position())

def scroll():
    pyautogui.scroll(-150)

def MoveAndClick(x,y,t=1):
    pyautogui.moveTo(x, y)
    time.sleep(t)
    pyautogui.click()
    time.sleep(t)
def main():
    #全屏
    MoveAndClick(2248, 128)
    #私信
    MoveAndClick(2171, 68)

    #私信下c1
    MoveAndClick(2166, 193)
    #c1
    MoveAndClick(1713, 198)


    # emoji
    MoveAndClick(2336, 991)

    # double q
    MoveAndClick(2028, 928)


    # ->
    MoveAndClick(2035, 809)


    scroll()
    # fire
    MoveAndClick(1871, 801)
def schedule_random_task():
    # 生成一个 0 到 30 分钟之间的随机秒数
    delay = random.randint(0, 1800)
    print(f"任务将在 {delay} 秒后执行")

    # 延迟执行任务
    time.sleep(delay)
    my_task()
def my_task():

    print("任务执行时间:", datetime.now())
    oc.open_douyin()
    time.sleep(3)

    main()
    time.sleep(2)

    oc.close_douyin()
    # 在这里添加你想要执行的任务代码
    print("任务执行完成")
if __name__ == '__main__':
    # getPosition()
    # time.sleep(2)
    #
    # scroll()
    # oc.open_douyin()
    # main()
    # time.sleep(2)
    #
    # oc.close_douyin()

    schedule.every().day.at("00:00").do(schedule_random_task)

    print("定时任务已启动...")

    while True:
        # 运行所有的计划任务
        schedule.run_pending()
        time.sleep(1)