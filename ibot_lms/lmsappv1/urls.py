from django.urls import path
from .views import SendOTP, Forget, UpdatePassword, FetchCoursePreview,courselist, addproduct,getdetails,updatedetails,CertificationAPIView, CourseListView, OrderAPIView, CheckoutAPIView, SignInAPIView, OfflinePurchaseUserAPIView, canaccesscourse, checkanswers, tasktrack, canviewmodule, pickup, checkcertifyanswer, Signup,UserReviews, UserCourses,delaccount,categories, ProductView,CategoryAPIView, Eachproduct, ProductReviews,SubscriptionAmount,transact,cartproduct, carttransact,delcart,getprodetail, buyerct, activates, delcoursereview, delproductreview

urlpatterns = [

    path('signin/', SignInAPIView.as_view(), name='signin'),
    path('signup/',Signup.as_view(),name='signup'),
    path('sendotp/',SendOTP.as_view(),name='sendotp'),
    path('forget/',Forget.as_view(),name='forget'),
    path('updatepassword/',UpdatePassword.as_view(),name='updatepassword'),
    path('getdetail/',getdetails.as_view(),name='getdetail'),
    path('updatedetails/',updatedetails.as_view(),name='updatedetils'),
    path('activateaccount/',activates.as_view(),name='activateaccount'),
    # path('uploadcourse/',UploadCourse.as_view(),name='uploadcourse'),
    # path('uploadmodule/',UploadModule.as_view(),name='uploadmodule'),
    # path('assessmentquestion/',AssessmentQuestion.as_view(),name='assessmentquestion'),
    path('deleteaccount/',delaccount.as_view(),name='deleteaccount'),
    # path('deletemodule/<uuid:id>/', DeleteModuleView.as_view(), name='deletemodule'),
    # path('deleteques/<uuid:id>/',deleteQuestion.as_view(),name='deleteques'),
    # path('deletecourse/<uuid:id>/',deleteCourse.as_view(),name='deletecourse'),
    # path('confirm/',courseconfirm.as_view(),name='confirm'),
    path('addproduct/',addproduct.as_view(),name='addproduct'),
    path('categories/', CategoryAPIView.as_view()),  # For GET and POST
    path('offlinepurchase/', OfflinePurchaseUserAPIView.as_view(), name='offlinepurchase'),
    # path('deletecertifyques/<uuid:id>/<uuid:courseid>/',deletecertifyques.as_view(),name='deletecertifyques'),
    # path('statistics/', StatisticsAPIView.as_view(), name='statistics'),

    path('canaccesscourse/',canaccesscourse.as_view(),name='canaccesscourse'),
    path('tasktracking/',tasktrack.as_view(),name='tasktrack'),
    path('canviewmodule/',canviewmodule.as_view(),name='canviewmodule'),
    path('pickup/',pickup.as_view(),name='pickup'),
    path('coursepreview/',FetchCoursePreview.as_view(),name='course-preview'),
    path('courselist/',courselist.as_view(),name='courselist'),
    path('submitanswers/',checkanswers.as_view(),name='submitanswers'),
    path('submitcertificationanswers/',checkcertifyanswer.as_view(),name='submitcertificationanswer'),
    path('coursescategory/', CourseListView.as_view(), name='course-list'),
    path('productfilter/',ProductView.as_view(),name='productfilter'),
    path('productreviews/',ProductReviews.as_view(),name='productreviews'),
    path('eachproduct/', Eachproduct.as_view(),name='eachproduct'),
    # path('isallowed/',Userscheck.as_view(),name='isallowed'),
    path('reviews/',UserReviews.as_view(),name='reviews'),
    path('delcoursereview/<uuid:id>/',delcoursereview.as_view(),name='delcoursereview'),
    path('delproductreview/<uuid:id>/',delproductreview.as_view(),name='delproductreview'),
    path('userstartedcourses/',UserCourses.as_view(),name='usercourses'),
    path('listcategory/',categories.as_view(),name='listcategory'),
    path('getsubscription/', SubscriptionAmount.as_view(), name='getsubscription'),
    path('order/', OrderAPIView.as_view(), name='order'),    
    path('orderStatus/', CheckoutAPIView.as_view(), name='checkout'),
    path('buyercount/', buyerct.as_view(),name='buyercount'),
    path('transact/', transact.as_view(), name='transact'),
    path('productcart/', cartproduct.as_view(), name='productcart'),
    path('usercart/',carttransact.as_view(),name='usercart'),
    path('delcart/<uuid:id>/',delcart.as_view(),name='delcart'),
    path('getprodetail/',getprodetail.as_view(),name='getprodetail'),
    path('certifications/', CertificationAPIView.as_view(), name='certifications'),
    # path('certificationsupdate/<uuid:pk>/', CertificationUpdateAPIView.as_view(), name='certification-detail'),  
    
]



