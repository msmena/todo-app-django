from django.utils import timezone

from django.db import models
from django.urls import reverse


def una_semana_despues():
    return timezone.now() + timezone.timedelta(days=7)


class ToDoList(models.Model):
    titulo = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('list', args=[self.id])

    def __str__(self):
        return self.titulo


class ToDoItem(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_caducidad = models.DateTimeField(default=una_semana_despues)
    todo_lista = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('item-update', args=[str(self.todo_list.id), str(self.id)])

    def __str__(self):
        return f"{self.titulo}: caducidad {self.fecha_caducidad}"

    class Meta:
        ordering = ['fecha_caducidad']
