#! /bin/bash

docker images | grep bhsearch
if [[ $(echo $?) -eq 1 ]]
then
	docker build --no-cache -t bhsearch:test --force-rm -f Dockerfile .
else
	echo "The test image already is readily available"
fi
