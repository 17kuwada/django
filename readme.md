# Django プロジェクト

前提条件
1.前提条件 django機能がインストールされた仮想環境が存在する

→ターミナルで pip listを実行し「Django 5.1.1」が一覧にあること

2.VScodeで作業フォルダを開いている

## プロジェクトを作成する

django-admin.exe startproject private_diary

## アプリを作成する

1.プロジェクトフォルダへ移動する
cd private_diary

2.アプリを作成する
python manage.py startapp diary