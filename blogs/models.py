from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_body = models.TextField()

    def __str__(self):
        return self.blog_title
    




class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment
    



