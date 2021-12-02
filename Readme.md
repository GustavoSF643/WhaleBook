# **WhaleBook (Capstone Django)**


# **Como instalar e rodar? 🚀**

Para instalar o sistema, é necessário seguir alguns passos, como baixar o projeto e fazer instalação das dependências. Para isso, é necessário abrir uma aba do terminal e digitar o seguinte:

# Este passo é para baixar o projeto
```
git clone https://gitlab.com/<your_user>/q4-capstone_django.git
```

Depois que terminar de baixar, é necessário entrar na pasta, criar um ambiente virtual e entrar nele:

## Entrar na pasta

```
cd q4-capstone_django
```

## Criar um ambiente virtual

```
python3 -m venv venv
```


## Entrar no ambiente virtual

```
source venv/bin/activate
```

Então, para instalar as dependências, basta:

```
pip install -r requirements.txt
```

Depois de ter instalado as dependências, é necessário rodar as migrations para que o banco de dados e as tabelas sejam criadas:
```
./manage.py migrate
```

Então, para rodar, basta digitar o seguinte, no terminal:

```
./manage.py runserver
```

E o sistema estará rodando em http://127.0.0.1:8000/

### **Utilização** 🖥️

Para utilizar este sistema, é necessário utilizar um API Client, como o Insomnia

## **Rotas**

#### **POST /api/accounts/**


Rota para criação de usuários.

```
RESPONSE STATUS -> HTTP 201 (created)
```

Body:
```
{
    "username": "user",
    "email": "example@example.com",
    "password": "1234",
} 
```

Response:

```
{
    "id": 1,
    "username": "user",
    "email": "example@example.com"
}
```


#### **POST /api/login/**

Faz a autenticação do usuário.
```
RESPONSE STATUS -> HTTP 200 (ok)
```

Body:
```
{
    "email": "example@example.com",
    "password": "1234"
}
```

Response:
```
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzODQ1ODgxNSwiaWF0IjoxNjM4MzcyNDE1LCJqdGkiOiIzNDk0ODM1ZGRjNjk0NWIwODRlMzY4ZjVjYjY1Y2RiMCIsInVzZXJfaWQiOjEsInVzZXIiOiJ0ZXN0ZSJ9.2Llf9KgxjtV7jU0_2c0FjOpsPRniB61b2bv3cImuYQc",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM4Mzc2MDE1LCJpYXQiOjE2MzgzNzI0MTUsImp0aSI6IjM2ZTk5ZWU1MjRkNzRiNGM5YjhmOTA0MTI3Y2JkOGYyIiwidXNlcl9pZCI6MSwidXNlciI6InRlc3RlIn0.p7jierEDDyAoUUShobXK9EehGQ6dFyo6tsMMASohUqc"
}
```


#### **GET /api/user/**
Rota com informações sobre o seu usuário. **(Apenas usuário autenticado)**

```
RESPONSE STATUS -> HTTP 200 (ok)
```


Response:

```
{
  "id": 1,
  "username": "user",
  "email": "example@example.com",
  "is_staff": false,
  "is_superuser": false,
  "books": []
}
```

#### **GET /api/users/**
Rota para listagem de usuários.

```
RESPONSE STATUS -> HTTP 200 (ok)
```

Response:
```
[
  {
    "id": 1,
    "username": "user",
    "email": "example@example.com",
    "is_staff": false,
    "is_superuser": false,
    "books": []
  },
  {
    "id": 2,
    "username": "user2",
    "email": "example2@example.com",
    "is_staff": false,
    "is_superuser": false,
    "books": []
  }
]
```

#### **GET /api/users/\<int:user_id>/**
Rota para obter informações de um usuário.

```
RESPONSE STATUS -> HTTP 200 (ok)
```

Response:
```
{
  "id": 1,
  "username": "user",
  "email": "example@example.com",
  "is_staff": false,
  "is_superuser": false,
  "is_active": true
}
  
```

#### **POST /api/user/books/**
Rota para vincular livros ao usuário.

```
RESPONSE STATUS -> HTTP 201 (created)
```

Body:
```
{
	"title": "O que é o SUS",
	"book_url": "/api/books/5unrAgAAQBAJ/",
	"image_url": "http://books.google.com/books/publisher/content?id=5unrAgAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&imgtk=AFLRE73Oh67GC3JDW_YrZbK",
	"total_pages": 148,
	"is_favorite": true
}
```

Response:
```
{
  "id": 1,
  "book_url": "/api/books/5unrAgAAQBAJ/",
  "image_url": "http://books.google.com/books/publisher/content?id=5unrAgAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&imgtk=AFLRE73Oh67GC3JDW_YrZbK",
  "title": "O que é o SUS",
  "total_pages": 148,
  "current_page": 0,
  "is_favorite": true,
  "is_reading": false,
  "read": false,
  "user": 1
}
```

