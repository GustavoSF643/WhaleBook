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

### **Rotas**

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


## **Testes**
Para rodar os testes, basta digitar o seguinte no terminal:

```
python manage.py test
```

## **Tecnologias utilizadas 📱**
- Django
- Django Rest Framework
- SQLite3

## **Licence**
MIT