# Generated by Django 3.1 on 2020-08-25 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('target_person', models.CharField(max_length=255, verbose_name='目标人群')),
                ('target_person_details', models.CharField(max_length=255, verbose_name='目标人群详情')),
                ('free', models.SmallIntegerField(choices=[(0, '否'), (1, '是')], default=0, verbose_name='免费')),
                ('published', models.SmallIntegerField(choices=[(0, '否'), (1, '是')], default=0, verbose_name='发布')),
                ('completed', models.SmallIntegerField(choices=[(0, '否'), (1, '是')], default=0, verbose_name='完结')),
                ('recommended', models.SmallIntegerField(choices=[(0, '否'), (1, '是')], default=0, verbose_name='推荐')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category', verbose_name='分类')),
            ],
            options={
                'verbose_name': '视频课程',
                'verbose_name_plural': '视频课程',
                'db_table': 'courses',
            },
        ),
    ]