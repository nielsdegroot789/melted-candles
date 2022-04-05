# Generated by Django 4.0.3 on 2022-04-05 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candles', '0002_candle_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='candle',
            name='description',
            field=models.TextField(default='descr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candle',
            name='name',
            field=models.CharField(default='name', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candle',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='candle',
            name='price',
            field=models.DecimalField(decimal_places=2, default=12, max_digits=4),
            preserve_default=False,
        ),
    ]