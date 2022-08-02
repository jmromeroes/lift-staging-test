FROM ubuntu

USER root

RUN apt install -y \
    curl \
    jq \
    less

WORKDIR /app/

COPY file.txt .

CMD [ "jq" ]