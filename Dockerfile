FROM nginx:1.27-alpine

WORKDIR /usr/share/nginx/html

COPY ["index.html", "./"]
COPY ["styles.css", "./"]
COPY ["Frame 48096189.jpg", "./"]
COPY ["Group 48096177.jpg", "./"]
COPY ["Group 48096185.jpg", "./"]
COPY ["QR.png", "./"]
COPY ["favicon.png", "./"]
COPY ["web/", "./web/"]

EXPOSE 80
