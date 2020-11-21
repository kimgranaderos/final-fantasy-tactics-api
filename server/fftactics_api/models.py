from django.db import models


class Job(models.Model):
    class_name = models.CharField(max_length=20, unique=True)
    # picture male
    # picture female
    move_rate = models.PositiveSmallIntegerField(default=0)
    jump_rate = models.PositiveSmallIntegerField(default=0)
    speed = models.PositiveSmallIntegerField(default=0)
    physical_evasion_rate = models.PositiveSmallIntegerField(default=0)

    SCOPE = [
        ('high', 'High'),
        ('average', 'Average'),
        ('medium', 'Medium'),
        ('low', 'Low'),
        ('very low', 'Very Low')
    ]

    base_attack = models.CharField(max_length=10, choices=SCOPE, default='low')
    base_magic = models.CharField(max_length=10, choices=SCOPE, default='low')
    base_hp = models.CharField(max_length=10, choices=SCOPE, default='low')
    base_mp = models.CharField(max_length=10, choices=SCOPE, default='low')

    def __str__(self):
        return f"{self.class_name}'s info"
