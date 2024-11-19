# 外部機能を参照する
# from フォルダ/ファイルを指定する
# from 
# 
from django.urls import path

# 同一フォルダ内のviews.pyを参照する
from . import views

app_name = 'diary'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('inquiry/',views.InquiryView.as_view(),name='inquiry'),
]