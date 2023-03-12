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



