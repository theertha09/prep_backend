from django.urls import path
from .views import MetaTagsAboutUsListCreateAPIView,MetaTagsAboutUsRetrieveUpdateDestroyAPIView,QuestionListView,SubmitResponseView,QuestionCreateView,OptionCreateView,UserResponseListView,QuestionRetrieveUpdateDestroyAPIView,OptionretrieveUpdateDestoyView

urlpatterns = [
    path('aboutmeta/',MetaTagsAboutUsListCreateAPIView.as_view(),name="about-meta-list-create"),
    path('aboutmeta/<int:pk>/',MetaTagsAboutUsRetrieveUpdateDestroyAPIView.as_view(),name="about-meta-retrieve-update-destroy"),
    path("questions/", QuestionListView.as_view(), name="question-list"),
    path("question/<int:pk>/",QuestionRetrieveUpdateDestroyAPIView.as_view(),name="question-update-destroy"),
    path("create-question/", QuestionCreateView.as_view(), name="create-question"),
    path("create-option/", OptionCreateView.as_view(), name="create-option"),
    # path("options/", OptionRetrieveAPIView.as_view(), name="option-list"),
    path("option/<int:pk>/", OptionretrieveUpdateDestoyView.as_view(), name="option-retrieve-update-destroy"),
    path("submit-response/", SubmitResponseView.as_view(), name="submit-response"),
    path("user-responses/", UserResponseListView.as_view(), name="user-responses"),

]