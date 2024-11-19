# topアプリのマッピング処理

# Django内のpath機能を追加する
from django.urls import path

# 現在のフォルダにあるviews.pyファイルを参照する
from . import views

app_name = 'top'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
]

