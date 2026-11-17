# Node-RED met FlowFuse Dashboard al in de image.
#
# Let op: compose.yaml gebruikt deze Dockerfile NIET. Daar draaien we de
# officiele Node-RED image en installeren we het dashboard via de palette
# manager (het blijft bewaard in het node-red-data volume).
#
# Deze Dockerfile houden we bij voor CI/CD: GitHub Actions kan hiermee een
# image bouwen en pushen, zodat de demo-VM niets manueel moet installeren.
# Lokaal zelf bouwen en testen:
#   docker build -t pdp-node-red:local ./node-red

FROM ghcr.io/node-red/node-red:5.0.9

# WORKDIR is /usr/src/node-red; nodes hier komen in NODE_PATH terecht
RUN npm install --no-audit --no-fund --no-update-notifier @flowfuse/node-red-dashboard
