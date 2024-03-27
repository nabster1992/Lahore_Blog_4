from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
    # Just like with common Python classes, you can add a .__str()__ method to model classes to provide a better string representation of your objects. For categories, you want to display the name. For posts, you want the title. For comments, show the name of the commenter and the post that they’re commenting on.

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    # for categories, you use another relational field, the ForeignKey field. This is similar to the ManyToManyField but instead defines a many-to-one relationship. The reasoning behind this is that many comments can be assigned to one post. But you can’t have a comment that corresponds to many posts.
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    class Meta:
        ordering = ['-date_added']

    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f"{self.name} on '{self.post}'"
