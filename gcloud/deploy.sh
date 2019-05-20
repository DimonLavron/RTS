#!/bin/bash

set -e

docker tag rts_script gcr.io/${PROJECT_PROD}/${SCRIPT_IMAGE}:$TRAVIS_COMMIT
docker tag rts_site gcr.io/${PROJECT_PROD}/${SITE_IMAGE}:$TRAVIS_COMMIT
docker tag mongo gcr.io/${PROJECT_PROD}/${MONGO_IMAGE}:$TRAVIS_COMMIT
docker tag eclipse-mosquitto gcr.io/${PROJECT_PROD}/${MQTT_IMAGE}:$TRAVIS_COMMIT

gcloud --quiet config set project $PROJECT_PROD
gcloud --quiet config set container/cluster $CLUSTER
gcloud --quiet config set compute/zone ${ZONE}

gcloud docker -- push gcr.io/${PROJECT_PROD}/${SCRIPT_IMAGE}
gcloud docker -- push gcr.io/${PROJECT_PROD}/${SITE_IMAGE}
gcloud docker -- push gcr.io/${PROJECT_PROD}/${MONGO_IMAGE}
gcloud docker -- push gcr.io/${PROJECT_PROD}/${MQTT_IMAGE}

yes | gcloud beta container images add-tag gcr.io/${PROJECT_PROD}/${SCRIPT_IMAGE}:$TRAVIS_COMMIT gcr.io/${PROJECT_PROD}/${SCRIPT_IMAGE}:latest
yes | gcloud beta container images add-tag gcr.io/${PROJECT_PROD}/${SITE_IMAGE}:$TRAVIS_COMMIT gcr.io/${PROJECT_PROD}/${SITE_IMAGE}:latest
yes | gcloud beta container images add-tag gcr.io/${PROJECT_PROD}/${MONGO_IMAGE}:$TRAVIS_COMMIT gcr.io/${PROJECT_PROD}/${MONGO_IMAGE}:latest
yes | gcloud beta container images add-tag gcr.io/${PROJECT_PROD}/${MQTT_IMAGE}:$TRAVIS_COMMIT gcr.io/${PROJECT_PROD}/${MQTT_IMAGE}:latest

kubectl set image deployment/${SITE_DEPLOYMENT} ${SITE_CONTAINER}=gcr.io/${PROJECT_PROD}/${SITE_IMAGE}:$TRAVIS_COMMIT
kubectl set image deployment/${SCRIPT_DEPLOYMENT} ${SCRIPT_CONTAINER}=gcr.io/${PROJECT_PROD}/${SCRIPT_IMAGE}:$TRAVIS_COMMIT
kubectl set image deployment/${MONGO_DEPLOYMENT} ${MOBGO_CONTAINER}=gcr.io/${PROJECT_PROD}/${MONGO_IMAGE}:$TRAVIS_COMMIT
kubectl set image deployment/${MQTT_DEPLOYMENT} ${MQTT_CONTAINER}=gcr.io/${PROJECT_PROD}/${MQTT_IMAGE}:$TRAVIS_COMMIT
