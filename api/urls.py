from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

from api import views
from api.views import ListAnimes, AnimeName, ListCreateAnime, CustomAuthToken

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'username', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('ratings', ListAnimes.as_view()),
    path('animes/<name>', AnimeName.as_view()),
    path('animes/', ListCreateAnime.as_view()),
    path('api-token-auth/', CustomAuthToken.as_view())
]