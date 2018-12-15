# Generated by Django 2.1.4 on 2018-12-15 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('ann_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('ann_issue', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('user_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password_hash', models.TextField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('valid_applicant', models.BooleanField()),
                ('validation_code', models.CharField(max_length=10)),
                ('private_resume', models.BooleanField()),
                ('image_addr', models.TextField()),
                ('job_title', models.CharField(max_length=100)),
                ('employment_status', models.CharField(max_length=50)),
                ('last_corporate', models.CharField(max_length=100)),
                ('last_educational_certificate_degree', models.CharField(max_length=100)),
                ('email_address', models.CharField(max_length=100)),
                ('cellphone_number', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('home_address', models.TextField()),
                ('sex', models.CharField(max_length=100)),
                ('martial_status', models.BooleanField()),
                ('about_me', models.TextField()),
                ('professional_skills', models.TextField()),
                ('link1', models.TextField()),
                ('link2', models.TextField()),
                ('link3', models.TextField()),
                ('link4', models.TextField()),
                ('work_experience1_job_title', models.CharField(max_length=50)),
                ('work_experience1_corporate_name', models.CharField(max_length=50)),
                ('work_experience1_start_date', models.DateField()),
                ('work_experience1_end_date', models.DateField()),
                ('work_experience1_description', models.TextField()),
                ('work_experience2_job_title', models.CharField(max_length=50)),
                ('work_experience2_corporate_name', models.CharField(max_length=50)),
                ('work_experience2_start_date', models.DateField()),
                ('work_experience2_end_date', models.DateField()),
                ('work_experience2_description', models.TextField()),
                ('work_experience3_job_title', models.CharField(max_length=50)),
                ('work_experience3_corporate_name', models.CharField(max_length=50)),
                ('work_experience3_start_date', models.DateField()),
                ('work_experience3_end_date', models.DateField()),
                ('work_experience3_description', models.TextField()),
                ('work_experience4_job_title', models.CharField(max_length=50)),
                ('work_experience4_corporate_name', models.CharField(max_length=50)),
                ('work_experience4_start_date', models.DateField()),
                ('work_experience4_end_date', models.DateField()),
                ('work_experience4_description', models.TextField()),
                ('work_experience5_job_title', models.CharField(max_length=50)),
                ('work_experience5_corporate_name', models.CharField(max_length=50)),
                ('work_experience5_start_date', models.DateField()),
                ('work_experience5_end_date', models.DateField()),
                ('work_experience5_description', models.TextField()),
                ('more_work_experiences', models.TextField()),
                ('degree', models.CharField(max_length=30)),
                ('field_of_study', models.CharField(max_length=30)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('degree_description', models.TextField()),
                ('languages', models.TextField()),
                ('job_preferences', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Corporate',
            fields=[
                ('co_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password_hash', models.TextField()),
                ('corporate_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('valid_corporate', models.BooleanField()),
                ('validation_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('corporate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Corporate')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='SentResume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ann_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Announcement')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Applicant')),
            ],
        ),
        migrations.AddField(
            model_name='announcement',
            name='co_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Corporate'),
        ),
    ]
