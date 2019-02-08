FROM postgres:9.6

COPY scripts/create_phones_user.sh /docker-entrypoint-initdb.d/10-create_user.sh
COPY scripts/create_phones_db.sh /docker-entrypoint-initdb.d/20-create_db.sh
