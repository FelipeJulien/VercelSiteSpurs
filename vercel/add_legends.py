#!/usr/bin/env python
"""Script para adicionar lendas do San Antonio Spurs"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spurs_site.settings')
django.setup()

from core.models import Player

# Lista de lendas do San Antonio Spurs com seus dados
legends_data = [
    {
        'name': 'Tim Duncan',
        'number': 21,
        'position': 'PF/C',
        'position_full': 'Power Forward/Center',
        'height': "6'11\"",
        'experience': '19',
        'is_legend': True,
        'legend_years': '1997-2016',
        'legend_achievements': '5 títulos da NBA, 15 All-Star, 2 MVPs da temporada, 3 MVPs das Finals',
        'photo_url': 'https://cdn.nba.com/headshots/nba/latest/1040x760/2544.png'
    },
    {
        'name': 'David Robinson',
        'number': 50,
        'position': 'C',
        'position_full': 'Center',
        'height': "7'1\"",
        'experience': '14',
        'is_legend': True,
        'legend_years': '1989-2003',
        'legend_achievements': '2 títulos da NBA, 10 All-Star, 1 MVP da temporada, Hall of Fame',
        'photo_url': 'https://cdn.nba.com/headshots/nba/latest/1040x760/2545.png'
    },
    {
        'name': 'Tony Parker',
        'number': 9,
        'position': 'PG',
        'position_full': 'Point Guard',
        'height': "6'2\"",
        'experience': '18',
        'is_legend': True,
        'legend_years': '2001-2018',
        'legend_achievements': '4 títulos da NBA, 6 All-Star, 3 MVPs das Finals, Hall of Fame',
        'photo_url': 'https://cdn.nba.com/headshots/nba/latest/1040x760/2338.png'
    },
    {
        'name': 'Manu Ginóbili',
        'number': 20,
        'position': 'SG/SF',
        'position_full': 'Shooting Guard/Small Forward',
        'height': "6'6\"",
        'experience': '16',
        'is_legend': True,
        'legend_years': '2002-2018',
        'legend_achievements': '4 títulos da NBA, 2 All-Star, 1 MVP das Finals, Hall of Fame',
        'photo_url': 'https://cdn.nba.com/headshots/nba/latest/1040x760/2202.png'
    },
    {
        'name': 'Avery Johnson',
        'number': 6,
        'position': 'PG',
        'position_full': 'Point Guard',
        'height': "6'2\"",
        'experience': '16',
        'is_legend': True,
        'legend_years': '1994-2001',
        'legend_achievements': 'Campeão da NBA 1999, "O Homem que Ganhou o Jogo"',
        'photo_url': 'https://cdn.nba.com/headshots/nba/latest/1040x760/2549.png'
    },
]

# Adicionar as lendas
created_count = 0
for legend_data in legends_data:
    # Procurar se já existe
    try:
        player = Player.objects.get(name=legend_data['name'])
        # Atualizar se já existe
        player.is_legend = legend_data['is_legend']
        player.legend_years = legend_data['legend_years']
        player.legend_achievements = legend_data['legend_achievements']
        player.photo_url = legend_data['photo_url']
        player.save()
        print(f"✓ Atualizado: {legend_data['name']} (Lenda)")
    except Player.DoesNotExist:
        # Criar se não existe
        player = Player.objects.create(
            name=legend_data['name'],
            number=legend_data['number'],
            position=legend_data['position'],
            position_full=legend_data['position_full'],
            height=legend_data['height'],
            experience=legend_data['experience'],
            is_legend=legend_data['is_legend'],
            legend_years=legend_data['legend_years'],
            legend_achievements=legend_data['legend_achievements'],
            photo_url=legend_data['photo_url'],
            is_active=False  # Lendas não estão no elenco ativo
        )
        created_count += 1
        print(f"✓ Criado: {legend_data['name']} (Lenda)")

print(f"\n✅ Total de lendas adicionadas: {created_count}")
print(f"✅ Todas as lendas foram marcadas como 'Lenda do Clube'")
