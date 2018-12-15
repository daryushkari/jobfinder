from django.db import models

# Create your models here.


class Applicant(models.Model):
    user_name = models.CharField(max_length=100, primary_key=True)
    password_hash = models.TextField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    valid_applicant = models.BooleanField()
    validation_code = models.CharField(max_length=10)

    # resume information
    private_resume = models.BooleanField()
    image_addr = models.TextField()
    job_title = models.CharField(max_length=100)
    employment_status = models.CharField(max_length=50)
    last_corporate = models.CharField(max_length=100)
    last_educational_certificate_degree = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    cellphone_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    birth_date = models.DateField()
    home_address = models.TextField()
    sex = models.CharField(max_length=100)
    martial_status = models.BooleanField()
    about_me = models.TextField()
    professional_skills = models.TextField()
    link1 = models.TextField()
    link2 = models.TextField()
    link3 = models.TextField()
    link4 = models.TextField()
    # work experience 1
    work_experience1_job_title = models.CharField(max_length=50)
    work_experience1_corporate_name = models.CharField(max_length=50)
    work_experience1_start_date = models.DateField()
    work_experience1_end_date = models.DateField()
    work_experience1_description = models.TextField()
    # work experience 2
    work_experience2_job_title = models.CharField(max_length=50)
    work_experience2_corporate_name = models.CharField(max_length=50)
    work_experience2_start_date = models.DateField()
    work_experience2_end_date = models.DateField()
    work_experience2_description = models.TextField()
    # work experience 3
    work_experience3_job_title = models.CharField(max_length=50)
    work_experience3_corporate_name = models.CharField(max_length=50)
    work_experience3_start_date = models.DateField()
    work_experience3_end_date = models.DateField()
    work_experience3_description = models.TextField()
    # work experience 4
    work_experience4_job_title = models.CharField(max_length=50)
    work_experience4_corporate_name = models.CharField(max_length=50)
    work_experience4_start_date = models.DateField()
    work_experience4_end_date = models.DateField()
    work_experience4_description = models.TextField()
    # work experience 5
    work_experience5_job_title = models.CharField(max_length=50)
    work_experience5_corporate_name = models.CharField(max_length=50)
    work_experience5_start_date = models.DateField()
    work_experience5_end_date = models.DateField()
    work_experience5_description = models.TextField()
    more_work_experiences = models.TextField()
    # last educational certificate
    degree = models.CharField(max_length=30)
    field_of_study = models.CharField(max_length=30)
    start_time = models.DateField()
    end_time = models.DateField()
    degree_description = models.TextField()
    # languages
    languages = models.TextField()
    # Job preferences
    job_preferences = models.TextField()


# include corporates information


class Corporate(models.Model):
    co_name = models.CharField(max_length=100, primary_key=True)
    password_hash = models.TextField()
    corporate_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    Description = models.TextField()
    valid_corporate = models.BooleanField()
    validation_code = models.CharField(max_length=10)

# include job announcement information


class Announcement(models.Model):
    ann_id = models.CharField(max_length=50, primary_key=True)
    co_name = models.ForeignKey(Corporate, on_delete=models.CASCADE)
    ann_issue = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateField()
    end_time = models.DateField()


class SentResume(models.Model):
    ann_id = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    user_name = models.ForeignKey(Applicant, on_delete=models.CASCADE)


class Rate(models.Model):
    corporate_id = models.ForeignKey(Corporate, on_delete=models.CASCADE)
    user_name = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    rate = models.IntegerField()
