from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Player(models.Model):
    """Modelo representando um jogador do San Antonio Spurs."""

    POSITION_CHOICES = [
        ('PG', 'Point Guard'),
        ('SG', 'Shooting Guard'),
        ('SF', 'Small Forward'),
        ('PF', 'Power Forward'),
        ('C', 'Center'),
        ('PF/C', 'Power Forward/Center'),
        ('SG/SF', 'Shooting Guard/Small Forward'),
    ]

    name = models.CharField('Nome', max_length=100)
    number = models.PositiveIntegerField('Número da Camisa')
    position = models.CharField('Posição (sigla)', max_length=5, choices=POSITION_CHOICES)
    position_full = models.CharField('Posição (completa)', max_length=50)
    height = models.CharField('Altura', max_length=10)
    experience = models.CharField('Experiência', max_length=20)
    photo = models.ImageField('Foto (upload)', upload_to='players/', blank=True, null=True)
    photo_url = models.URLField('Foto (URL externa)', blank=True, null=True)
    is_active = models.BooleanField('Ativo no Elenco', default=True)
    is_legend = models.BooleanField('Lenda do Clube', default=False)
    legend_years = models.CharField('Período (lendas)', max_length=20, blank=True, null=True,
                                     help_text='Ex: 1997-2016')
    legend_achievements = models.CharField('Conquistas (lendas)', max_length=200, blank=True, null=True,
                                            help_text='Ex: 19 temporadas, 5 títulos, 2 MVPs')
    created_at = models.DateTimeField('Criado em', default=timezone.now)

    class Meta:
        ordering = ['number']
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'

    def __str__(self):
        return f'#{self.number} {self.name}'

    @property
    def photo_src(self):
        """Retorna a URL da foto: prioriza upload, senão usa URL externa."""
        if self.photo:
            return self.photo.url
        return self.photo_url or ''


class Championship(models.Model):
    """Modelo representando um título da NBA conquistado pelos Spurs."""

    year = models.PositiveIntegerField('Ano', unique=True)
    description = models.CharField('Descrição', max_length=100)

    class Meta:
        ordering = ['year']
        verbose_name = 'Título'
        verbose_name_plural = 'Títulos'

    def __str__(self):
        return f'NBA {self.year}'


class HistoryEvent(models.Model):
    """Modelo representando um evento na linha do tempo da história dos Spurs."""

    year = models.PositiveIntegerField('Ano')
    title = models.CharField('Título', max_length=100)
    description = models.TextField('Descrição')
    order = models.PositiveIntegerField('Ordem na Timeline', unique=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Evento Histórico'
        verbose_name_plural = 'Eventos Históricos'

    def __str__(self):
        return f'{self.year} - {self.title}'



