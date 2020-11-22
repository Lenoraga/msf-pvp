FROM node:12 as build-stage

ADD package.json /tmp/package.json
RUN cd /tmp && npm install
RUN npm install -g @quasar/cli

RUN mkdir -p /app && cp -a /tmp/node_modules /app
WORKDIR /app


ADD . /app

RUN quasar build



FROM nginx
COPY --from=build-stage /app/dist/spa /usr/share/nginx/html


EXPOSE 80 443