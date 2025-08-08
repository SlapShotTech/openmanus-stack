FROM node:18-alpine
WORKDIR /app

# Only copy the package manifest(s) – a lockfile isn't required
# and the build should not fail if one isn't present.
COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

EXPOSE 3000
CMD ["npm", "start"]
