from django.urls import path
from .views import  UploadCourse, SendOTP, Forget, UpdatePassword,UploadModule, AssessmentQuestion,FetchCoursePreview,courseconfirm,courselist, addproduct,getdetails,updatedetails,CertificationAPIView, CourseListView,StatisticsAPIView, CertificationUpdateAPIView, OrderAPIView, CheckoutAPIView, SignInAPIView, OfflinePurchaseUserAPIView, canaccesscourse, checkanswers, DeleteModuleView, deleteQuestion, deleteCourse, tasktrack, canviewmodule, pickup, checkcertifyanswer, deletecertifyques,Userscheck,Signup,UserReviews, UserCourses,delaccount,categories, ProductView,CategoryAPIView

urlpatterns = [

    path('signin/', SignInAPIView.as_view(), name='signin'),
    path('signup/',Signup.as_view(),name='signup'),
    path('sendotp/',SendOTP.as_view(),name='sendotp'),
    path('forget/',Forget.as_view(),name='forget'),
    path('updatepassword/',UpdatePassword.as_view(),name='updatepassword'),
    path('getdetail/',getdetails.as_view(),name='getdetail'),
    path('updatedetails/',updatedetails.as_view(),name='updatedetils'),

    path('uploadcourse/',UploadCourse.as_view(),name='uploadcourse'),
    path('uploadmodule/',UploadModule.as_view(),name='uploadmodule'),
    path('assessmentquestion/',AssessmentQuestion.as_view(),name='assessmentquestion'),
    path('deleteaccount/',delaccount.as_view(),name='deleteaccount'),
    path('deletemodule/<uuid:id>/', DeleteModuleView.as_view(), name='deletemodule'),
    path('deleteques/<uuid:id>/',deleteQuestion.as_view(),name='deleteques'),
    path('deletecourse/<uuid:id>/',deleteCourse.as_view(),name='deletecourse'),
    path('confirm/',courseconfirm.as_view(),name='confirm'),
    path('addproduct/',addproduct.as_view(),name='addproduct'),
    path('categories/', CategoryAPIView.as_view()),  # For GET and POST
    path('offlinepurchase/', OfflinePurchaseUserAPIView.as_view(), name='offlinepurchase'),
    path('deletecertifyques/<uuid:id>/<uuid:courseid>/',deletecertifyques.as_view(),name='deletecertifyques'),
    path('statistics/', StatisticsAPIView.as_view(), name='statistics'),

    path('canaccesscourse/',canaccesscourse.as_view(),name='canaccesscourse'),
    path('tasktracking/',tasktrack.as_view(),name='tasktrack'),
    path('canviewmodule/',canviewmodule.as_view(),name='canviewmodule'),
    path('pickup/',pickup.as_view(),name='pickup'),
    path('coursepreview/',FetchCoursePreview.as_view(),name='course-preview'),
    path('courselist/',courselist.as_view(),name='courselist'),
    path('submitanswers/',checkanswers.as_view(),name='submitanswers'),
    path('submitcertificationanswers/',checkcertifyanswer.as_view(),name='submitcertificationanswer'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('productfilter/',ProductView.as_view(),name='productfilter'),
    path('isallowed/',Userscheck.as_view(),name='isallowed'),
    path('reviews/',UserReviews.as_view(),name='reviews'),
    path('userstartedcourses/',UserCourses.as_view(),name='usercourses'),
    path('getcategory/',categories.as_view(),name='getcategory'),
    
    path('order/', OrderAPIView.as_view(), name='order'),    
    path('orderStatus/', CheckoutAPIView.as_view(), name='checkout'),
   
    path('certifications/', CertificationAPIView.as_view(), name='certifications'),
    path('certificationsupdate/<uuid:pk>/', CertificationUpdateAPIView.as_view(), name='certification-detail'),  
    
   
]



