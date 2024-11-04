from django.db import models
from django.utils import timezone
import uuid
from django.db.models import Sum
from cloudinary.models import CloudinaryField

class User(models.Model):
    Role = (
        ('purchasedUser', 'purchasedUser'),
        ('CourseSubscribedUser', 'CourseSubscribedUser'),
        ('admin', 'admin'),
        ('visitor', 'visitor'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=Role, default='visitor')
    subscription = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class OTP(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=100, unique=True,null=True, blank=True)
    otp = models.TextField(max_length=4)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class Course(models.Model):
    age_choices = [
        ('Age 3-5', 'Age 3-5'),
        ('Age 5-9', 'Age 5-9'),
        ('Age 9+', 'Age 9+'),        
    ]
    product_choice = [
        ('U10 pro', 'U10 pro'),
        ('U20 pro', 'U20 pro'),
        ('A1', 'A1'),
        ('A3', 'A3'),
        ('S30', 'S30'),
        ('S40', 'S40'),
        ('D3 pro', 'D3 pro'),
        ('AI MODULE 1S', 'AI MODULE 1S'),
        ('AI MODULE 5S', 'AI MODULE 5S'),
        ('AI MODULE 3S', 'AI MODULE 3S'),
        ('E7 pro', 'E7 pro'),
    ]
    level_choices = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ] 
     
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_name = models.CharField(max_length=255)
    course_description = models.TextField(null=True, blank=True)
    course_duration = models.IntegerField()
    course_price = models.DecimalField(max_digits=10, decimal_places=2)
    age_category = models.CharField(max_length=50,choices=age_choices)
    level = models.CharField(max_length=100, choices=level_choices)
    isconfirmed = models.BooleanField(default=False)
    module_count = models.IntegerField()
    course_cover_image = models.ImageField(upload_to='images/')
    product_model = models.CharField(max_length=100, choices=product_choice, default='U10 pro')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class Module(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    module_name = models.CharField(max_length=255)
    module_description = models.TextField(null=True, blank=True)
    intro = models.FileField(upload_to='pdfs/',null=True, blank=True)
    content = models.FileField(upload_to='pdfs/',null=True, blank=True)
    activity = models.FileField(upload_to='pdfs/',null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')  # One Course has many Modules
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class Assessment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True)
    option1 = models.TextField(null=True, blank=True)
    option2 = models.TextField(null=True, blank=True)
    option3 = models.TextField(null=True, blank=True)
    option4 = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class Certification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey('Course', related_name='certifications', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.DurationField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class CertificationQuestion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    certification = models.ForeignKey(Certification, related_name='questions', on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class ProductKit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_number = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.FloatField()
    product_cover_image = models.ImageField(upload_to='images/',null=True, blank=True)
    age_category = models.CharField(max_length=50,null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class Transaction(models.Model):
    STATUS_CHOICES = [
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
        ('PENDING', 'Pending'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')    
    # Razorpay fields
    razorpay_payment_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    razorpay_order_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=255, null=True, blank=True)
    
    # Transaction details
    amount = models.IntegerField(null=True, blank=True)  # Store in appropriate currency format
    currency = models.CharField(max_length=10, default='INR')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    receipt = models.CharField(max_length=100, unique=True, null=True, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class OfflinePurchase(models.Model):
    Payment_Types = (
        ('online', 'online'),
        ('offline', 'offline'),
        ('cheque', 'cheque'),
        ('neft', 'neft'),
    )
    product_choice = [
        ('U10 pro', 'U10 pro'),
        ('U20 pro', 'U20 pro'),
        ('A1', 'A1'),
        ('A3', 'A3'),
        ('S30', 'S30'),
        ('S40', 'S40'),
        ('D3 pro', 'D3 pro'),
        ('AI MODULE 1S', 'AI MODULE 1S'),
        ('AI MODULE 5S', 'AI MODULE 5S'),
        ('AI MODULE 3S', 'AI MODULE 3S'),
        ('E7 pro', 'E7 pro'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    vendor_name = models.CharField(max_length=100)
    vendor_contact_name = models.CharField(max_length=100)
    vendor_contact_number = models.CharField(max_length=15)
    vendor_email = models.EmailField(max_length=100)
    vendor_address = models.TextField()
    
    customer_name = models.CharField(max_length=100)
    customer_contact_name = models.CharField(max_length=100)
    customer_contact_number = models.CharField(max_length=15)
    customer_email = models.EmailField(max_length=100)
    customer_address = models.TextField()
    
    payment_term = models.CharField(max_length=100, choices=Payment_Types, default='offline')
    order_id = models.CharField(max_length=100)
    transaction_number = models.CharField(max_length=100)
    
    product_name = models.CharField(max_length=100, choices=product_choice, default='U10 pro')
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    status = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

# class UserCourseProgress(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_progress')
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     last_module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True, blank=True)
#     last_task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)
#     is_completed = models.BooleanField(default=False)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)

# class UserAssessmentScore(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assessment_scores')
#     module = models.ForeignKey(Module, on_delete=models.CASCADE)
#     assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
#     score = models.FloatField(default=0)
#     total_marks = models.IntegerField(default=0)
#     obtained_marks = models.IntegerField(default=0)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)
    
# class Task(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
#     task_name = models.CharField(max_length=100)
#     task_description = models.TextField()
#     task_duration = models.DurationField(max_length=100)

#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)
    
    
# class Module(models.Model):
#     TYPE_OF_MODULE = (('Introduction', 'Introduction'), ('Building', 'Building'), ('Activity', 'Activity'))
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
    
#     module_name = models.CharField(max_length=100)
#     module_description = models.TextField()
#     module_type = models.CharField(max_length=100, choices=TYPE_OF_MODULE, default='Introduction')
#     file = models.FileField(upload_to='pptx_files/', null=True, blank=True)

#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)
    
# class BaseQuestion(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

#     question = models.TextField()
#     option1 = models.CharField(max_length=100)
#     option2 = models.CharField(max_length=100)
#     option3 = models.CharField(max_length=100)
#     option4 = models.CharField(max_length=100)
#     answer = models.CharField(max_length=100)
    
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)
    
# class Assessment(BaseQuestion):
#     module = models.ForeignKey(Module, on_delete=models.CASCADE)      
    