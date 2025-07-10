from django.urls import path

from . import views


# Wire up our API using automatic URL routing., basename='QandA'
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('qa/', views.QandAView.as_view(), name='qa'),
    path('qas/', views.PremiumWebsiteView.as_view(), name='qas'),
    path('content-generator/', views.WebsiteContentGenerator.as_view(), name='content-generator'),
]