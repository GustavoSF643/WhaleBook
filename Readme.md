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

Para utilizar este sistema, é necessário utilizar um API Client, como o Insomnia, ou o front-end https://whalebook.vercel.app/

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

#### **POST /api/refresh/**

Rota para obter o access token a partir do refresh.

```
RESPONSE STATUS -> HTTP 200 (ok)
```

Body:

```
{
	"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzODU0MDMxNCwiaWF0IjoxNjM4NDUzOTE0LCJqdGkiOiJjOTgzYmVhMDg3YmQ0OWI3ODJkMTc3NDA5NThlYWUxYSIsInVzZXJfaWQiOjUsInVzZXIiOiJ0ZXN0ZTUifQ.DVoaoOBdDeNFsUHlDngcp9Vhpt4BlIs5P4UppQav0Pw"
}
```

Response:

```
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM4NDU4NzI4LCJpYXQiOjE2Mzg0NTM5MTQsImp0aSI6ImRlZTMyODQxNGM1NzQyNTE5Y2NmZDk1NTdmMjMxYmYzIiwidXNlcl9pZCI6NSwidXNlciI6InRlc3RlNSJ9.kZCu1OCe7qYuwax9lFf4wmXTp4LKqEIr-vvUkAkDY7M"
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

Rota para vincular livros ao usuário.**(Apenas usuário autenticado)**

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

Rota para listar os livros vinculados ao usuário.**(Apenas usuário autenticado)**

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

Rota para obter informações de um livro vinculado ao usuário.**(Apenas usuário autenticado)**

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

Rota para atualizar informações de um livro vinculado ao usuário.**(Apenas usuário autenticado)**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

Body:

```
{
	"read": true
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
  "read": true,
  "user": 1
}
```

#### **DELETE /api/user/books/\<int:book_id>/**

Rota para deletar um livro vinculado ao usuário.**(Apenas usuário autenticado)**

```
RESPONSE STATUS -> HTTP 204 (No content)
```

#### **POST /api/user/friends/requests/\<int:user_id>/**

Rota para enviar solicitão de amizade para outro usuário.**(Apenas usuário autenticado)**

```
RESPONSE STATUS -> HTTP 201 (created)
```

Response:

```
[
  {
    "friend": 2
  }
]
```

#### **GET /api/user/friends/requests/**

Rota para listar suas solicitações de amizade.**(Apenas usuário autenticado)**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

Response:

```
{
  "sent_requests": [],
  "received_requests": [
    {
      "user": 1
    }
  ]
}
```

#### **DELETE /api/user/friends/requests/\<int:user_id>/**

Rota para deletar um solicitação de amizade recebida.**(Apenas usuário autenticado)**

```
RESPONSE STATUS -> HTTP 204 (No content)
```

#### **POST /api/user/friends/\<int:user_id>/**

Rota para aceitar uma solicitação de amizade.**(Apenas usuário autenticado)**

```
RESPONSE STATUS -> HTTP 201 (created)
```

Response:

```
{
  "message": "Friend added."
}
```

#### **GET /api/user/friends/**

Rota para listar os amigos do usuário.**(Apenas usuário autenticado)**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

Response:

```
[
  {
    "friend": 2
  }
]
```

#### **DELETE /api/user/friends/\<int:user_id>/**

Rota para deletar um amigo da lista de amigos do usuário.**(Apenas usuário autenticado)**

```
RESPONSE STATUS -> HTTP 204 (No content)
```

#### **GET /api/user/reviews/**

Rota para listar os reviews feitos pelo usuário.

```
RESPONSE STATUS -> HTTP 200 (ok)
```

Response:

```
[
  {
    "id": 1,
    "book_id": "5unrAgAAQBAJ",
    "stars": 5,
    "review": "teste"
  }
]
```

#### **POST /api/groups/**

```
RESPONSE STATUS -> HTTP 201 (created)
```

Body:

```
{
  "name": "Novo Grupo",
  "description": "Descrição do grupo"
}
```

Response:

```
{
  {
    "id": 1,
    "leader": {
      "id": 1,
      "username": "new_user"
    },
    "name": "Novo grupo",
    "description": "Descrição do grupo"
  }
}
```

#### **PATCH /api/groups/\<int:group_id>/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

Body:

```
{
	"name": "update_name"
}
```

Response:

```
{
  "id": 2,
  "leader": {
    "id": 1,
    "username": "new_user"
  },
  "name": "update_name",
  "description": "teste"
}
```

#### **GET /api/groups/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

Response:

```
[
  {
    "id": 1,
    "leader": {
      "id": 1,
      "username": "new_user"
    },
    "name": "Novo grupo",
    "description": "Descrição do grupo"
  }
    {
    "id": 2,
    "leader": {
      "id": 2,
      "username": "new_use2"
    },
    "name": "Novo grupo2",
    "description": "Descrição do grupo"
  }
]
```

#### **GET /api/groups/\<int:group_id>/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```
Response:

