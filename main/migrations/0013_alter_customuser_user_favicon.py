# Generated by Django 3.2.8 on 2021-10-24 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_customuser_user_favicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_favicon',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]