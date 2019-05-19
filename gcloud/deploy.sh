#!/bin/bash

set -e

# docker build -t gcr.io/${PROJECT_PROD}/${SCRIPT_IMAGE}:$TRAVIS_COMMIT -f script/Dockerfile .
# docker build -t gcr.io/${PROJECT_PROD}/${SITE_IMAGE}:$TRAVIS_COMMIT -f site/Dockerfile .

docker tag rts_script gcr.io/${PROJECT_PROD}/${SCRIPT_IMAGE}:$TRAVIS_COMMIT
docker tag rts_site gcr.io/${PROJECT_PROD}/${SITE_IMAGE}:$TRAVIS_COMMIT
dcoker tag mongo gcr.io/${PROJECT_PROD}/${MONGO_IMAGE}:$TRAVIS_COMMIT
docker tag eclipse-mosquitto gcr.io/${PROJECT_PROD}/${MQTT_IMAGE}:$TRAVIS_COMMIT

echo $GCLOUD_SERVICE_KEY_TEST | base64 --decode -i > ${HOME}/client-secret.json
gcloud auth activate-service-account --key-file ${HOME}/client-secret.json

gcloud --quiet config set project $PROJECT_PROD
# gcloud --quiet config set container/cluster $CLUSTER
gcloud --quiet config set compute/zone ${ZONE}
# gcloud --quiet container clusters get-credentials $CLUSTER

gcloud docker -- push gcr.io/${PROJECT_PROD}/${SCRIPT_IMAGE}
gcloud docker -- push gcr.io/${PROJECT_PROD}/${SITE_IMAGE}
gcloud docker -- push gcr.io/${PROJECT_PROD}/${MONGO_IMAGE}
gcloud docker -- push gcr.io/${PROJECT_PROD}/${MQTT_IMAGE}

yes | gcloud beta container images add-tag gcr.io/${PROJECT_PROD}/${SCRIPT_IMAGE}:$TRAVIS_COMMIT gcr.io/${PROJECT_PROD}/${SCRIPT_IMAGE}:latest
yes | gcloud beta container images add-tag gcr.io/${PROJECT_PROD}/${SITE_IMAGE}:$TRAVIS_COMMIT gcr.io/${PROJECT_PROD}/${SITE_IMAGE}:latest
yes | gcloud beta container images add-tag gcr.io/${PROJECT_PROD}/${MONGO_IMAGE}:$TRAVIS_COMMIT gcr.io/${PROJECT_PROD}/${MONGO_IMAGE}:latest
yes | gcloud beta container images add-tag gcr.io/${PROJECT_PROD}/${MQTT_IMAGE}:$TRAVIS_COMMIT gcr.io/${PROJECT_PROD}/${MQTT_IMAGE}:latest
