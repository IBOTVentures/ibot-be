from rest_framework import serializers
from .models import User, OfflinePurchase, Transaction, Course, Module, Assessment, Certification, CertificationQuestion, OTP, ProductKit, UserCourseProgress,UserAssessmentScore, UserCertificationScore
from django.core.files.storage import default_storage

# Serializer for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']  

    def update(self, instance, validated_data):
        new_image = validated_data.get('profile')
        if new_image and instance.profile:
            old_image_path = instance.profile.path
            if default_storage.exists(old_image_path):
                default_storage.delete(old_image_path)

        # Update instance with validated data
        return super().update(instance, validated_data)
       
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields = '__all__'

class TasktrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourseProgress
        fields = '__all__'

# Serializer for Module model
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

# Serializer for BaseQuestion model
class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Assessment
        fields = '__all__'

class UserAssessmentSerialiser(serializers.ModelSerializer):
    class Meta:
        model= UserAssessmentScore
        fields = '__all__'

class UserCertificationSerialiser(serializers.ModelSerializer):
    class Meta:
        model= UserCertificationScore
        fields = '__all__'

# Serializer for CertificationQuestion model
class CertificationQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationQuestion
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'answer','id']

class CertificationsSerializer(serializers.ModelSerializer):
    questions = CertificationQuestionSerializer(many=True)

    class Meta:
        model = Certification
        fields = ['name', 'description', 'duration', 'questions', 'course']  # Exclude course from fields

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        # Create the certification instance without course
        certification = Certification.objects.create(**validated_data)

        # Associate course with the certification
        certification.course = self.context['course']  # Set the course reference
        certification.save()  # Save the certification again to update the course

        for question_data in questions_data:
            question_data['certification'] = certification  # Associate the certification
            CertificationQuestion.objects.create(**question_data)

        return certification

    def update(self, instance, validated_data):
        questions_data = validated_data.pop('questions')
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()

        for question_data in questions_data:
            question_id = question_data.get('id')
            if question_id:
                question = CertificationQuestion.objects.get(id=question_id, certification=instance)
                question.question = question_data.get('question', question.question)
                question.option1 = question_data.get('option1', question.option1)
                question.option2 = question_data.get('option2', question.option2)
                question.option3 = question_data.get('option3', question.option3)
                question.option4 = question_data.get('option4', question.option4)
                question.answer = question_data.get('answer', question.answer)
                question.save()
            else:
                CertificationQuestion.objects.create(certification=instance, **question_data)
        
        return instance
    
