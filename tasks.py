import os
from celery import Celery
import requests

app = Celery('tasks', broker=os.getenv("CELERY_BROKER_URL"))

endpoint = os.getenv("WEBHOOK_URL")


@app.task
def add(request):
    res = requests.post(endpoint, request, headers={"Content-Type": "application/json"}) 
    return res.json()
