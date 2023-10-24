import os
from celery import Celery

# Lệnh trong file manage.py vì celery container không có command to run app ma dung khai bao
# ben duoi de Celery worker Django project nhan biet file settings cua Django o vi tri nao
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cedjango.settings')

app = Celery('cedjango')
# Gọi method này để Celery lấy config từ file settings.py trong Django project
app.config_from_object("django.conf:settings", namespace='CELERY')


@app.task
def task1():
    return


# Call this method to make Celery looking for all tasks in tasks.py in all INSTALLED_APPS
app.autodiscover_tasks()
