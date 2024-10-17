import pyautogui
import time
import OpenAndCloseDouyin as oc
import schedule
import random
from datetime import datetime

from GetTime import get_time


def get_position():
    while True:
        time.sleep(1)
        print(pyautogui.position())

def down_scroll():
    pyautogui.scroll(-150)

def move_and_click(x,y,t=1):
    pyautogui.moveTo(x, y)
    time.sleep(t)
    pyautogui.click()
    time.sleep(t)

def main():
    #全屏
    move_and_click(2248, 128,3)
    #私信
    move_and_click(2171, 68)

    #私信下c1
    move_and_click(2166, 193)
    #c1
    move_and_click(1713, 198)


    # emoji
    move_and_click(2351, 1001)

    # double q
    move_and_click(2028, 928)


    # ->
    move_and_click(2035, 809)

    down_scroll()
    # fire
    move_and_click(1871, 801)
def schedule_random_task():
    # 生成一个 0 到 30 分钟之间的随机秒数
    # delay = random.randint(0, 1800)
    delay = random.randint(1, 3)

    print(f"任务将在 {delay} 秒后执行")

    # 延迟执行任务
    time.sleep(delay)
    my_task()
def my_task():

    print("任务执行时间:", get_time())
    oc.open_douyin()
    time.sleep(3)

    main()
    time.sleep(2)

    oc.close_douyin()
    # 在这里添加你想要执行的任务代码
    print("任务执行完成")
if __name__ == '__main__':
    # getPosition()
    #
    # scroll()
    # oc.open_douyin()
    # main()
    # oc.close_douyin()

    time0 = '00:00'
    time1 = '23:32'
    schedule.every().day.at(time1).do(schedule_random_task)

    print("定时任务已启动...")

    while True:
        # 运行所有的计划任务
        schedule.run_pending()
        time.sleep(1)