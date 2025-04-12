from django.db import migrations

def create_initial_data(apps, schema_editor):
    Status = apps.get_model('core', 'Status')
    Type = apps.get_model('core', 'Type')
    Category = apps.get_model('core', 'Category')
    Subcategory = apps.get_model('core', 'Subcategory')

    for name in ['Бизнес', 'Личное', 'Налог']:
        Status.objects.get_or_create(name=name)

    income, _ = Type.objects.get_or_create(name='Пополнение')
    outcome, _ = Type.objects.get_or_create(name='Списание')

    infra, _ = Category.objects.get_or_create(name='Инфраструктура', type=outcome)
    marketing, _ = Category.objects.get_or_create(name='Маркетинг', type=outcome)

    Subcategory.objects.get_or_create(name='VPS', category=infra)
    Subcategory.objects.get_or_create(name='Proxy', category=infra)
    Subcategory.objects.get_or_create(name='Farpost', category=marketing)
    Subcategory.objects.get_or_create(name='Avito', category=marketing)

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]
