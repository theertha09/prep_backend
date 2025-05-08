from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.FormListCreateAPIView.as_view(), name='form-list-create'),
    path('form/<uuid:uuid>/', views.FormRetrieveUpdateDestroyAPIView.as_view(), name='form-retrieve-update-destroy'),
    
    path('userform/', views.UserformListCreateAPIView.as_view(), name='userform-list-create'),
    path('userform/<uuid:uuid>/', views.UserformRetrieveUpdateDestroyAPIView.as_view(), name='userform-retrieve-update-destroy'),

    path('create-order/', views.CreateOrderAPIView.as_view(), name='create-order'),  # <== fix here
    path('verify-payment/', views.VerifyPaymentAPIView.as_view(), name='verify-payment'),  # <== fix here

    path('courses/', views.courseListCreateAPIView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/',views. courseRetrieveUpdateDestroyAPIView.as_view(), name='course-detail'),
    path('payments/',views.PaymentListAPIView.as_view(), name='payment-list'),

    # SubjectCategory endpoints
    path('subjects/', views.SubjectCategoryListCreateAPIView.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>/',views. SubjectCategoryRetrieveUpdateDestroyAPIView.as_view(), name='subject-detail'),
    path('sections/', views.SectionCategoryListCreateAPIView.as_view(), name='section-list-create'),
    path('sections/<int:pk>/',views. SectionCategoryRetrieveUpdateDestroyAPIView.as_view(), name='section-detail'),

]