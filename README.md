# Private Diary
専用の日記アプリをDjangoで作成した。  
[参照の本](https://www.amazon.co.jp/%E5%8B%95%E3%81%8B%E3%81%97%E3%81%A6%E5%AD%A6%E3%81%B6-Python-Django%E9%96%8B%E7%99%BA%E5%85%A5%E9%96%80-NEXT-ONE/dp/4798162507/ref=asc_df_4798162507/?tag=jpgo-22&linkCode=df0&hvadid=343222257571&hvpos=&hvnetw=g&hvrand=15851572609106809943&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1009718&hvtargid=pla-848852189750&psc=1&th=1&psc=1)

## 環境
* Python 3.7
* Django 2.2.2
* PostgreSQL 10.14
* psycopg2-binary 2.8.6
* pillow 7.2.0
* django-auth 0.39.1
* selenium 3.141.0 (テストに使う)
* ChromeDriver 85.0.4183.87 (google chromのバージョンに合わせる)

## DataBaseの設定
[こちらを参照](https://qiita.com/kanzaki0507/items/12a2ef0b778250d699bd)
今回はpostgresql@10を使用したのでインストールするときは@10をつける。

    $ pip install postgresql@10

## Web Serverを動かす
    $ python manage.py --settings private_diary.settings_dev