FROM alpine:latest

RUN apk update && apk add --no-cache python3 py3-pip py3-dateutil nano curl openrc nginx gcc make \
libffi-dev libevent-dev build-base py3-cryptography mariadb-dev musl-dev python3-dev npm && \
mkdir -p /home/ebube/Documents && rc-update add nginx default

COPY CandidateSearch/ /home/ebube/Documents/CandidateSearch
COPY requirements.txt /home/ebube/Documents
COPY bhSearch.conf /etc/nginx/conf.d/
COPY startServices.sh /home/ebube/Documents/CandidateSearch/backend

RUN chmod 775 -R /home/ebube/Documents && rm /etc/nginx/conf.d/default.conf && \
mkdir -p /etc/nginx/sites-enabled && ln -s /etc/nginx/conf.d/bhSearch.conf /etc/nginx/sites-enabled && \
python3 -m pip install setuptools configparser && \
python3 -m pip install -r /home/ebube/Documents/requirements.txt && \
cd /home/ebube/Documents/CandidateSearch/frontend && npm install && \
rm -rf /home/ebube/Documents/CandidateSearch/frontend/node_modules/babel-preset-es201*

WORKDIR /home/ebube/Documents/CandidateSearch/backend
CMD /home/ebube/Documents/CandidateSearch/backend/startServices.sh
