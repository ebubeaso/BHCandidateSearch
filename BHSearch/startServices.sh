#! /bin/sh

openrc default && sleep 1 && \
cd /home/ebube/Documents/CandidateSearch/backend && \
gunicorn -w 3 -b 0.0.0.0:5555 backend:app
