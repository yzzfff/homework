# -*- coding: utf-8 -*-
import time

class ElectronicLock:
    def __init__(self, password):
        self.password = password
        self.is_locked = True
        self.attempts_left = 3
        self.locked_time = None
        self.is_door_open = False
        self.is_alarm_on = False
        self.is_guest_mode = False
        self.access_logs = []

    def enter_password(self):
        while self.attempts_left > 0:
            if self.is_locked:
                if self.locked_time is not None:
                    time_diff = time.time() - self.locked_time
                    if time_diff < 10:
                        print(f"请等待 {int(10 - time_diff)} 秒后再尝试输入密码")
                        return
                    else:
                        self.is_locked = False
                        self.locked_time = None
                        self.attempts_left = 3

                user_password = input("请输入密码: ")
                if user_password == self.password:
                    print("密码正确，门已解锁！")
                    self.is_locked = False
                    self.attempts_left = 3
                    self.access_logs.append((time.strftime("%Y-%m-%d %H:%M:%S"), "密码解锁"))
                    break
                else:
                    self.attempts_left -= 1
                    print(f"密码错误，还剩 {self.attempts_left} 次尝试机会")
                    if self.attempts_left == 0:
                        print("尝试次数超过限制，锁定门10秒")
                        self.is_locked = True
                        self.locked_time = time.time()
                        self.access_logs.append((time.strftime("%Y-%m-%d %H:%M:%S"), "密码锁定"))
            else:
                print("门已解锁")
                break

    def open_door(self):
        if not self.is_locked:
            if not self.is_door_open:
                print("门已打开")
                self.is_door_open = True
                self.access_logs.append((time.strftime("%Y-%m-%d %H:%M:%S"), "门打开"))
            else:
                print("门已经是打开状态")
        else:
            print("门已锁定，无法打开")

    def close_door(self):
        if self.is_door_open:
            print("门已关闭")
            self.is_door_open = False
            self.access_logs.append((time.strftime("%Y-%m-%d %H:%M:%S"), "门关闭"))
        else:
            print("门已经是关闭状态")

    def toggle_alarm(self):
        if self.is_alarm_on:
            print("警报已关闭")
            self.is_alarm_on = False
            self.access_logs.append((time.strftime("%Y-%m-%d %H:%M:%S"), "警报关闭"))
        else:
            print("警报已开启")
            self.is_alarm_on = True
            self.access_logs.append((time.strftime("%Y-%m-%d %H:%M:%S"), "警报开启"))

    def toggle_guest_mode(self):
        if self.is_guest_mode:
            print("访客模式已关闭")
            self.is_guest_mode = False
            self.access_logs.append((time.strftime("%Y-%m-%d %H:%M:%S"), "访客模式关闭"))
        else:
            print("访客模
式)