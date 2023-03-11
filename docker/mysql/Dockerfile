FROM mysql/mysql-server:8.0


RUN chown mysql:mysql /var/run/mysqld

RUN mkdir -p /Users/me/docker/mysql/data
RUN chmod -R 777 /Users/me/docker/mysql/data


COPY ./docker/mysql/init_db.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/init_db.sh
