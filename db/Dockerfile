FROM postgres:14

ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_DB=ecommerce

COPY init.sql /docker-entrypoint-initdb.d/

