from celery import Task
from celery.exceptions import SoftTimeLimitExceeded
import traceback

class MyTask1(Task):

    name = 'celery_demo2.mytask1.MyTask1'
    soft_time_limit = 10

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))

    def run(self):
        try:
            print(self.request.id)
        except SoftTimeLimitExceeded:
            print(traceback.format_exc())
            raise
        except Exception:
            print(traceback.format_exc())
            return False
        return True
