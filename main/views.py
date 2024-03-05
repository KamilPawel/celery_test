from main.tasks import index_task
from django.http import JsonResponse


def index(request):
    index_task.delay()
    return JsonResponse(
        {"message": "Created a task!"},
    )