```
{
  "id": 1,
  "leader": {
    "id": 1,
    "username": "new_user"
  },
  "name": "Novo grupo",
  "description": "Descrição do grupo"
}
```

#### **POST /api/groups/\<int:group_id>/subscription/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

Response:

```
{
  "Message": "Created a request to join the group"
}
```


#### **GET /api/groups/\<int:group_id>/request_users/**

```
RESPONSE STATUS -> HTTP 200 (ok)

```

Response:
```

[
  {
    "user": {
      "id": 2,
      "username": "new_user2"
    }
  },
  {
    "user": {
      "id": 3,
      "username": "new_user3"
    }
  }
]
```

#### **GET /api/groups/my_groups/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

Response:
```
[
  {
    "group": {
      "id": 1,
      "leader": {
        "id": 1,
        "username": "new_user"
      },
      "name": "new1",
      "description": "teste"
    }
  },
  {
    "group": {
      "id": 2,
      "leader": {
        "id": 2,
        "username": "new_user2"
      },
      "name": "grupo teste",
      "description": "Teste"
    }
  }
]
```

#### **POST /api/groups/\<int:group_id>/accept_member/\<int:user_id>/**

```
RESPONSE STATUS -> HTTP 201 (created)
```

Response:
```
{
  "Message": "New member added"
}
```

#### **GET /groups/\<int:group_id>/members/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

Response:

```
[
  {
    "id": 1,
    "username": "new_user"
  },
  {
    "id": 2,
    "username": "new_user2"
  }
]
```

#### **DELETE /api/groups/\<int:group_id>/remove_member/\<int:user_id>/**

```
RESPONSE STATUS -> HTTP 204 (No content)
```

#### **POST /api/groups/\<int:group_id>/goals/**

```
RESPONSE STATUS -> HTTP 201 (created)
```

Body:

```
{
	"book_url": "http://google.api/book/xxxxxxx",
	"title": "novo_goal",
	"image_url": "http://google.api/img/xxxxxxx",
	"description": "teste"
}
```

Response:

```
{
  "id": 2,
  "book_url": "http://google.api/book/xxxxxxx",
  "title": "novo_goal3",
  "image_url": "http://google.api/img/xxxxxxx",
  "deadline": null,
  "description": "teste"
}
```

#### **PATCH /api/groups/\<int:group_id>/goals/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

Body:

```
{
	"title": "update_title"
}
```

Response:

```
{
  "id": 2,
  "book_url": "http://google.api/book/xxxxxxx",
  "title": "update_title",
  "image_url": "http://google.api/img/xxxxxxx",
  "deadline": null,
  "description": "teste"
}
```

#### **POST /api/groups/\<int:group_id>/goals/update_status/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

Response:

```
{
  "Message": "Updated reading status"
}
```

#### **POST /api/groups/\<int:group_id>/goals/join/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

Response:

```
{
  "Message": "Associated with a goal"
}
```

#### **GET /api/groups/\<int:group_id>/goals/members/**

```
RESPONSE STATUS -> HTTP 200 (ok)
```

Response:

```
[
  {
    "id": 1,
    "username": "new_user"
  },
    {
    "id": 2,
    "username": "new_user2"
  }
]
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

Response:

```

[
{
"id": "BBWWAAAAMAAJ",
"selfLink": "/api/books/BBWWAAAAMAAJ/",
"volumeInfo": {
"title": "Using Computers in Legal Research",
"subtitle": "A Guide to LEXIS and WESTLAW",
"authors": [
"Christopher G. Wren",
"Jill Robinson Wren"
],
"pageCount": 815,
"categories": [
"Computers"
],
"imageLinks": {
"smallThumbnail": "http://books.google.com/books/content?id=BBWWAAAAMAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
"thumbnail": "http://books.google.com/books/content?id=BBWWAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
},
"language": "en",
"averageRating": 5.0
}
}
]

