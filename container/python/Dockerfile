FROM python:3.12

WORKDIR /user/src/python

# pipのアップデート
RUN pip install --upgrade pip

# pipでインストールしたいモジュールをrequirements.txtに記述しておいて、
# コンテナ内でpipにインストールさせる
# requirements.txtの書き方は[pip freeze]コマンドから参考に出来る
COPY container/python/requirements.txt /tmp/requirements.txt
COPY container/python/entrypoint.sh /tmp/entrypoint.sh
COPY container/python/lib-update.sh /tmp/lib-update.sh
RUN pip install -r /tmp/requirements.txt

COPY ./src /user/src/python

EXPOSE 80
CMD ["sh", "/tmp/entrypoint.sh"]