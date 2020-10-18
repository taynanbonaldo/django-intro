from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

class Usuario(AbstractBaseUser):
    email = models.EmailField(unique = True)
    nome = models.CharField(max_length = 120)
    nascimento = models.DateField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome"]

    objects = UserManager()


""" from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nome_completo', models.CharField(max_length=155)),
                ('nascimento', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ] """
    