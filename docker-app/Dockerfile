FROM nginx:latest

LABEL MAINTAINER=james

CMD ["nginx", "-g", "daemon off;"]

FROM node:latest

COPY /d/User/Jem/Python/tech_230/tech230-cicd-with-jenkins/app/ ./

WORKDIR /app

RUN npm install

EXPOSE 3000

CMD ["npm","start"]