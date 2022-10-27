from django.urls import path

from . import views, viewsets

urlpatterns = [
    path("<int:pk>/", views.product_detail_view),
    path("", views.product_list_create_view),
    # path("", views.product_mixin_view),
    path("<int:pk>/delete/", views.product_delete_view),
    path("<int:pk>/update/", views.product_update_view),
    # path("<int:pk>/", views.product_alt_view),
    # path("", views.product_alt_view),
    path("v2/<int:pk>/", viewsets.product_list_view),
    path("v2/<int:pk>/", viewsets.product_detail_view)

]
