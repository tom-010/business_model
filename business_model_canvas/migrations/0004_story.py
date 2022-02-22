# Generated by Django 4.0.2 on 2022-02-22 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business_model_canvas', '0003_businessmodelcanvas_one_sentence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('version', models.IntegerField(default=1)),
                ('character', models.TextField(blank=True, default='')),
                ('problem_villain', models.TextField(blank=True, default='')),
                ('problem_external', models.TextField(blank=True, default='')),
                ('problem_internal', models.TextField(blank=True, default='')),
                ('problem_philosophical', models.TextField(blank=True, default='')),
                ('guide_empathy', models.TextField(blank=True, default='')),
                ('guide_competence', models.TextField(blank=True, default='')),
                ('plan_process', models.TextField(blank=True, default='')),
                ('plan_agreement', models.TextField(blank=True, default='')),
                ('action_direct', models.TextField(blank=True, default='')),
                ('action_transitional', models.TextField(blank=True, default='')),
                ('avoid_failure', models.TextField(blank=True, default='')),
                ('success', models.TextField(blank=True, default='')),
                ('previous', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business_model_canvas.story')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
