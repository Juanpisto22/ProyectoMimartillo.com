from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
#modelo de Intereses
class Interest(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Interés'
        verbose_name_plural = 'Intereses'
        ordering = ['name']


    def __str__(self):
        return self.name
        




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='users/image_user.png', upload_to='users/')
    location = models.CharField(max_length=80, null=True, blank=True)
    bio = models.TextField(max_length=400, null=True, blank=True)
    interest = models.ManyToManyField(Interest, verbose_name='Intereses')


    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']


# Se usan las señales de la base de datos para que en el momento de crear un usuario se creee un perfil
#para eso mismo se importo lo siguiente:
#from django.db.models.signals import post_save

#funcion que crea el usuario
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#funcion que guarda los datos del usuario
def save_user_profile(sender, instance,**kwargs):
    instance.profile.save()


#ejecuta las dos funciones enteriormente creadas, la que crea y la que guarda    
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

