# Generated by Django 4.1.5 on 2023-01-11 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_alter_produto_preco_marketing_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='variacao',
            name='preco_promocional',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
