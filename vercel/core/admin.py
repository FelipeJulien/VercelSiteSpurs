from django.contrib import admin
from .models import Player, Championship, HistoryEvent


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'position', 'height', 'experience', 'is_active', 'is_legend')
    list_filter = ('position', 'is_active', 'is_legend')
    search_fields = ('name',)
    list_editable = ('is_active', 'is_legend')
    list_per_page = 20

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'number', 'position', 'position_full', 'height', 'experience')
        }),
        ('Foto', {
            'fields': ('photo', 'photo_url'),
            'description': 'Faça upload de uma foto OU insira uma URL externa. O upload tem prioridade.'
        }),
        ('Status', {
            'fields': ('is_active', 'is_legend')
        }),
        ('Dados de Lenda', {
            'fields': ('legend_years', 'legend_achievements'),
            'classes': ('collapse',),
            'description': 'Preencha apenas para jogadores marcados como "Lenda do Clube".'
        }),
    )


@admin.register(Championship)
class ChampionshipAdmin(admin.ModelAdmin):
    list_display = ('year', 'description')
    ordering = ('year',)


@admin.register(HistoryEvent)
class HistoryEventAdmin(admin.ModelAdmin):
    list_display = ('order', 'year', 'title')
    list_display_links = ('title',)
    ordering = ('order',)

