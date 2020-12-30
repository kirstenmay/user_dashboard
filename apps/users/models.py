from django.db import models

class message_manager(models.Manager):
    def new_message_validator(self, postData):
        errors = {}
        return errors


class Message(models.Model):
    message_body = models.CharField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = message_manager()


class comment_manager(models.Manager):
    def new_comment_validator(self, postData):
        errors = {}
        return errors


class Comment(models.Model):
    comment_body = models.CharField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = message_manager()

