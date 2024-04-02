#!/bin/bash
docker run -e "IMAGE_SERVICE_HOST=http://178.154.220.122:7777" -v $PWD:/app -p 8080:8080 ds-backend