#### **GET /api/user/books/**
Rota para listar os livros vinculados ao usuário.

```
RESPONSE STATUS -> HTTP 200 (ok)
```

Response:
```
[
  {
    "id": 1,
    "book_url": "/api/books/5unrAgAAQBAJ/",
    "image_url": "http://books.google.com/books/publisher/content?id=5unrAgAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&imgtk=AFLRE73Oh67GC3JDW_YrZbK",
    "title": "O que é o SUS",
    "total_pages": 148,
    "current_page": 0,
    "is_favorite": true,
    "is_reading": false,
    "read": false,
    "user": 1
  }
]
```

#### **GET /api/user/books/\<int:book_id>/**
Rota para obter informações de um livro vinculado ao usuário.
```
RESPONSE STATUS -> HTTP 200 (ok)
```

Response:
```
{
  "id": 1,
  "book_url": "/api/books/5unrAgAAQBAJ/",
  "image_url": "http://books.google.com/books/publisher/content?id=5unrAgAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&imgtk=AFLRE73Oh67GC3JDW_YrZbK",
  "title": "O que é o SUS",
  "total_pages": 148,
  "current_page": 0,
  "is_favorite": true,
  "is_reading": false,
  "read": false,
  "user": 1
}
```
#### **PATCH /api/user/books/\<int:book_id>/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

#### **DELETE /api/user/books/\<int:book_id>/**

#### **POST /api/user/friends/requests/\<int:user_id>/**

```
RESPONSE STATUS -> HTTP 201 (created)
```

#### **GET /api/user/friends/requests/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

#### **DELETE /api/user/friends/requests/\<int:user_id>/**

```
RESPONSE STATUS -> HTTP 204 (No content)
```

#### **POST /api/user/friends/\<int:user_id>/**

```
RESPONSE STATUS -> HTTP 201 (created)
```

#### **GET /api/user/friends/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

#### **DELETE /api/user/friends/\<int:user_id>/**

```
RESPONSE STATUS -> HTTP 204 (No content)
```

#### **GET /api/user/reviews/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

#### **POST /api/groups/**

```
RESPONSE STATUS -> HTTP 201 (created)
```

#### **GET /api/groups/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

#### **GET /api/groups/\<int:group_id>/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

#### **POST /api/groups/\<int:group_id>/subscription/**

```
RESPONSE STATUS -> HTTP 201 (created)
```

#### **GET /api/groups/\<int:group_id>/request_users/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

#### **GET /api/groups/my_groups/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

#### **POST /api/groups/\<int:group_id>/accept_member/\<int:user_id>/**

```
RESPONSE STATUS -> HTTP 201 (created)
```

#### **GET /groups/\<int:group_id>/members/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

#### **DELETE /api/groups/\<int:group_id>/remove_member/\<int:user_id>/**

```
RESPONSE STATUS -> HTTP 204 (No content)
```

#### **POST /api/groups/\<int:group_id>/goals/**

```
RESPONSE STATUS -> HTTP 201 (created)
```

#### **POST /api/groups/\<int:group_id>/goals/update_status/**

```
RESPONSE STATUS -> HTTP 201 (created)
```

#### **POST /api/groups/\<int:group_id>/goals/join/**

```
RESPONSE STATUS -> HTTP 201 (created)
```

#### **GET /api/groups/\<int:group_id>/goals/members/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

#### **DELETE /api/groups/\<int:group_id>/goals/leave/**

```
RESPONSE STATUS -> HTTP 204 (No content)
```

#### **GET /api/books/?q=search+terms**
Rota para listagem de livros, seguindo a api do google disponível em https://developers.google.com/books/docs/v1/using

```
RESPONSE STATUS -> HTTP 200 (ok)
```


#### **GET /api/books/\<str:book_id>/**
Rota para obter informações de um livro pelo id.

```
RESPONSE STATUS -> HTTP 200 (ok)
```

#### **POST /api/books/\<str:book_id>/reviews/**

```
RESPONSE STATUS -> HTTP 201 (created)
```

#### **GET /api/books/\<str:book_id>/reviews/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

#### **GET /api/books/\<str:book_id>/reviews/\<int:review_id>/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

#### **PATCH /api/books/\<str:book_id>/reviews/\<int:review_id>/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

#### **DELETE /api/books/\<str:book_id>/reviews/\<int:review_id>/**

```
RESPONSE STATUS -> HTTP 204 (No content)
```


## **Testes**
Para rodar os testes, basta digitar o seguinte no terminal:

```
TEST=TEST python manage.py test
```

## **Tecnologias utilizadas 📱**
- Django
- Django Rest Framework
- PostgreSQL

## **Licence**
MIT