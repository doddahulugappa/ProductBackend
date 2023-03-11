#!/bin/bash

mysql -u root --password=''  << EOF
USE mysql;
UPDATE user set Host='%' where User='root';
COMMIT;
USE ${MYSQL_DATABASE};
GRANT ALL PRIVILEGES ON *.* TO root@localhost IDENTIFIED BY '' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON  test_${MYSQL_DATABASE}.* TO '${MYSQL_USER}';
EOF
