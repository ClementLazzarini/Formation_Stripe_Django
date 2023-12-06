from django.urls import path
from django.conf.urls.static import static
from Shopformation import settings
from shop.views import home, signup, login_user, logout_user

urlpatterns = [
    path('', home, name='home'),
    path('signup', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
