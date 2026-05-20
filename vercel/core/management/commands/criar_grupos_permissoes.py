"""
Management command: criar_grupos_permissoes
==========================================

Implementa o RBAC (Role Based Access Control) criando Grupos e Permissões
nativas do Django para o sistema de empréstimos.

Uso:
    python manage.py criar_grupos_permissoes

Grupos criados:
    - admins      : acesso total ao sistema de empréstimos
    - professores : pode listar empréstimos, mas não cadastrar
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from core.models import Emprestimo


class Command(BaseCommand):
    help = 'Cria os grupos de usuários (RBAC) e associa permissões de empréstimo.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING('=== Configurando RBAC — Grupos e Permissões ===\n'))

        # Obtém o ContentType do model Emprestimo
        content_type = ContentType.objects.get_for_model(Emprestimo)

        # ── Permissões customizadas do model ──────────────────────────────────
        perm_cadastrar, _ = Permission.objects.get_or_create(
            codename='cadastrar_emprestimo',
            content_type=content_type,
            defaults={'name': 'Pode cadastrar empréstimos'},
        )
        perm_listar, _ = Permission.objects.get_or_create(
            codename='listar_emprestimo',
            content_type=content_type,
            defaults={'name': 'Pode listar empréstimos'},
        )

        # Permissões padrão geradas automaticamente pelo Django
        perm_add    = Permission.objects.get(codename='add_emprestimo',    content_type=content_type)
        perm_change = Permission.objects.get(codename='change_emprestimo', content_type=content_type)
        perm_delete = Permission.objects.get(codename='delete_emprestimo', content_type=content_type)
        perm_view   = Permission.objects.get(codename='view_emprestimo',   content_type=content_type)

        # ── Grupo: admins ─────────────────────────────────────────────────────
        grupo_admins, criado = Group.objects.get_or_create(name='admins')
        grupo_admins.permissions.set([
            perm_cadastrar,
            perm_listar,
            perm_add,
            perm_change,
            perm_delete,
            perm_view,
        ])
        status = 'CRIADO' if criado else 'ATUALIZADO'
        self.stdout.write(self.style.SUCCESS(f'  [OK] Grupo "admins" {status} com permissoes completas.'))

        # ── Grupo: professores ────────────────────────────────────────────────
        grupo_professores, criado = Group.objects.get_or_create(name='professores')
        grupo_professores.permissions.set([
            perm_listar,
            perm_view,
        ])
        status = 'CRIADO' if criado else 'ATUALIZADO'
        self.stdout.write(self.style.SUCCESS(f'  [OK] Grupo "professores" {status} com permissao de listagem.'))

        self.stdout.write('\n' + self.style.MIGRATE_HEADING('Permissoes por grupo:'))
        self.stdout.write('  admins      -> cadastrar_emprestimo, listar_emprestimo, add, change, delete, view')
        self.stdout.write('  professores -> listar_emprestimo, view')
        self.stdout.write('\n' + self.style.SUCCESS('[OK] RBAC configurado com sucesso!'))
        self.stdout.write(
            self.style.WARNING(
                '\n  Lembre-se: para que a pagina /emprestimos/ seja acessivel,\n'
                '  o usuario tambem precisa ter is_staff=True.\n'
            )
        )
