from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CHOIES = [
        ('Pendente', 'Pendente'),
        ('Em andamento',  'Em andamento'),
        ('Concluido', 'Concluido')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOIES, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    
    def __str__(self):
        return self.title