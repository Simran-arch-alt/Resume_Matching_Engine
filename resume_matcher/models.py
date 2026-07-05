from django.db import models
from mongoengine import Document, StringField


class Job(Document):
    job_title = StringField()
    company = StringField()
    location = StringField()
    is_remote = StringField()
    role_category = StringField()
    seniority_level = StringField()
    is_aggregator = StringField()
    skills_str = StringField()

    meta = {
        'collection': 'jobs',
        'db_alias': 'default',
    }
