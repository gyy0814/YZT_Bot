import logging
import os
import signal

import subprocess
import UiFile.SIG
import re


# 去除ansi颜色代码和命令提示符>
def ansi(text: str) -> str:
    text = re.sub(r'\x1b\x5b([\x30-\x39]*\x3b)*[\x30-\x39]*\x6d', '', text)  # 正则去除颜色代码
    return text
    # return text.replace('> \r  \r', '')  # 替换命令提示符>


def run():
    try:
        result = subprocess.Popen("java -jar mcl.jar",
                                  # shell=True,
                                  cwd=os.getcwd() + "\\mcl-1.2.2",
                                  stdout=subprocess.PIPE,
                                  stdin=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)

        # result = subprocess.Popen('java -cp "libs/*" "net.mamoe.mirai.console.terminal.MiraiConsoleTerminalLoader"',
        #                           shell=True,
        #                           cwd=os.getcwd() + "\\mcl-1.2.2",
        #                           stdout=subprocess.PIPE,
        #                           stderr=subprocess.STDOUT)

        # result = subprocess.Popen('python test1.py',
        #                           # shell=True,
        #                           stdout=subprocess.PIPE,
        #                           stdin=subprocess.PIPE,
        #                           stderr=subprocess.STDOUT)
        return result
    except Exception as e:
        print(e)


class MCL:
    def __init__(self):
        self.isRun = True
        self.result = subprocess.Popen("java -jar mcl.jar",
                                       # shell=True,
                                       cwd=os.getcwd() + "\\mcl-1.2.2",
                                       stdout=subprocess.PIPE,
                                       stdin=subprocess.PIPE,
                                       stderr=subprocess.STDOUT)

        # self.result = subprocess.Popen('java -cp "libs/*" "net.mamoe.mirai.console.terminal.MiraiConsoleTerminalLoader"',
        #                           shell=True,
        #                           cwd=os.getcwd() + "\\mcl-1.2.2",
        #                           stdout=subprocess.PIPE,
        #                           stderr=subprocess.STDOUT)

        # self.result = subprocess.Popen('python test1.py',
        #                           # shell=True,
        #                           stdout=subprocess.PIPE,
        #                           stdin=subprocess.PIPE,
        #                           stderr=subprocess.STDOUT)

    def readLine(self):
        logging.debug("mcl启动")
        while self.isRun:
            rcode = self.result.poll()
            if rcode is None:
                line = self.result.stdout.readline().strip()
                UiFile.SIG.mysig.mclDebug.emit(ansi(line.decode('gbk')))
        print("mcl停止读取")

    def stop(self):
        try:
            self.isRun =False
            if self.result:
                # result.stdin.write(b'stop\r\n')
                # print('stop\r\n')
                # print(result.pid)

                self.result.send_signal(signal.CTRL_C_EVENT)
                # cmd = "taskkill /f /pid %s"%result.pid
                # os.system(cmd)
        except Exception as e:
            print(e)