# Serializer for Certification model with nested questions
class CertificationSerializer(serializers.ModelSerializer):
    questions = CertificationQuestionSerializer(many=True)
    class Meta:
        model = Certification
        fields = ['name', 'description', 'duration', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        certification = Certification.objects.create(**validated_data)
        for question_data in questions_data:
            CertificationQuestion.objects.create(certification=certification, **question_data)
        return certification
    
class UserCourseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourseProgress
        fields = ['id', 'user', 'course', 'course_name', 'last_module', 'last_module_name', 'last_task', 'last_task_name', 'is_completed', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
    
class StatisticsSerializer(serializers.Serializer):
    total_users = serializers.IntegerField()
    purchased_users = serializers.IntegerField()
    subscribed_users = serializers.IntegerField()
    users_by_role = serializers.DictField(child=serializers.IntegerField())
    
    total_purchases = serializers.IntegerField()
    purchases_by_product = serializers.DictField(child=serializers.IntegerField())
    revenue_by_product = serializers.DictField(child=serializers.FloatField())
    purchases_by_payment_method = serializers.DictField(child=serializers.IntegerField())
    
    total_courses = serializers.IntegerField()
    courses_by_level = serializers.DictField(child=serializers.IntegerField())
    courses_by_age_category = serializers.DictField(child=serializers.IntegerField())
    courses_by_product = serializers.DictField(child=serializers.IntegerField())

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductKit
        fields = '__all__'

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = '__all__'

# Serializer for OfflinePurchase model
class OfflinePurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfflinePurchase
        fields = '__all__'

# Serializer for Transaction model for order-related fields
class TransactionOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['user_id', 'amount', 'currency', 'receipt']

# Serializer for Transaction model for checkout-related fields
class TransactionCheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['user_id', 'razorpay_payment_id', 'razorpay_order_id', 'razorpay_signature']














# Serializer for BaseQuestion model #Assessment Serializer
# class BaseQuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Assessment
#         fields = ['question', 'option1', 'option2', 'option3', 'option4', 'answer']

# Serializer for Assessment model, inheriting from BaseQuestionSerializer
# class AssessmentSerializer(BaseQuestionSerializer):
#     class Meta(BaseQuestionSerializer.Meta):
#         model = Assessment
#         fields = BaseQuestionSerializer.Meta.fields

# Serializer for Module model with nested assessments
# class ModuleSerializer(serializers.ModelSerializer):
#     assessments = AssessmentSerializer(many=True, write_only=True)
#     class Meta:
#         model = Module
#         fields = ['module_name', 'module_description', 'module_type', 'file', 'assessments']

#     def create(self, validated_data):
#         assessments_data = validated_data.pop('assessments')
#         module = Module.objects.create(**validated_data)
#         # Create assessments related to the module
#         for assessment_data in assessments_data:
#             Assessment.objects.create(module=module, **assessment_data)
#         return module


# Serializer for Task model with nested modules
# class TaskSerializer(serializers.ModelSerializer):
#     modules = ModuleSerializer(many=True, write_only=True)
#     class Meta:
#         model = Task
#         fields = ['task_name', 'task_description', 'task_duration', 'modules']

#     def create(self, validated_data):
#         modules_data = validated_data.pop('modules')
#         task = Task.objects.create(**validated_data)
#         for module_data in modules_data:
#             assessments_data = module_data.pop('assessments')
#             module = Module.objects.create(task=task, **module_data)
#             for assessment_data in assessments_data:
#                 Assessment.objects.create(module=module, **assessment_data)
#         return task

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_description', 'course_duration', 'age_category', 'level']
        
class CourseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'course_description', 'course_duration', 'age_category', 'level']
        
# class TaskListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ['id', 'task_name', 'task_description', 'task_duration']
        
# class TaskUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ['task_name', 'task_description', 'task_duration']
        
# class ModuleListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Module
#         fields = ['id', 'module_name', 'module_description', 'module_type', 'file']
        
# class ModuleUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Module
#         fields = ['module_name', 'module_description', 'module_type', 'file']
        
# class AssessmentListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Assessment
#         fields = ['id', 'question', 'option1', 'option2', 'option3', 'option4', 'answer']


# class CourseTaskModuleSerializer(serializers.ModelSerializer):
#     tasks_count = serializers.SerializerMethodField()
#     modules_count = serializers.SerializerMethodField()

#     class Meta:
#         model = Course
#         fields = ['id', 'course_name', 'tasks_count', 'modules_count']

#     def get_tasks_count(self, obj):
#         return Task.objects.filter(course=obj).count()

#     def get_modules_count(self, obj):
#         return Module.objects.filter(task__course=obj).count()
    
class CourseFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

#got repeated
# class CertificationQuestionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CertificationQuestion
#         fields = ['question', 'option1', 'option2', 'option3', 'option4', 'answer'] 

# Serializer for Course model with nested tasks and certification
# class CourseSerializer(serializers.ModelSerializer):
#     tasks = TaskSerializer(many=True, write_only=True)
#     certification = CertificationSerializer(write_only=True)
#     class Meta:
#         model = Course
#         fields = ['course_name', 'course_description', 'course_duration', 'age_category', 'level', 'tasks', 'certification']

#     def create(self, validated_data):
#         tasks_data = validated_data.pop('tasks')
#         certification_data = validated_data.pop('certification')
#         course = Course.objects.create(**validated_data)
#         for task_data in tasks_data:
#             modules_data = task_data.pop('modules')
#             task = Task.objects.create(course=course, **task_data)
#             for module_data in modules_data:
#                 assessments_data = module_data.pop('assessments')
#                 module = Module.objects.create(task=task, **module_data)
#                 for assessment_data in assessments_data:
#                     Assessment.objects.create(module=module, **assessment_data)
#         questions_data = certification_data.pop('questions', [])
#         print("Certification Data: ", certification_data)
#         print("Questions Data: ", questions_data)
#         certification = Certification.objects.create(course=course, **certification_data)
#         for question_data in questions_data:
#             print("Creating question: ", question_data)
#             CertificationQuestion.objects.create(certification=certification, **question_data)
#         return course

# Serializer for Module model
# class ModuleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Module
#         fields = ['module_name', 'file']
