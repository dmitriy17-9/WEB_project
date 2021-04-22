from requests import get, post, delete

# # Books: get
# print('Books')
# print('get:')
# # получение всех книг
# # корректный запрос
# print(get('http://localhost:8080/api/books').json())
#
# # получение одной книги с существующим id == 1
# # корректный запрос
# print(get('http://localhost:8080/api/book/1').json())
#
# # получение одной книги с несуществующим id == 999
# # некорректный запрос
# print(get('http://localhost:8080/api/book/999').json())
#
# # параметр не типа int
# # некорректный запрос
# print(get('http://localhost:8080/api/book/q').json())
#
# print()
#
# # Books: post
# print('post:')
# # добавление книги
# # корректный запрос
# print(post('http://localhost:8080/api/book',
#            json={"name": "Сказка о рыбаке и рыбке",
#                  "author": "А. С. Пушкин",
#                  "genre_id": 11,
#                  "file": "static/pdf/Skazka_o_rybake_i_rybke.pdf",
#                  "cover": "static/img/Skazka_o_rybake_i_rybke.png"}).json())
#
# # добавление пустого запроса
# # некорректный запрос
# print(post('http://localhost:8080/api/book').json())
#
# # добавление неполного запроса
# # некорректный запрос
# print(post('http://localhost:8080/api/book',
#            json={'name': 'Сказка о рыбаке и рыбке'}).json())
#
# print()
#
# #Books: delete
# print('delete:')
# # удаление книги с id == 3
# # корректный запрос
# print(delete('http://localhost:8080/api/book/3').json())
# post('http://localhost:8080/api/book',
#            json={'name': 'Сказка о рыбаке и рыбке',
#                  'author': 'А. С. Пушкин',
#                  'genre_id': 11,
#                  'file': 'static/pdf/Skazka_o_rybake_i_rybke.pdf',
#                  'cover': 'static/img/Skazka_o_rybake_i_rybke.png'}).json()
#
# # удаление книги с несуществующем id == 999
# # некорректный запрос
# print(delete('http://localhost:8080/api/books/999').json())
#
# print('-------------------------')

# Genres: get
print('Genres')
# print('get:')
# # получение всех жанров
# # корректный запрос
# print(get('http://localhost:8080/api/genres').json())
#
# # получение одного жанра с существующим id == 1
# # корректный запрос
# print(get('http://localhost:8080/api/genre/1').json())
#
# # получение одного жанра с несуществующим id == 999
# # некорректный запрос
# print(get('http://localhost:8080/api/genre/999').json())
#
# # параметр не типа int
# # некорректный запрос
# print(get('http://localhost:8080/api/genre/q').json())
#
# print()
#
# # Genres: post
# print('post:')
# # добавление жанра
# # корректный запрос
# print(post('http://localhost:8080/api/genre',
#            json={'name': 'Повесть',
#                  'is_for_kids': True}).json())
#
# # добавление пустого запроса
# # некорректный запрос
# print(post('http://localhost:8080/api/genre').json())
#
# print()
#
# # Genres: delete
# print('delete:')
# # удаление жанра с id == 12
# # корректный запрос
# print(delete('http://localhost:8080/api/genre/12').json())
# post('http://localhost:8080/api/genre',
#            json={'name': 'Повесть',
#                  'is_for_kids': True}).json()
#
# # удаление жанра с несуществующем id == 999
# # некорректный запрос
# print(delete('http://localhost:8080/api/genre/999').json())
