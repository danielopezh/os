FROM node:23-alpine

WORKDIR /app

# Copiar solo lo necesario desde la etapa de build
COPY package*.json ./
COPY dist ./dist

# Instalar solo dependencias de producción
RUN npm install --only=production

# Exponer el puerto del servidor
EXPOSE 3000

# Comando para iniciar el servidor
CMD ["node", "dist/server.js"]