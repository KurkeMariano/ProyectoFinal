-- Crear bases de datos
CREATE DATABASE database1;
CREATE DATABASE database2;
CREATE DATABASE database3;

-- Crear usuarios y asignarles permisos
CREATE USER user1 WITH ENCRYPTED PASSWORD 'password1';
CREATE USER user2 WITH ENCRYPTED PASSWORD 'password2';
CREATE USER user3 WITH ENCRYPTED PASSWORD 'password3';

-- Otorgar permisos a los usuarios en las bases de datos
GRANT ALL PRIVILEGES ON DATABASE database1 TO user1;
GRANT ALL PRIVILEGES ON DATABASE database2 TO user2;
GRANT ALL PRIVILEGES ON DATABASE database3 TO user3;
