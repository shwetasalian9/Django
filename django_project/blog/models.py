from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

class Posts(models.Model) :
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now= True updates the date_posted to current time everytime the post is updated
    # auto_now_add=True will add current time when its created but not update it everytime
    #default - can chnage the date_posted whenever needed
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) :
        return self.title
