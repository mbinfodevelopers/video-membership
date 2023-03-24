# base image
FROM node:lts-alpine

# set working directory
WORKDIR /app

# install app dependencies
COPY package*.json ./
RUN npm install

# copy app files
COPY . .

# build for production with minification
RUN npm run build

# expose port 8080
EXPOSE 8080

# start the app
CMD [ "npm", "run", "start" ]
