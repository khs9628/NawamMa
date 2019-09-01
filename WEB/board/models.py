from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField('date published')
    # 공지사항 / 자유게시판 -> I / F
    stat_choices = (('I','공지사항'), ('F','자유게시판'))
    stat = models.CharField(max_length=10, choices=stat_choices)
    hashtags = models.ManyToManyField('Hashtag', blank=True)
    image = models.ImageField(upload_to='board/image/', blank=True)
    

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:30]

class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comment(models.Model):
    Board_pk = models.ForeignKey(Board, on_delete=models.CASCADE, related_name ="comments")
    comment_text = models.CharField(max_length=50)
    c_date = models.DateTimeField('date published')

    def __str__(self):
        return self.comment_text