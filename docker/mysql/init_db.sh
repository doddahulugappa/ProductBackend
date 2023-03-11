#!/bin/bash

mysql -u root --password="${DATABASE_PASSWORD}"  << EOF
USE ${DATABASE_NAME};
GRANT ALL PRIVILEGES ON  test_${DATABASE_NAME}.* TO '${DATABASE_USER}';
EOF
