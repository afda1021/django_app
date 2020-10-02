from django.db import models

class TodoList(models.Model):
    STATE = (
        (1,'未実行'),
        (2,'実行中'),
        (3,'終了')
    )
    name = models.CharField('内容', max_length=255)
    state = models.IntegerField('状態', choices=STATE)

    def __str__(self):
        return self.name
