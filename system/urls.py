from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('biker/', views.bike, name='biker'),
    path('trucker/', views.truck, name='trucker'),
    path('transport/', views.transport, name='transport'),
    path('register/', views.register, name='register'),
    path('bform', views.bform, name='bform'),
    path('tform', views.tform, name='tform'),
    path('cform',views.cform,name='cform'),
    path('book',views.book,name='book'),
    path('about',views.about,name='about'),
    path('house', views.house, name='house'),
    path('corporate', views.corporate, name='corporate'),
    path('office', views.office, name='office'),
    path('personal', views.personal, name='personal'),
    path('house/housemore', views.housemore, name='housemore'),
    path('corporate/corporatemore', views.corporatemore, name='corporatemore'),
    path('office/officemore', views.officemore, name='officemore'),
    path('personal/personalmore', views.personalmore, name='personalmore'),
    path('cbook',views.cbook,name='cbook'),
    path('pbook', views.pbook, name='pbook'),
    path('ofbook', views.ofbook, name='ofbook'),
]