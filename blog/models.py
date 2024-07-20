from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', _('Published')),
        ('drf', _('Draft')),
    )

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('Author'))
    title = models.CharField(max_length=250, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    cover = models.ImageField(upload_to='covers/', blank=True, verbose_name=_('Cover'))
    status = models.CharField(choices=STATUS_CHOICES, max_length=3, default=STATUS_CHOICES[0][0],
                              verbose_name=_('Status'))
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('DateTimeCreated'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('DateTimeModified'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('User'))
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, verbose_name=_('Post'))
    text = models.TextField(verbose_name=_('Text'))
    helpful = models.BooleanField(default=True, verbose_name=_('Post Was helpful?'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is_active'))
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('DateTimeCreated'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('DateTimeModified'))

    def __str__(self):
        return f"{self.user}: {self.text}"
