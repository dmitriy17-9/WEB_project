from requests import get, post, delete

print('Genres:')
print(get('http://localhost:8080/api/v2/genres').json())

print(post('http://localhost:8080/api/v2/genres', json={'name': 'Рассказ',
                                                       'is_for_kids': True}))

print(get('http://localhost:8080/api/v2/genres/1').json())

print(get('http://localhost:8080/api/v2/genres/999').json())

print(delete('http://localhost:8080/api/v2/genres/13').json())

print(delete('http://localhost:8080/api/v2/genres/999').json())

print('-----------------')

print('Books:')
print(get('http://localhost:8080/api/v2/books').json())

print(post('http://localhost:8080/api/v2/books', json={'name': 'Мастер и Маргарита',
                                                       'author': 'М. И. Булгаков',
                                                       'genre_id': 5,
                                                       'file': 'static/pdf/Master_i_margarita.pdf',
                                                       'cover': 'static/img/Master_i_margarita.png'}))

print(get('http://localhost:8080/api/v2/books/4').json())

print(get('http://localhost:8080/api/v2/books/999').json())

print(delete('http://localhost:8080/api/v2/books/4').json())

print(delete('http://localhost:8080/api/v2/books/999').json())

print('-----------------')

print('Users:')
print(get('http://localhost:8080/api/v2/users').json())

print(post('http://localhost:8080/api/v2/users', json={'name': 'da',
                                                       'about': 'net',
                                                       'email': 'email@ya.ru',
                                                       'position': 'user',
                                                       'hashed_password': '123'
                                                       }))

print(get('http://localhost:8080/api/v2/users/5').json())

print(get('http://localhost:8080/api/v2/users/999').json())

print(delete('http://localhost:8080/api/v2/users/11').json())

print(delete('http://localhost:8080/api/v2/users/999').json())