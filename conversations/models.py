from django.db import models
from core import models as core_models

class Conversation(core_models.TimeStampedModel):

    """ CONVERSATION MODEL DEFINITION """
    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)

class Message(core_models.TimeStampedModel):

    """ MESSAGE MODEL DEFINITION """

    message = models.TextField()
    user = models.ForeignKey("users.User", related_name="messages", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} says : {self.message}'