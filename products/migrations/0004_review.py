# Generated by Django 4.1.7 on 2023-08-28 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_promotion_variation_variationoption_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_id', models.CharField(max_length=100)),
                ('rating_value', models.CharField(max_length=50)),
                ('comment', models.TextField()),
                ('ordered_product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.review')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
