from django.db import models


class Job(models.Model):
    class_Name = models.CharField(max_length=20, unique=True)
    # picture male
    # picture female
    move_Rate = models.PositiveSmallIntegerField(default=0)
    jump_Rate = models.PositiveSmallIntegerField(default=0)
    speed = models.PositiveSmallIntegerField(default=0)
    physical_Evasion_Rate = models.PositiveSmallIntegerField(default=0)

    SCOPE = [
        ('high', 'High'),
        ('average', 'Average'),
        ('medium', 'Medium'),
        ('low', 'Low'),
        ('very low', 'Very Low')
    ]

    base_Attack = models.CharField(max_length=10, choices=SCOPE, default='low')
    base_Magic = models.CharField(max_length=10, choices=SCOPE, default='low')
    base_HP = models.CharField(max_length=10, choices=SCOPE, default='low')
    base_MP = models.CharField(max_length=10, choices=SCOPE, default='low')

    def __str__(self):
        return f"{self.class_Name}'s info"
