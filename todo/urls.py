# from django.contrib import admin
# from django.urls import path, include
# from todo import views
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path("", views.todohome, name='todo'),
#     path('about/', views.about, name='about'),
# ]

# # Serve static files in development (images placed in templates/static/)
# if settings.DEBUG:
#     # settings.STATICFILES_DIRS is a list; use first entry as document_root
#     if getattr(settings, 'STATICFILES_DIRS', None):
#         document_root = settings.STATICFILES_DIRS[0]
#     else:
#         document_root = None
#     if document_root:
#         urlpatterns += static(settings.STATIC_URL, document_root=document_root)



from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Home and main pages
    path('', views.todohome, name='todo'),
    path('about/', views.about, name='about'),
    path('features/', views.features_page, name='features'),
    
    # Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Todo management
    path('todos/', views.todos_list, name='todos_list'),
    path('todos/create/', views.create_todo, name='create_todo'),
    path('todos/<int:todo_id>/edit/', views.edit_todo, name='edit_todo'),
    path('todos/<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),
    
    # Feature management
    path('features/add/', views.feature_add_view, name='add_feature'),
    path('features/suggest/', views.suggest_feature, name='suggest_feature'),
]

if settings.DEBUG:
    # Serve static files from the first STATICFILES_DIRS entry in development
    if getattr(settings, 'STATICFILES_DIRS', None):
        docroot = settings.STATICFILES_DIRS[0]
    else:
        docroot = None
    if docroot:
        urlpatterns += static(settings.STATIC_URL, document_root=docroot)
