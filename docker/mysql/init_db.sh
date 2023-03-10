#!/bin/bash

mysql -u ${MYSQL_USER} --password=''  << EOF
USE mysql;
UPDATE user set Host='${MYSQL_ROOT_HOST}' where User='${MYSQL_USER}';
COMMIT;
CREATE DATABASE IF NOT EXISTS ${MYSQL_DATABASE};
USE ${MYSQL_DATABASE};
GRANT ALL PRIVILEGES ON *.* TO ${MYSQL_USER}@localhost IDENTIFIED BY '' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON  test_${MYSQL_DATABASE}.* TO '${MYSQL_USER}';
EOF
