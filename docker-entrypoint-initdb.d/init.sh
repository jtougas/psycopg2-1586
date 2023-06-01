#!/bin/bash

PG_MODE_ARGS_ROOT=(--echo-all --variable=ON_ERROR_STOP=1 --username "$POSTGRES_USER")
psql "${PG_MODE_ARGS_ROOT[@]}" <<-EOSQL
CREATE USER foo PASSWORD 'foo';
CREATE DATABASE foo;
EOSQL