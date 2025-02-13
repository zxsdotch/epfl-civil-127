FROM node:alpine3.20

EXPOSE 8100

WORKDIR /slidev
COPY package.json package-lock.json .
RUN npm install
RUN apk add python3 py3-pip expect

ENTRYPOINT ["npm", "run", "dev"]
