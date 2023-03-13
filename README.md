# ProductBackend

## setup instructions
```
git clone https://github.com/doddahulugappa/ProductBackend.git

cd ProductBackend 
```

create .env file and paste the data from sample env by updating blank variables
and default one use as it is

```

docker compose build

docker compose up -d

docker ps -a

```
In case if required execute following steps to do
```

docker exec -it api_container python manage.py makemigrations

docker exec -it api_container python manage.py migrate

docker exec -it api_container python manage.py createsuperuser

```

# Usage Guide
- Open the url in any browser (http://HOST/api-docs)
- register user using /register/ endpoint
- get JWT token by passing username & password using /token/ endpoint
- Authorise using JWT token like below while pasting token in the box
`Bearer <JWTTOKEN>`
- explore all other endpoints 
- http://HOST/api-docs

Explore other urls
- http://HOST
- http://HOST/admin


## Assumptions
- git is installed and working
- docker is installed and working
- port 80 inbound connection allowed for the server
- cart completed means cart checkout done and made payment
- keeping above point in mind , updated stock count and deleted cart using post save signal
- every time user adds items to cart, there is stock check using pre save signal 
- everyday @ 8am mail sending to eligible accounts
- images made specific size & thumbnail size post uploading and stored in same path appending -thumb , -full to image 
name




