from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(
        max_length=32,
        verbose_name="Title",
        help_text="Title of Post",
    )

    body = models.TextField(
        verbose_name="Body Content",
    )

    created_at = models.DateTimeField(
        verbose_name="Publish Datetime",
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.id}- {self.title}"

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name="Post",
        related_name="comments",
    )

    text = models.TextField(
        verbose_name="Text Comment"
    )

    created_at = models.DateTimeField(
        verbose_name="Write Time",
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.id}- {self.text}"
