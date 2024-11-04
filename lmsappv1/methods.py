import hashlib
import datetime
import re
import random
import jwt
import string
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .models import User, OfflinePurchase, Module
from decouple import config

def encrypt_password(raw_password):
    salt = hashlib.sha256()
    salt.update(raw_password.encode('utf-8'))
    salt_bytes = salt.digest()

    hashed_password = hashlib.sha256()
    hashed_password.update(raw_password.encode('utf-8') + salt_bytes)
    hashed_password_bytes = hashed_password.digest()

    return hashed_password_bytes.hex()

def generate_otp():
    return random.randint(1000, 9999)
    
def purchasedUser_encode_token(payload: dict):
    payload["exp"] = datetime.datetime.now(
        tz=datetime.timezone.utc
    ) + datetime.timedelta(days=7)
    token = jwt.encode(payload, "purchasedUser_key", algorithm="HS256")
    return token

def courseSubscribedUser_encode_token(payload: dict):
    payload["exp"] = datetime.datetime.now(
        tz=datetime.timezone.utc
    ) + datetime.timedelta(days=7)
    token = jwt.encode(payload, "CourseSubscribedUser_key", algorithm="HS256")
    return token

def admin_encode_token(payload: dict):
    payload["exp"] = datetime.datetime.now(
        tz=datetime.timezone.utc
    ) + datetime.timedelta(days=7)
    token = jwt.encode(payload, "admin_key", algorithm="HS256")
    return token

def visitor_encode_token(payload: dict):
    payload["exp"] = datetime.datetime.now(
        tz=datetime.timezone.utc
    ) + datetime.timedelta(days=7)
    token = jwt.encode(payload, "visitor_key", algorithm="HS256")
    return token

# def calculate_course_progress(user, course):
#     total_modules = Module.objects.filter(task__course=course).count()  # Updated to reflect the relation
#     completed_modules = UserCourseProgress.objects.filter(user=user, course=course, is_completed=True).count()
#     return (completed_modules / total_modules) * 100 if total_modules > 0 else 0