FROM postgres:13

# Copia los scripts SQL
COPY sql/ /docker-entrypoint-initdb.d/