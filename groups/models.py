from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django import template
import misaka


User = get_user_model()

register = template.Library()


class Group(models.Model):
    pass


class GroupMember(models.Model):
    pass
