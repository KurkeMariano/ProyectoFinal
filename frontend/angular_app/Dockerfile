# frontend/Dockerfile
FROM node:16

WORKDIR /app

# Copiar el package.json y el package-lock.json
COPY package*.json ./

# Instalar las dependencias
RUN npm install

# Copiar el código fuente
COPY ./src /app/src

# Construir la aplicación Angular
RUN npm run build

# Exponer el puerto para el servidor de desarrollo
EXPOSE 4200

# Comando para iniciar el servidor de desarrollo de Angular
CMD ["npm", "start"]
