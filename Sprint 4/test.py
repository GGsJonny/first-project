from main import BooksCollector

# Инициализация объекта класса для тестирования
@pytest.fixture
def collector():
    return BooksCollector()

# Тест на добавление новой книги с корректным именем
def test_add_new_book_valid_name(collector):
    book_name = "Корректное имя"
    collector.add_new_book(book_name)
    assert book_name in collector.books_genre

# Тест на добавление новой книги с пустым именем
def test_add_new_book_empty_name(collector):
    book_name = ""
    collector.add_new_book(book_name)
    assert book_name not in collector.books_genre

# Тест на добавление новой книги с длинным именем
def test_add_new_book_long_name(collector):
    book_name = "x" * 42  # Имя длиннее 41 символа
    collector.add_new_book(book_name)
    assert book_name not in collector.books_genre

# Тест на установку жанра для существующей книги
def test_set_book_genre_existing_book(collector):
    book_name = "Книга с жанром"
    genre = "Фантастика"
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, genre)
    assert collector.get_book_genre(book_name) == genre

# Тест на установку жанра для несуществующей книги
def test_set_book_genre_nonexistent_book(collector):
    book_name = "Несуществующая книга"
    genre = "Фантастика"
    collector.set_book_genre(book_name, genre)
    assert collector.get_book_genre(book_name) is None

# Тест на получение списка книг определенного жанра
def test_get_books_with_specific_genre(collector):
    collector.add_new_book("Книга1")
    collector.set_book_genre("Книга1", "Фантастика")
    collector.add_new_book("Книга2")
    collector.set_book_genre("Книга2", "Фантастика")
    assert "Книга1" in collector.get_books_with_specific_genre("Фантастика")
    assert "Книга2" in collector.get_books_with_specific_genre("Фантастика")

# Тест на получение списка книг, подходящих детям
def test_get_books_for_children(collector):
    collector.add_new_book("Детская книга")
    collector.set_book_genre("Детская книга", "Мультфильмы")
    assert "Детская книга" in collector.get_books_for_children()

# Тест на добавление книги в избранное
def test_add_book_in_favorites(collector):
    book_name = "Избранная книга"
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)
    assert book_name in collector.favorites

# Тест на удаление книги из избранного
def test_delete_book_from_favorites(collector):
    book_name = "Избранная книга"
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)
    collector.delete_book_from_favorites(book_name)
    assert book_name not in collector.favorites

# Параметризованный тест для проверки поиска книг по названию
@pytest.mark.parametrize("name, expected_result", [
    ("Книга1", True),
    ("Книга2", True),
    ("Несуществующая книга", False)
])
def test_search_books_by_name(collector, name, expected_result):
    collector.add_new_book("Книга1")
    collector.add_new_book("Книга2")
    result = name in collector.books_genre
    assert result == expected_result
