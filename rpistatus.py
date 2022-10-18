#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# cython: language_level=3

#Flag Bits
UNDERVOLTED         = '0'
CAPPED              = '1'
THROTTLED           = '2'
SOFT_TEMPLIMIT      = '3'
HAS_UNDERVOLTED     = '16'
HAS_CAPPED          = '17'
HAS_THROTTLED       = '18'
HAS_SOFT_TEMPLIMIT  = '19'

from vcgencmd import Vcgencmd
from colorama import init
from colorama import Fore, Back, Style
import time

init(autoreset=True)

vcgm = Vcgencmd()

def print_log(flag, info):
    if flag:
        print(Fore.RED + Style.BRIGHT + info, end = '  ')
    else:
        print(Fore.GREEN + Style.DIM + info, end = '  ')

while True:

    print('[{}] '.format(time.strftime('%M:%S')), end = '')

    output = vcgm.get_throttled()
    output1 =vcgm.measure_temp()

    flag = output['breakdown'][UNDERVOLTED]
    print_log(flag, '输入电压')

    flag = output['breakdown'][THROTTLED]
    print_log(flag, '工作频率')

    flag = output['breakdown'][HAS_UNDERVOLTED]
    print_log(flag, '历史电压')

    flag = output['breakdown'][HAS_THROTTLED]
    print_log(flag, '历史频率')

    print("Soc温度："+str(output1))

    print()

    time.sleep(1)

#EOF

