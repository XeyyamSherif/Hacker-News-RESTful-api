from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.utils.log import get_task_logger
from .models import Post


logger = get_task_logger(__name__)


@shared_task
def add():
    all_post = Post.objects.all()
    all_post.update(upvote=0)
    logger.info("Upvotes  has been reset ")
