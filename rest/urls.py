from django.urls import path,include
from .views import PersonList,CountryViewset,StateViewset,StateView
#noinspection PyUnresolvedReferences
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('rest',CountryViewset,basename='country')
#router.register('state', StateViewset,basename='state')


urlpatterns=[
    path('rest/',PersonList.as_view()),
    path('viewset/', include(router.urls)),
path('rest/state/', StateViewset.as_view()),
path(r'^rest/state/(?P<pk>\d+)/$', StateView.as_view()),
    ]