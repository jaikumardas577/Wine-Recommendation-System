from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.urls import resolve
from django.conf import settings
from wine_recommender.views import review_list,review_detail,wine_detail,user_review_list,user_recommendation_list
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /wine/
    url(r'^wine$', views.wine_list, name='wine_list'),
    # ex: /wine/5/
    url(r'^wine/(?P<wine_id>[0-9]+)/$', views.wine_detail, name='wine_detail'),
    url(r'^wine/(?P<wine_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    # ex: /review/user - get reviews for the logged user
    url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    url(r'^review/user/$', views.user_review_list, name='user_review_list'), 
    url(r'^recommendation/$', views.user_recommendation_list, name='user_recommendation_list'),
	]