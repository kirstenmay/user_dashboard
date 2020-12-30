from django.db import models
from apps.login_reg.models import User

class message_manager(models.Manager):
    def new_message_validator(self, postData):
        errors = {}
        if len(postData['message_body']) > 1:
            errors['message_body'] = "Message body may not be empty"
        return errors


class Message(models.Model):
    message_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    #Message will have a creator (one to many)
    creator = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    #Message will have a recipient (many to many)
    recipient = models.ManyToManyField(User, related_name="user_messages")
    objects = message_manager()


class comment_manager(models.Manager):
    def new_comment_validator(self, postData):
        errors = {}
        if len(postData['comment_body']) > 1:
            errors['comment_body'] = "Comment body may not be empty"
        return errors


class Comment(models.Model):
    comment_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    #Comment will have a message (one to many)
    message = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    #Comment will have a creator (one to many)
    creator = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    objects = message_manager()

