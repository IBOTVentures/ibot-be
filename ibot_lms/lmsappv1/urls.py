from django.urls import path
from .views import CertificationAPIView,TaskStatusAPIView, AddAPIView, CourseListView,StatisticsAPIView, CourseTaskModuleCountAPIView, CertificationUpdateAPIView, OrderAPIView, CheckoutAPIView, SignUpAPIView, SignInAPIView, OfflinePurchaseUserAPIView, TaskAPIView, TaskUpdateAPIView, UserCourseProgressUpdateView, UserCourseProgressView, FileRecieverAPIView, CourseAPIView, CourseUpdateAPIView, ModuleAPIView, ModuleUpdateAPIView, AssessmentAPIView, AssessmentUpdateAPIView

urlpatterns = [
    path('order/', OrderAPIView.as_view(), name='order'),    
    path('orderStatus/', CheckoutAPIView.as_view(), name='checkout'),
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('signin/', SignInAPIView.as_view(), name='signin'),
    path('offlinepurchase/', OfflinePurchaseUserAPIView.as_view(), name='offlinePurchase'),
    path('file/', FileRecieverAPIView.as_view(), name='file'),
    path('courses/', CourseAPIView.as_view(), name='course-create'),
    path('courseslist/<uuid:pk>/', CourseUpdateAPIView.as_view(), name='course-list'),
    path('tasks/', TaskAPIView.as_view(), name='task-list'),
    path('taskslist/<uuid:pk>/', TaskUpdateAPIView.as_view(), name='task-list'),
    path('modules/', ModuleAPIView.as_view(), name='module-list'),
    path('moduleslist/<uuid:pk>/', ModuleUpdateAPIView.as_view(), name='module-list'),
    path('assessments/', AssessmentAPIView.as_view(), name='assessment-list'),
    path('assessmentslist/<uuid:pk>/', AssessmentUpdateAPIView.as_view(), name='assessment-list'),
    path('certifications/', CertificationAPIView.as_view(), name='certifications'),
    path('certificationsupdate/<uuid:pk>/', CertificationUpdateAPIView.as_view(), name='certification-detail'),    
    path('usercourseprogress/', UserCourseProgressView.as_view(), name='user-course-progress'),
    path('usercourseprogressupdate/<uuid:pk>/', UserCourseProgressUpdateView.as_view(), name='user-course-progress-update'),
    path('coursetaskmodulecount/', CourseTaskModuleCountAPIView.as_view(), name='course-task-module-count'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('statistics/', StatisticsAPIView.as_view(), name='statistics'),
    
    path('add/', AddAPIView.as_view(), name='add'),
    path('taskstatus/', TaskStatusAPIView.as_view(), name='task-status'),
]