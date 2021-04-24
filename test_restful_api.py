from requests import get, post, delete

print(get('http://localhost:8080/api/v2/users').json())

print(post('http://localhost:8080/api/v2/users', json={'name': 'uussseerr',
                                                       'about': 'aaaa',
                                                       'email': 'a@ya.ru',
                                                       'position': 'user',
                                                       'hashed_password': 'user123456789'}))

print(get('http://localhost:8080/api/v2/users/1').json())

print(get('http://localhost:8080/api/v2/users/999').json())

print(delete('http://localhost:8080/api/v2/users/10').json())

print(delete('http://localhost:8080/api/v2/users/999').json())
