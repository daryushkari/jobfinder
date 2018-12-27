from django.db import models
from pymongo import MongoClient
import hashlib
import random
import os

client = MongoClient('localhost', 27017)
db = client.jobfinderdb


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

# example mongodb database

# Todo: should be deleted just shows how database works


# applicant = {
#     'user_name': '',
#     'password_hash': '',
#     'last_name': '',
#     'first_name': '',
#     'email': '',
#     'is_valid': '',
#     'validation_code': '',
#     'token': '',
#     'private': '',
#     'image': '',
#     'resume': {
#         'job_title': '',
#         'employment_status': '',
#         'last_corporate': '',
#         'degree': '',
#         'email_address': '',
#         'cellphone_number': '',
#         'birth_date': '',
#         'home_address': '',
#         'sex': '',
#         'about_me': '',
#         'professional_skills': [],
#         'links': '',
#         'work_experiences': [{'job_title': '',
#                               'corporate_name': '',
#                               'start_date': '',
#                               'end_time': '',
#                               'corporate_site': '',
#                               'description': '', }],
#         'field_of_study': '',
#         'study_start_time': '',
#         'study_end_time': '',
#         'education_institution_name': '',
#         'degree_description': '',
#         'languages': [{'language_name': '', 'level': ''}],
#         'job_preferences': {'work_locations': [],
#                             'work_fields': [],
#                             'level': '',
#                             'excepted_salary': '',
#                             'Job Benefits': [],
#                             }
#     },
# }
# corporate = {
#     'co_user_name': '',
#     'password_hash': '',
#     'name': '',
#     'email': '',
#     'rate': '',
#     'token': '',
#     'user_rates': [{'user_name': '', 'user_rate': 0}],
#     'is_valid': '',
#     'validation_code': '',
#     'description': '',
#     'announcements': [],
# }
#
# announcement = {
#     '_id': '',
#     'corporate_name': '',
#     'corporate_link': '',
#     'issue': '',
#     'fields': '',
#     'salary': '',
#     'start_time': '',
#     'end_time': '',
#     'sent_resumes': [],
#     'description': '',
# }

# add applicant user to database

def applicant_sign_up(first_name, last_name, user_name, password, email, token, validation_code):

    if db.applicant.find_one({'user_name': user_name}):
        return False, "user name already exist"

    new_applicant = {
        'user_name': user_name,
        'password_hash': str(hashlib.sha512(password.encode('utf-8')).hexdigest()),
        'last_name': last_name,
        'first_name': first_name,
        'email': email,
        'is_valid': False,
        'validation_code': validation_code,
        'token': token,
        'private': False,
        'image': '',
        'resume': {
            'job_title': '',
            'employment_status': '',
            'last_corporate': '',
            'degree': '',
            'email_address': '',
            'cellphone_number': '',
            'birth_date': '',
            'home_address': '',
            'sex': '',
            'about_me': '',
            'professional_skills': [],
            'links': '',
            'work_experiences': [{'job_title': '',
                                  'corporate_name': '',
                                  'start_date': '',
                                  'end_time': '',
                                  'corporate_site': '',
                                  'description': '', }],
            'field_of_study': '',
            'study_start_time': '',
            'study_end_time': '',
            'education_institution_name': '',
            'degree_description': '',
            'languages': [{'language_name': '', 'level': ''}],
            'job_preferences': {'work_locations': [],
                                'work_fields': [],
                                'level': '',
                                'excepted_salary': '',
                                'Job Benefits': [],
                                }
        },
    }

    db.applicant.insert(new_applicant)
    return True, "user created successfully"

# add corporate user to database


def corporate_sign_up(co_user_name, name, email, description, password, token, validation_code):

    if db.corporate.find_one({'co_user_name': co_user_name}):
        return False, "user name already exist"

    new_corporate = {
        'co_user_name': co_user_name,
        'password_hash': str(hashlib.sha512(password.encode('utf-8')).hexdigest()),
        'name': name,
        'email': email,
        'rate': 2.5,
        'token': token,
        'user_rates': [],
        'is_valid': False,
        'validation_code': validation_code,
        'description': description,
        'announcements': [],
    }
    db.corporate.insert(new_corporate)
    return True, "corporate created successfully"
