FROM gliderlabs/alpine:3.3

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

WORKDIR /app

ONBUILD COPY . /app
ONBUILD RUN pip install -r requirements.txt

CMD ["python", "select_products_database.py"]