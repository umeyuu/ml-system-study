# MLflow racking API よりコード部分引用
# https://www.mlflow.org/docs/latest/quickstart.html
import os
from random import randint, random

from mlflow import log_artifacts, log_metric, log_param

if __name__ == "__main__":
    # パラメータ（キーと値のペア）を記録する
    log_param("param1", randint(0, 100))

    # 指標を記録し、実行中に指標を更新することが可能（ MLflowに記録）
    log_metric("foo", random())
    log_metric("foo", random() + 1)
    log_metric("foo", random() + 2)

    # アーティファクト（出力ファイル）のログ
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open("outputs/test.txt", "w") as f:
        f.write("hello world!")
    log_artifacts("outputs") # フォルダごと記録