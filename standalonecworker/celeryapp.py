from celery import Celery

app = Celery('StandaloneWorker')
app.config_from_object('celeryconfig')


@app.task
def say_hello():
    return print('Hello! This is hello from standalone celery worker!')
