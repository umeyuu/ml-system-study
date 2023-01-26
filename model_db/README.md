# モデル管理 DB
モデルを管理するためのデータベースおよびサービス用 REST API を構築した

## How to use
コンテナを立ち上げる
```
$ docker-compose up -d --build
```
コンテナの停止・破棄を一気にする

```
$ docker-compose down
```

コンテナを起動したら`localhost:8000/docs` をブラウザで開き、モデル DB サービスの起動確認する。

## DB確認

DBコンテナに入る
```
$ docker-compose exec postgres psql -h localhost -U user --dbname=model_db

```
`\dt;`というコマンドでテーブルを確認できる。

```
model_db=# \dt;

          List of relations
 Schema |    Name     | Type  | Owner 
--------+-------------+-------+-------
 public | experiments | table | user
 public | models      | table | user
 public | projects    | table | user
```
