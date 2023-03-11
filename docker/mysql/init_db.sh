#!/bin/bash

mysql -u root --password=""  << EOF
USE ${MYSQL_DATABASE};
GRANT ALL PRIVILEGES ON  test_${MYSQL_DATABASE}.* TO '${MYSQL_USER}';
EOF
