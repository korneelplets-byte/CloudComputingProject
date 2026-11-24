# Node-RED met FlowFuse Dashboard (Dashboard 2.0) al in de image, zodat een
# nieuwe machine (teamgenoot, demo-VM, CI) niets manueel moet installeren.
#
# Gebouwd via compose.yaml:  docker compose up -d --build node-red
# Of los:                    docker build -t pdp-node-red:local ./node-red

FROM ghcr.io/node-red/node-red:5.0.9

# WORKDIR is /usr/src/node-red; nodes die hier staan laadt Node-RED altijd,
# los van wat er in het /data-volume zit.
RUN npm install --no-audit --no-fund --no-update-notifier @flowfuse/node-red-dashboard
