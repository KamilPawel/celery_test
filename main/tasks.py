from celery import shared_task
from time import sleep, asctime
import logging
from django.contrib.auth.models import User
from random import randint


@shared_task
def index_task():
    logging.info("starting a task...")
    counter = 0
    logging.info(f"{counter:.2f}%")
    for i in range(5):
        sleep(1)
        counter += 20
        logging.info(f"{counter:.2f}%")
    with open("file.txt", "w") as file:
        file.write(asctime())
    user, created = User.objects.get_or_create(username="help")
    if not created:
        User.objects.filter(username="help").update(
            first_name=str(randint(0, 2930284930))
        )
    logging.info(user)
    logging.info("task finished!!!")
