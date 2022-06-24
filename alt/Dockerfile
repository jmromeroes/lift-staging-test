FROM ubuntu

RUN top

USER root

RUN apt-get install python

RUN apt install -y \
    curl \
    jq \
    less

USER root

WORKDIR /app/

COPY file.txt .

CMD [ "jq" ]