from django.db import models

from login_app.models import Universe


# Create your models here.
class Glossary(models.Model):

    wordEn = models.CharField(max_length=200, verbose_name='Palabra inglés')
    wordEs = models.CharField(max_length=200, null=True, blank=True, verbose_name='Palabra español')
    universe = models.ForeignKey(Universe, models.DO_NOTHING, null=True, blank=True, related_name='glossary_universe',
                                 verbose_name='Universo')
    urlEn = models.URLField(max_length=2000, null=True, blank=True, verbose_name='Enlace Coppermind en inglés')
    urlEs = models.URLField(max_length=2000, null=True, blank=True, verbose_name='Enlace Coppermind en español')

    def __str__(self):
        return str(self.wordEs)

    def get_absolute_url(self):
        return reverse('wordEs', args=[str(self.id)])

    class Meta:
        verbose_name = 'Glosario'
        verbose_name_plural = 'Glosario'