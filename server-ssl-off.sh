#!/bin/bash

set -euo pipefail

THIS_FILE=${BASH_SOURCE[0]}
THIS_FILE_REAL=$(realpath "$THIS_FILE")
THIS_FILE_REAL_DIR=$(dirname "$THIS_FILE_REAL")

docker run --rm \
    --shm-size=256MB \
    -p 5432:5432 \
    -v "$THIS_FILE_REAL_DIR"/conf:/etc/postgres \
    -v "$THIS_FILE_REAL_DIR"/docker-entrypoint-initdb.d:/docker-entrypoint-initdb.d \
    -u postgres \
    -e POSTGRES_PASSWORD=password \
    "postgres:15.2" \
    -c 'config_file=/etc/postgres/postgresql-ssl-off.conf'