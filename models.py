# Import necessary Django model and user authentication model
from django.db import models
from django.contrib.auth.models import User

# Define the Post model
class Post(models.Model):
    # Each post has a title, which is a character field with a maximum length of 200
    title = models.CharField(max_length=200)
    
    # Each post has content, which is a text field that can contain an unlimited number of characters
    content = models.TextField()
    
    # Each post is authored by a user. ForeignKey creates a many-to-one relationship.
    # This means that each user can author many posts. When a User is deleted, all associated Posts are also deleted (models.CASCADE).
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Each post can have multiple tags. Here it is just a character field, so tags need to be processed before saving (e.g., split by commas)
    tags = models.CharField(max_length=200)

# Define the Comment model
class Comment(models.Model):
    # Each comment has content, which is a text field that can contain an unlimited number of characters
    content = models.TextField()
    
    # Each comment is authored by a user. ForeignKey creates a many-to-one relationship.
    # This means that each user can author many comments. When a User is deleted, all associated Comments are also deleted (models.CASCADE).
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Each comment is associated with a post. ForeignKey creates a many-to-one relationship.
    # This means that each post can have many comments. When a Post is deleted, all associated Comments are also deleted (models.CASCADE).
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
