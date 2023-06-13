# decide which base image to use
FROM nginx:latest

# ensure to use official image
LABEL MAINTAINER=james

# copy data index
COPY index.html /usr/share/nginx/html

# required port, expos 80 (80 is default)
EXPOSE 80

# launch the app/server
CMD ["nginx", "-g", "daemon off;"]