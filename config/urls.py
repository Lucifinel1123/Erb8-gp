
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls',namespace='pages')),
    path('listings/', include('listings.urls',namespace='listings')),
    path('applies/', include('applies.urls',namespace='applies')),
    path('companies/', include('companies.urls',namespace='companies')),
    path('accounts/', include('accounts.urls',namespace='accounts')),
    path('admin/', admin.site.urls),
]
