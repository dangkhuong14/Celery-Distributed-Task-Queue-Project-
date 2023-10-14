import os
from celery import Celery

# Lệnh trong file manage.py vì celery container không có command to run app
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cedjango.settings')

app = Celery('cedjango')
# Gọi method này để Celery lấy config từ file settings.py trong Django project
app.config_from_object("django.conf:settings", namespace='CELERY')


@app.task
def task1():
    return


# Call this method to make Celery looking for all tasks in tasks.py in all INSTALLED_APPS
app.autodiscover_tasks()
