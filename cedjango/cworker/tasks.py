from celery import shared_task


@shared_task
def this_task_is_auto_found_by_celery():
    return