```


#### **GET /api/books/\<str:book_id>/**
Rota para obter informações de um livro pelo id.

```

RESPONSE STATUS -> HTTP 200 (ok)

```

Response:
```

{
"id": "5unrAgAAQBAJ",
"selfLink": "https://www.googleapis.com/books/v1/volumes/5unrAgAAQBAJ",
"volumeInfo": {
"title": "O que é o SUS",
"authors": [
"Jairnilson Paim"
],
"description": "A luta pelo direito à saúde e pela consolidação do Sistema Único de Saúde (SUS) brasileiro tem se expressado a partir da articulação de trabalhadores dos campos da saúde, pesquisadores e militantes dos movimentos sociais nas duas últimas décadas. Este livro busca esclarecer o que é, o que não é, o que faz, o que deve fazer e o que pode fazer o SUS. É destinado a todos que estão na luta por uma saúde pública de qualidade, aos trabalhadores do SUS, estudantes, pesquisadores, militantes de movimentos sociais e a sociedade em geral.",
"pageCount": 148,
"categories": [
"Medical / Administration"
],
"imageLinks": {
"smallThumbnail": "http://books.google.com/books/publisher/content?id=5unrAgAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&imgtk=AFLRE71q0tgvjQG3IiHa28BBvWFQPpl1eVfvyrMWneFGOgVJDQLhQvufOwWYGDUYCcQQcZlVuxNrX8o__Mbi_EPb7UQmy9of2z0t5PheighMN7qUG2iye1njrcGLOBT6zakR1iTJPEjw&source=gbs_api",
"thumbnail": "http://books.google.com/books/publisher/content?id=5unrAgAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&imgtk=AFLRE73Oh67GC3JDW_YrZbKswAXCJvHnMgElrZcryRgvvalsLCWgxI_9wwCI7ZWaO5jxV3Quje8QiXl-GLlQG2EGYNr7-dvVsCafCnbY5JzkGS--wAS9cCnD7I6c0NcT6TszInL-NJWP&source=gbs_api"
},
"language": "pt-BR",
"averageRating": 5.0
}
}

```
#### **POST /api/books/\<str:book_id>/reviews/**
Rota para criação de reviews para um livro.**(Apenas usuário autenticado)**
```

RESPONSE STATUS -> HTTP 201 (created)

```

Body:
```

{
"stars": 5,
"review": "teste"
}

```

Response:
```

{
"id": 5,
"user": 1,
"book_id": "nQo8EAAAQBAJ",
"stars": 5,
"review": "teste"
}

```

#### **GET /api/books/\<str:book_id>/reviews/**
Rota para listar os reviews de um livro.
```

RESPONSE STATUS -> HTTP 200 (ok)

```

Response:
```

[
{
"id": 1,
"user": 1,
"book_id": "5unrAgAAQBAJ",
"stars": 5,
"review": "teste"
}
]

```
#### **GET /api/books/\<str:book_id>/reviews/\<int:review_id>/**
Rota para obter informações de um review de um livro.
```

RESPONSE STATUS -> HTTP 200 (ok)

```

Response:
```

{
"id": 1,
"user": 1,
"book_id": "5unrAgAAQBAJ",
"stars": 5,
"review": "teste"
}

```

#### **PATCH /api/books/\<str:book_id>/reviews/\<int:review_id>/**
Rota para atualizar uma review feita para um livro.**(Apenas usuário autenticado)**
```

RESPONSE STATUS -> HTTP 200 (ok)

```

Body:
```

{
"stars": 4,
"review": "teste"
}

```

Response:
```

{
"id": 1,
"user": 1,
"book_id": "5unrAgAAQBAJ",
"stars": 4,
"review": "teste"
}

```

#### **DELETE /api/books/\<str:book_id>/reviews/\<int:review_id>/**
Rota para deletar o review feito para um livro.**(Apenas usuário autenticado)**
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

## **Autores** ✒️

* **Gustavo Silva** - *Tech Leader* - [Gustavo Silva](https://gitlab.com/GustavoSil)
* **Wander Moreira** - *Scrum Master* - [Wander Moreira](https://gitlab.com/trevius)
* **Paulo Mello** - *Product Owner* - [Paulo Mello](https://gitlab.com/pauloraphaelmello)
* **Leomar Romanzini** - *Dev* - [Leomar Romanzini](https://gitlab.com/leomarromanzini)

## **Licence**
MIT
```
