#!/usr/bin/env python
"""Script para adicionar URLs de fotos dos jogadores"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spurs_site.settings')
django.setup()

from core.models import Player

# Mapeamento de nomes para IDs do NBA CDN
players_photo_ids = {
    'Victor Wembanyama': '1641705',
    'De\'Aaron Fox': '1628368',
    'Stephon Castle': '1642264',
    'Dylan Harper': '1642844',
    'Keldon Johnson': '1629640',
    'Devin Vassell': '1630170',
    'Julian Champagnie': '1630577',
    'Harrison Barnes': '203084',
    'Carter Bryant': '1642868',
    'Luke Kornet': '1628436',
    'Kelly Olynyk': '203482',
    'Mason Plumlee': '203486',
    'Bismack Biyombo': '202687',
    'Jordan McLaughlin': '1629162',
    'David Jones Garcia': '1642357',
    'Emanuel Miller': '1641801',
    'Lindy Waters III': '1630322',
    'Harrison Ingram': '1631127',
}

# URL base do NBA CDN
base_url = 'https://cdn.nba.com/headshots/nba/latest/1040x760/'

updated_count = 0
for name, nba_id in players_photo_ids.items():
    try:
        player = Player.objects.get(name=name)
        photo_url = f'{base_url}{nba_id}.png'
        player.photo_url = photo_url
        player.save()
        updated_count += 1
        print(f"✓ Atualizado: {name} - {photo_url}")
    except Player.DoesNotExist:
        print(f"✗ Jogador não encontrado: {name}")

print(f"\n✅ Total de jogadores atualizados: {updated_count}")
