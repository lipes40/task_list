from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CHOIES = [
        ('P', 'Pendente'),
        ('A',  'Em andamento'),
        ('C', 'Concluido')
    ]

    numero = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOIES, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.numero:  # só define se ainda não tiver número
            ultimo = Task.objects.order_by('-numero').first()
            self.numero = (ultimo.numero + 1) if ultimo else 1
        super().save(*args, **kwargs)