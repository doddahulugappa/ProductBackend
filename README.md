# ProductBackend API Project

## Setup instructions
```
git clone https://github.com/doddahulugappa/ProductBackend.git

cd ProductBackend 
```

create .env file and paste the data from sample env by updating blank variables
and default one use as it is

```

docker compose build

docker compose up -d
```
To see all containers status
`docker ps -a`


In case if required execute following steps to do migration and admin user creation
```

docker exec -it api_container python manage.py makemigrations

docker exec -it api_container python manage.py migrate

docker exec -it api_container python manage.py createsuperuser

```

## Usage Guide
- Open the url in any browser (http://HOST/api-docs)
- Register user using /register/ endpoint
- Get JWT token by passing username & password using /token/ endpoint
- Authorise using JWT token like below while pasting token in the box
`Bearer <JWTTOKEN>`
- explore all other endpoints 
- http://HOST/api-docs

Explore other urls
- http://HOST
- http://HOST/admin


## Assumptions
- Git is installed and working
- Docker is installed and working
- Port 80 inbound connection allowed for the server
- Cart completed means cart checkout done and made payment
- Keeping above point in mind , updated stock count and deleted cart using post save signal
- Every time user adds items to cart, there is stock check using pre save signal 
- Everyday @8am mail sending to eligible accounts
- Images made specific size & thumbnail size post uploading and stored in same path appending -thumb , -full to image 
name

## Features

- Product App Rest API's with swagger API browser - Open API specification
- JWT Authentication
- Django admin 
- Docker files and Docker Compose manifest file to deploy all services together
- Celery to handle async/periodic tasks
- Get/Post/Put/Patch/Delete methods for below models
  - Products
  - Category
  - Cart
  - CartItems
- User registration
- Get token & refresh token
- Image upload with Post method for products and saved various sizes of images uploaded like thumbnail , 
specific size images using multiprocessing
- MySQL Database used as backend DB
- Sending mail for the registered user after one day using celery worker & celery beat 
- Pagination for the search results
- Sorting for the search results
- Redis to handle caching and message broker
- API served via Gunicorn - Web server gateway interface
- keys/Secretes/Creds & some important settings handled with environment variables
- Test cases

