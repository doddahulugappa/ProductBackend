# ProductBackend

## setup
```
git clone https://github.com/doddahulugappa/ProductBackend.git

cd ProductBackend

docker compose build

docker compose up -d

docker ps -a

docker exec -it api_container python manage.py makemigrations

docker exec -it api_container python manage.py migrate

docker exec -it api_container python manage.py createsuperuser

```

# Usage Guide
- Open the url in any browser (http://HOST/api-docs)
- get JWT token by passing username & password 
- Authorise using JWT token 
`Bearer <JWTTOKEN>`
- explore all other endpoints 

## Assumptions
- cart completed means cart checkout done and made payment
- keeping above point in mind , updated stock count and deleted cart using post save signal
- every time user adds items to cart, there is stock check using presave signal 
- everyday @ 8am mail sending to eligible accounts
- images made specific size & thumbnail size post uploading and stored in same path appending -thumb , -full to image 
name



