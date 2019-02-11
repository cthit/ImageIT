FROM postgres:latest

ENV POSTGRES_PASSWORD password
ENV POSTGRES_USER imageit
ENV POSTGRES_DB imageit

COPY tables.sql /docker-entrypoint-initdb.d/10-init.sql