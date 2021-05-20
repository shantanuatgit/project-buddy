# Generated by Django 2.2.13 on 2021-04-16 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0003_auto_20210416_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='allprofile',
            name='backendframework',
            field=models.CharField(choices=[('Django', 'Django'), ('Laravel', 'Larvel'), ('Ruby on Rails', 'Ruby on Rails'), ('NodeJS', 'NodeJS'), ('CakePHP', 'CakePHP'), ('Flask', 'Flask'), ('Asp.NET', 'Asp.NET'), ('Spring Boot', 'Spring Boot'), ('Koa', 'Koa'), ('Phoenix', 'Phoenix'), ('None', 'None')], default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='allprofile',
            name='frontendframework',
            field=models.CharField(choices=[('React', 'React'), ('Angular', 'Angular'), ('Vue.js', 'Vue.js'), ('AngularJS', 'AngularJS'), ('Svelte', 'Svelte'), ('Express.js', 'Express.js'), ('Next.js', 'Next.js'), ('None', 'None')], default='None', max_length=5),
        ),
        migrations.AlterField(
            model_name='allprofile',
            name='languages',
            field=models.CharField(choices=[('Python', 'Python'), ('Java', 'Java'), ('Javascript', 'Javascript'), ('Ruby', 'Ruby'), ('C', 'C'), ('C++', 'C++'), ('GO', 'GO'), ('R', 'R'), ('Perl', 'Perl'), ('Swift', 'Swift'), ('PHP', 'PHP'), ('Objective-C', 'Objective-C'), ('C#', 'C#'), ('SQL', 'SQL'), ('None', 'None')], default='None', max_length=50),
        ),
    ]
