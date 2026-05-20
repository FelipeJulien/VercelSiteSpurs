#!/usr/bin/env python
"""Script para adicionar eventos históricos dos Spurs"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spurs_site.settings')
django.setup()

from core.models import HistoryEvent

# Lista de eventos históricos do San Antonio Spurs
history_events = [
    {
        'year': 1973,
        'title': 'Fundação da Franquia',
        'description': 'Os San Antonio Spurs são fundados como parte da ABA (American Basketball Association).',
        'order': 1
    },
    {
        'year': 1976,
        'title': 'Entrada na NBA',
        'description': 'Os Spurs ingressam na NBA após a fusão entre ABA e NBA.',
        'order': 2
    },
    {
        'year': 1985,
        'title': 'Seleção de David Robinson',
        'description': 'O Spurs seleciona David Robinson no draft de 1987, o que marcaria o início de uma era de domínio.',
        'order': 3
    },
    {
        'year': 1989,
        'title': 'Chegada de Tim Duncan',
        'description': 'Com a primeira escolha do draft de 1997, Tim Duncan chega aos Spurs, formando a dupla que dominaria a NBA.',
        'order': 4
    },
    {
        'year': 1999,
        'title': '1º Título da NBA',
        'description': 'Os Spurs conquistam seu primeiro campeonato da NBA, derrotando o New York Knicks nas Finals.',
        'order': 5
    },
    {
        'year': 2003,
        'title': '2º Título da NBA',
        'description': 'O segundo título vem com a vitória na Finals sobre o New Jersey Nets, consolidando o começo de uma dinastia.',
        'order': 6
    },
    {
        'year': 2005,
        'title': '3º Título da NBA',
        'description': 'Os Spurs conquistam seu terceiro campeonato, novamente com vitória na Finals.',
        'order': 7
    },
    {
        'year': 2007,
        'title': '4º Título da NBA',
        'description': 'Mais um título é conquistado, com performances memoráveis nas Finals contra o Cleveland Cavaliers.',
        'order': 8
    },
    {
        'year': 2014,
        'title': '5º Título da NBA',
        'description': 'O quinto e último título, conquistado com o famoso basquete de movimento e Tony Parker em destaque.',
        'order': 9
    },
    {
        'year': 2015,
        'title': 'Reforma da Franquia',
        'description': 'Após a aposentadoria de Tim Duncan, os Spurs iniciam um período de transição e renovação.',
        'order': 10
    },
    {
        'year': 2019,
        'title': 'Abertura do AT&T Center',
        'description': 'Os Spurs começam a jogar no AT&T Center (agora Frost Bank Center), sua casa moderna e de classe mundial.',
        'order': 11
    },
    {
        'year': 2023,
        'title': 'Nomeação de Mitch Johnson',
        'description': 'Mitch Johnson é nomeado técnico dos Spurs, iniciando uma nova era com foco no desenvolvimento de talentos.',
        'order': 12
    },
    {
        'year': 2024,
        'title': 'Seleção de Victor Wembanyama',
        'description': 'Com a primeira escolha do draft de 2023, os Spurs selecionam Victor Wembanyama, um talento geracional.',
        'order': 13
    },
    {
        'year': 2025,
        'title': 'Aquisição de De\'Aaron Fox',
        'description': 'Os Spurs adquirem De\'Aaron Fox em uma troca com o Sacramento Kings, criando um backcourt dinâmico.',
        'order': 14
    },
    {
        'year': 2026,
        'title': 'Renovação e Esperança',
        'description': 'A temporada 2025-26 marca o início de um novo capítulo com jovens talentos e veteranos experientes.',
        'order': 15
    },
]

# Adicionar os eventos
created_count = 0
for event_data in history_events:
    event, created = HistoryEvent.objects.get_or_create(
        year=event_data['year'],
        order=event_data['order'],
        defaults={
            'title': event_data['title'],
            'description': event_data['description']
        }
    )
    if created:
        created_count += 1
        print(f"✓ Criado: {event_data['year']} - {event_data['title']}")
    else:
        print(f"✗ Já existe: {event_data['year']} - {event_data['title']}")

print(f"\n✅ Total de eventos históricos adicionados: {created_count}")
