# Юнит-тесты для класса BooksCollector
main.py - код класса BookCollector\
tests.py - 16 проверок, полностью покрывшие код класса.
### test_add_new_book_add_two_books
Проверка добавления книги. Даже двух книг.
### test_books_rating_and_favorites_true
Проверка метода __init__.
###  test_add_new_book_not_empty_name_rating_is_one
Устанавливается ли по умолчанию при добавлении книги с непустым именем рейтинг 1.
###  test_set_book_rating_for_added_book_rating_5_rating_is_set
Можно ли установить рейтинг 5 для книги, добавленной в словарь.
###  test_get_books_with_specific_rating_rating_5_return_list_of_books
Возвращается ли список книг с рейтингом 5.
###  test_get_books_rating_true
Возвращается ли словарь целиком.
###  test_add_book_in_favorites_added_book_name_book_in_favorites
Добавляется ли книга, добавленная в словарь, в Избранное.
###  test_delete_book_from_favorites_added_book_name_book_deleted
Удаляется ли книга, добавленная в словарь и Избранное, из Избранного.
###  test_get_list_of_favorites_books_true
Возвращается ли список книг, добавленных в Избранное.
###  test_get_book_rating_for_empty_name_return_rating
Возвращается ли рейтинг книги для пустого имени.
###  test_add_new_book_add_book_twice_not_in_books_rating
Можно ли дважды добавить в словарь одну и ту же книгу.
###  test_set_book_rating_for_not_added_book_rating_not_set
Устанавливается ли рейтинг для книги, не добавленной в словарь.
###  test_set_book_rating_rating_less_than_one_rating_not_set
Устанавливается ли рейтинг 0.
###  test_set_book_rating_rating_more_than_ten_rating_not_set
Устанавливается ли рейтинг 11.
###  test_get_book_rating_for_not_added_book_return_none
Возвращается ли None, если передать имя не добавленной в словарь книги.
###  test_add_book_in_favorites_not_added_book_return_none
Добавляется ли книга в Избранное, если ее нет в словаре.
