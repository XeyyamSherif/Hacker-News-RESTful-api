"""hackernews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/post-list/', views.postlist),
    path('api/post-detail/<str:pk>', views.postDetail),
    # path('api/add-post/', views.addPost),
    # path('api/delete-post/<str:pk>', views.deletePost),
    # path('api/update-post/<str:pk>', views.updatePost),

    path('api/edit-comment/<str:pk>', views.edit_comments),
    path('api/add-comment/<str:pk>', views.addComment),
    path('api/list-comment/<str:pk>', views.comments_of_post),
    #path('api/update-comment/<str:pk>', views.updateComment),


    path('api/increase-upvote/<str:pk>', views.increase_upvote),
    # path('api/reset-upvote/', views.reset_upvotes)
]
