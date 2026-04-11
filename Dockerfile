FROM nginx:1.27-alpine

WORKDIR /usr/share/nginx/html

COPY ["index.html", "styles.css", "Frame 48096189.jpg", "QR.png", "/usr/share/nginx/html/"]

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD wget -q -O /dev/null http://127.0.0.1/ || exit 1
