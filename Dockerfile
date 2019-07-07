FROM alpine:3.10

LABEL maintainer="yyu <yyu [at] mental.poker>"

ENV PERSISTENT_DEPS \
    python \
    py-pip

RUN apk upgrade --update

# Install basic dependencies
RUN apk add --no-cache --virtual .persistent-deps $PERSISTENT_DEPS

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm requirements.txt

RUN mkdir /workdir

COPY app.py /workdir

WORKDIR /workdir

CMD ["/bin/sh", "-c", "python app.py"]
