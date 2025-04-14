FROM node:18

WORKDIR /app

COPY package*.json ./

RUN npm install

# Remove build step for development
COPY . .

CMD ["npm", "run", "dev"]
