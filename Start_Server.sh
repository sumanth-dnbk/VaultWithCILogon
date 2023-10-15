#!/usr/bin/env bash

# Kills any running vault server.
kill $(ps ax |grep 'vault' |awk '{print $1}') 2>/dev/null
vault server -dev -dev-root-token-id=devroot -log-level=debug