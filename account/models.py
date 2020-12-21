from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


# The example for corresponding field in "post" object:
# django.contrib.auth.models.User.objects.get(username='whisper')
# I.e. the field type - django.contrib.auth.models.User
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).\
                 get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,    #model of the Django authentication system
                               on_delete=models.CASCADE,
                               related_name='bookmark_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.


class TreeComment(MPTTModel):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='tree_comments')
    parent = TreeForeignKey('self', 
                            on_delete=models.CASCADE, 
                            null=True, 
                            blank=True, 
                            related_name='children')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'