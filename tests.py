class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_books_rating_and_favorites_true(self, collector):
        assert collector.books_rating == {} and collector.favorites == []

    def test_add_new_book_not_empty_name_rating_is_one(self, collector):
        collector.add_new_book('Мегеры')
        assert collector.get_book_rating('Мегеры') == 1

    def test_set_book_rating_for_added_book_rating_5_rating_is_set(self, collector):
        collector.add_new_book('Шесть минут до конца лета')
        collector.set_book_rating('Шесть минут до конца лета', 5)
        assert collector.books_rating['Шесть минут до конца лета'] == 5

    def test_get_books_with_specific_rating_rating_5_return_list_of_books(self, collector):
        collector.add_new_book('Колледж святого Джозефа')
        collector.add_new_book('Чернила')
        collector.add_new_book('Хюльдра')
        collector.set_book_rating('Колледж святого Джозефа', 5)
        collector.set_book_rating('Чернила', 5)
        collector.set_book_rating('Хюльдра', 5)
        assert len(collector.get_books_with_specific_rating(5)) == 3

    def test_get_books_rating_true(self, collector):
        collector.add_new_book('Диалог')
        collector.add_new_book('Слово живое и мертвое')
        collector.add_new_book('Как писать хорошо')
        assert collector.get_books_rating() != {} and len(collector.get_books_rating()) == 3

    def test_add_book_in_favorites_added_book_name_book_in_favorites(self, collector):
        collector.add_new_book('Психбольница в руках пациентов')
        collector.add_book_in_favorites('Психбольница в руках пациентов')
        assert 'Психбольница в руках пациентов' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_added_book_name_book_deleted(self, collector):
        collector.add_new_book('Все о муми-троллях')
        collector.add_book_in_favorites('Все о муми-троллях')
        collector.delete_book_from_favorites('Все о муми-троллях')
        assert 'Все о муми-троллях' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_true(self, collector):
        collector.add_new_book('Острые предметы')
        collector.add_new_book('Исчезнувшая')
        collector.add_new_book('Темные тайны')
        collector.add_book_in_favorites('Острые предметы')
        collector.add_book_in_favorites('Исчезнувшая')
        collector.add_book_in_favorites('Темные тайны')
        assert len(collector.get_list_of_favorites_books()) == 3

    def test_get_book_rating_for_empty_name_return_rating(self, collector):
        collector.add_new_book('')
        collector.set_book_rating('', 5)
        assert collector.get_book_rating('') == 5

    def test_add_new_book_add_book_twice_not_in_books_rating(self, collector):
        collector.add_new_book('Русский балет Дягилева')
        collector.add_new_book('Русский балет Дягилева')
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_for_not_added_book_rating_not_set(self, collector):
        collector.set_book_rating('Несказочная проза провинциального города', 8)
        assert collector.get_book_rating('Несказочная проза провинциального города') == None

    def test_set_book_rating_rating_less_than_one_rating_not_set(self, collector):
        collector.add_new_book('Заводной апельсин')
        collector.set_book_rating('Заводной апельсин', 0)
        assert collector.get_book_rating('Заводной апельсин') == 1
    def test_set_book_rating_rating_more_than_ten_rating_not_set(self, collector):
        collector.add_new_book('Бремя страстей человеческих')
        collector.set_book_rating('Бремя страстей человеческих', 11)
        assert collector.get_book_rating('Бремя страстей человеческих') == 1

    def test_get_book_rating_for_not_added_book_return_none(self, collector):
        assert collector.get_book_rating('Несказочная проза провинциального города') == None
    def test_add_book_in_favorites_not_added_book_return_none(self, collector):
        collector.add_book_in_favorites('Крестный отец')
        assert 'Крестный отец' not in collector.get_list_of_favorites_books()


