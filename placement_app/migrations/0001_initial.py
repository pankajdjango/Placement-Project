# Generated by Django 4.2.7 on 2023-11-26 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('co_name', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Interviews',
            fields=[
                ('interview_id', models.AutoField(primary_key=True, serialize=False)),
                ('interview_date', models.DateField()),
                ('interview_status', models.CharField(max_length=50)),
                ('interview_feedback', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_app.companies')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('roll_number', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=80)),
                ('branch', models.CharField(max_length=50)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Placements',
            fields=[
                ('placement_id', models.AutoField(primary_key=True, serialize=False)),
                ('placement_date', models.DateField()),
                ('offered_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_app.companies')),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_app.interviews')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_app.students')),
            ],
        ),
        migrations.AddField(
            model_name='interviews',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_app.students'),
        ),
    ]