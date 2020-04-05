# Stage 0, build json from python
FROM python:3.7 as data-stage
WORKDIR /data
COPY ./scraper /data/scraper
RUN pip install -r ./scraper/requirements.txt
WORKDIR /data/scraper
RUN python ./index.py

# Stage 1, "build-stage", based on Node.js, to build and compile the frontend
FROM node:10 as build-stage
WORKDIR /app
COPY ./web/package*.json /app/
RUN npm install
COPY ./web /app/
COPY --from=data-stage /data/scraper/src/data.json /app/src/places.json
RUN chmod a+x ./node_modules/.bin/react-scripts
RUN npm run build

# server stage
FROM nginx:1.17.9-alpine as serve-stage
# Copy the default nginx.conf
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY ./fullchain.pem /etc/letsencrypt/live/www.bmore-curbside-map.site/
COPY ./privkey.pem /etc/letsencrypt/live/www.bmore-curbside-map.site/
COPY ./options-ssl-nginx.conf /etc/letsencrypt/
# Copy prod build
COPY --from=build-stage /app/build/ /usr/share/nginx/html