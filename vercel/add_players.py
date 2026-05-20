#!/usr/bin/env python
"""Script para adicionar todos os jogadores do roster do Spurs"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spurs_site.settings')
django.setup()

from core.models import Player

# Lista de todos os jogadores do roster 2025-26 do San Antonio Spurs
players_data = [
    {
        'name': 'Victor Wembanyama',
        'number': 1,
        'position': 'PF/C',
        'position_full': 'Forward-Center',
        'height': "7'4\"",
        'experience': '2'
    },
    {
        'name': 'De\'Aaron Fox',
        'number': 4,
        'position': 'PG',
        'position_full': 'Point Guard',
        'height': "6'3\"",
        'experience': '8'
    },
    {
        'name': 'Stephon Castle',
        'number': 5,
        'position': 'PG',
        'position_full': 'Point Guard',
        'height': "6'6\"",
        'experience': '1'
    },
    {
        'name': 'Dylan Harper',
        'number': 2,
        'position': 'PG',
        'position_full': 'Point Guard',
        'height': "6'5\"",
        'experience': 'R'
    },
    {
        'name': 'Devin Vassell',
        'number': 24,
        'position': 'SG/SF',
        'position_full': 'Guard-Forward',
        'height': "6'5\"",
        'experience': '5'
    },
    {
        'name': 'Julian Champagnie',
        'number': 30,
        'position': 'SF',
        'position_full': 'Small Forward',
        'height': "6'7\"",
        'experience': '3'
    },
    {
        'name': 'Keldon Johnson',
        'number': 3,
        'position': 'SF',
        'position_full': 'Small Forward',
        'height': "6'6\"",
        'experience': '6'
    },
    {
        'name': 'Harrison Barnes',
        'number': 40,
        'position': 'SF',
        'position_full': 'Small Forward',
        'height': "6'7\"",
        'experience': '13'
    },
    {
        'name': 'Carter Bryant',
        'number': 11,
        'position': 'SF',
        'position_full': 'Small Forward',
        'height': "6'6\"",
        'experience': 'R'
    },
    {
        'name': 'Luke Kornet',
        'number': 7,
        'position': 'PF/C',
        'position_full': 'Power Forward/Center',
        'height': "7'1\"",
        'experience': '8'
    },
    {
        'name': 'Kelly Olynyk',
        'number': 8,
        'position': 'PF/C',
        'position_full': 'Power Forward/Center',
        'height': "7'0\"",
        'experience': '12'
    },
    {
        'name': 'Mason Plumlee',
        'number': 45,
        'position': 'PF/C',
        'position_full': 'Power Forward/Center',
        'height': "7'0\"",
        'experience': '12'
    },
    {
        'name': 'Bismack Biyombo',
        'number': 18,
        'position': 'C',
        'position_full': 'Center',
        'height': "6'8\"",
        'experience': '14'
    },
    {
        'name': 'Jordan McLaughlin',
        'number': 0,
        'position': 'PG',
        'position_full': 'Point Guard',
        'height': "5'11\"",
        'experience': '6'
    },
    {
        'name': 'David Jones Garcia',
        'number': 25,
        'position': 'PG',
        'position_full': 'Point Guard',
        'height': "6'4\"",
        'experience': 'R'
    },
    {
        'name': 'Emanuel Miller',
        'number': 14,
        'position': 'SF',
        'position_full': 'Small Forward',
        'height': "6'5\"",
        'experience': '1'
    },
    {
        'name': 'Lindy Waters III',
        'number': 43,
        'position': 'SF',
        'position_full': 'Small Forward',
        'height': "6'5\"",
        'experience': '4'
    },
    {
        'name': 'Harrison Ingram',
        'number': 55,
        'position': 'SF',
        'position_full': 'Small Forward',
        'height': "6'5\"",
        'experience': '1'
    },
]

# Adicionar os jogadores
created_count = 0
for player_data in players_data:
    player, created = Player.objects.get_or_create(
        name=player_data['name'],
        defaults={
            'number': player_data['number'],
            'position': player_data['position'],
            'position_full': player_data['position_full'],
            'height': player_data['height'],
            'experience': player_data['experience']
        }
    )
    if created:
        created_count += 1
        print(f"✓ Criado: {player_data['name']} ({player_data['position']})")
    else:
        print(f"✗ Já existe: {player_data['name']}")

print(f"\n✅ Total de novos jogadores adicionados: {created_count}")
