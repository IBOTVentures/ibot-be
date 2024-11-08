from django.urls import path
from .views import  UploadCourse, SendOTP, Forget, UpdatePassword,UploadModule, AssessmentQuestion,FetchCoursePreview,courseconfirm,courselist, addproduct,getdetails,updatedetails,CertificationAPIView,TaskStatusAPIView, AddAPIView, CourseListView,StatisticsAPIView, CertificationUpdateAPIView, OrderAPIView, CheckoutAPIView, SignUpAPIView, SignInAPIView, OfflinePurchaseUserAPIView, FileRecieverAPIView, CourseAPIView, CourseUpdateAPIView,  ModuleUpdateAPIView, AssessmentAPIView, AssessmentUpdateAPIView
urlpatterns = [

    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('signin/', SignInAPIView.as_view(), name='signin'),
    path('uploadcourse/',UploadCourse.as_view(),name='upload-course'),
    path('uploadmodule/',UploadModule.as_view(),name='upload-module'),
    path('sendotp/',SendOTP.as_view(),name='sendotp'),
    path('forget/',Forget.as_view(),name='forget'),
    path('updatepassword/',UpdatePassword.as_view(),name='updatepassword'),
    path('assessmentquestion/',AssessmentQuestion.as_view(),name='assessment-question'),
    path('coursepreview/',FetchCoursePreview.as_view(),name='course-preview'),
    path('confirm/',courseconfirm.as_view(),name='confirm'),
    path('courselist/',courselist.as_view(),name='course-list'),
    path('addproduct/',addproduct.as_view(),name='add-product'),
    path('offlinepurchase/', OfflinePurchaseUserAPIView.as_view(), name='offlinePurchase'),
    path('getdetail/',getdetails.as_view(),name='getdetail'),
    path('updatedetails/',updatedetails.as_view(),name='updatedetils'),
    path('order/', OrderAPIView.as_view(), name='order'),    
    path('orderStatus/', CheckoutAPIView.as_view(), name='checkout'),
    path('statistics/', StatisticsAPIView.as_view(), name='statistics'),
    path('certifications/', CertificationAPIView.as_view(), name='certifications'),
    path('certificationsupdate/<uuid:pk>/', CertificationUpdateAPIView.as_view(), name='certification-detail'),    
    
]



# urlpatterns = [
    
#     path('file/', FileRecieverAPIView.as_view(), name='file'),
#     path('courses/', CourseAPIView.as_view(), name='course-create'),
#     path('courseslist/<uuid:pk>/', CourseUpdateAPIView.as_view(), name='course-list'),
#     path('tasks/', TaskAPIView.as_view(), name='task-list'),
#     path('taskslist/<uuid:pk>/', TaskUpdateAPIView.as_view(), name='task-list'),
#     path('modules/', ModuleAPIView.as_view(), name='module-list'),
#     path('moduleslist/<uuid:pk>/', ModuleUpdateAPIView.as_view(), name='module-list'),
#     path('assessments/', AssessmentAPIView.as_view(), name='assessment-list'),
#     path('assessmentslist/<uuid:pk>/', AssessmentUpdateAPIView.as_view(), name='assessment-list'),
#     path('courses/', CourseListView.as_view(), name='course-list'),
#     path('add/', AddAPIView.as_view(), name='add'),
#     path('taskstatus/', TaskStatusAPIView.as_view(), name='task-status'),
#  path('coursetaskmodulecount/', CourseTaskModuleCountAPIView.as_view(), name='course-task-module-count'),
# path('usercourseprogressupdate/<uuid:pk>/', UserCourseProgressUpdateView.as_view(), name='user-course-progress-update'),
# path('usercourseprogress/', UserCourseProgressView.as_view(), name='user-course-progress'),
# ]