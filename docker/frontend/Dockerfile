FROM node:latest

WORKDIR /code/frontend/

COPY package*.json /code/frontend/
RUN npm install
RUN npm audit --production
COPY . /code/frontend/

CMD ["bash", "-c", "npm start"]

