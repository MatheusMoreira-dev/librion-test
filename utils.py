import requests
from exceptions.copy_exception import IsbnNotFoundError

# função para buscar livros por isbn na API externa
def find_book(isbn: str):

    book_url = f'https://openlibrary.org/isbn/{isbn}.json'
    book_res = requests.get(book_url)

    if book_res.status_code != 200:
        raise IsbnNotFoundError('ISBN não encontrada ou inválida!')
    
    book_data = book_res.json()
    title = book_data.get('title')

    works = book_data.get('works', [])
    if not works:
        return {'title': title, 'author': 'Não encontrado',}
    
    work_key = works[0]['key']
    work_url = f'https://openlibrary.org{work_key}.json'
    work_res = requests.get(work_url)
    work_data = work_res.json()

    author = 'Não encontrado'
    authors = work_data.get("authors")

    if authors:
        author_key = authors[0]["author"]["key"]   # primeiro autor
        author_url = f"https://openlibrary.org{author_key}.json"
        author_res = requests.get(author_url)
        if author_res.status_code == 200:
            author_data = author_res.json()
            author = author_data.get('name')

    return {
        'title': title,
        'author': author,
        'description': '',
        'image': '',
        'age_rating': ''
    }

