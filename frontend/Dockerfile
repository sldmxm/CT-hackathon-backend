FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./

#RUN npm ci --no-audit --no-fund
RUN npm install

COPY . ./

RUN npm run build

CMD cp -r dist result_build

#FROM nginx:latest AS frontend
#
#RUN rm -rf /usr/share/nginx/html/*
#
#COPY --from=builder /app/dist /usr/share/nginx/html
#
#COPY nginx/conf.d/default.conf /etc/nginx/conf.d
#
#EXPOSE 80
#
#CMD ["nginx", "-g", "daemon off;"]