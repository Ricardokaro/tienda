from django.contrib.auth import get_user_model
import time

from config import celery_app

User = get_user_model()

@celery_app.task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    for i in range(30):
        time.sleep(1)
        print("Sleeping", str(i + 1))
    return User.objects.count()



