# -*- encoding: UTF-8 -*-

import utils
import logging
import work_flow
import settings
import schedule
import time
import datetime
from pathlib import Path

def job():
    if utils.is_weekday():
        work_flow.prepare()

# 获取当前时间并格式化文件名
current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
log_filename = f"logs/sequoia-{current_time}.log"

# 创建 logs 目录（如果不存在）
Path("logs").mkdir(parents=True, exist_ok=True)

# 配置 logging，使用格式化的文件名
logging.basicConfig(
    format='%(asctime)s %(message)s',
    filename=log_filename,
    encoding='utf-8',  # 添加编码设置，避免潜在的编码错误
    level=logging.INFO
)

settings.init()

if settings.config['cron']:
    EXEC_TIME = "15:15"
    schedule.every().day.at(EXEC_TIME).do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
else:
    work_flow.prepare()

