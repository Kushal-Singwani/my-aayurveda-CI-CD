from django.urls import path
from app1 import views
urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('service/',views.service,name="service"),
    path('blog/',views.blog,name="blog"),
    path('contact/',views.contact,name="contact"),
    path('contact/',views.contact,name="contact"),
   
    path('login/',views.userlogin,name="login"),
    path('register/',views.Register,name="register"),
    path('logout/',views.log_out,name="logout"),
    
    # client panal urls 
    path("clienthome/",views.clienthome,name="clienthome"),
    path("payment_info/",views.payment_info,name="payment_info"),
    path("profile/",views.profile,name="profile"),
    path("document/",views.document,name="document"),
    path("send_query/",views.send_query,name="send_query"),
    path("view_suggestion/",views.view_suggestion,name="view_suggestion"),
    
    # admin panal usrl
    path("adminhome/",views.adminhome,name="adminhome"),
    path("client-profile/",views.client_profile,name="client-profile"),
    path("send-suggestions/",views.send_suggestions,name="send-suggestions"),
    path("users-profile/",views.admin_profile,name="users-profile"),
    path("view-documents/",views.view_documents,name="view-documents"),
    path("view-receive-payment/",views.view_receive_payment,name="view-receive-payment"),
    path("view-suggestions/",views.view_suggestions,name="view-suggestions"),
    path("user_edit/<int:id>",views.user_edit,name="user_edit"),
    path("pages_login/",views.pages_login,name="pages_login"),
    path("admin_logout/",views.admin_log_out,name="admin_logout"),
    
    path("delete/<int:id>",views.delete,name="delete"),
    path("update/<int:id>",views.update,name="update"),
]