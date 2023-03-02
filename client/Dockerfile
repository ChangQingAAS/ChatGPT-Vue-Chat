FROM node:19.7.0

WORKDIR /src/

ADD *.js *.json ./

RUN npm i
ADD public/ ./public/
ADD src/ ./src/

ENTRYPOINT [ "npm", "run"]
CMD ["serve"]
