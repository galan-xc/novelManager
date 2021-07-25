import asyncio
import datetime

from apscheduler.events import EVENT_JOB_EXECUTED
from apscheduler.executors.asyncio import AsyncIOExecutor
from apscheduler.jobstores.redis import RedisJobStore  # 需要安装redis
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger

default_redis_jobstore = RedisJobStore(
    db=2,
    jobs_key="apschedulers.default_jobs",
    run_times_key="apschedulers.default_run_times",
    host="127.0.0.1",
    port=6379,
    password="1690036618"
)

default_executor = AsyncIOExecutor()

init_scheduler_options = {
    "jobstores": {
        # first 为 jobstore的名字，在创建Job时直接直接此名字即可
        "spider": default_redis_jobstore
    },
    "executors": {
        # first 为 executor 的名字，在创建Job时直接直接此名字，执行时则会使用此executor执行
        "spider": default_executor
    },
    # 创建job时的默认参数
    "job_defaults": {
        'coalesce': True,  # 是否合并执行
        'max_instances': 3  # 最大实例数
    }
}

# 创建scheduler
scheduler = AsyncIOScheduler(**init_scheduler_options)

# 启动调度
scheduler.start()
if __name__ == "__main__":
    print("启动: {}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    asyncio.get_event_loop().run_forever()