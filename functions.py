import json
from typing import List

PATH = 'posts.json'

def load_json_in_list(path) -> List[dict]:
    """Загружает все посты"""
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

def search_by_word(word: str) -> List[dict]:
    """Возвращает значение по слову"""
    result = []
    for post in load_json_in_list(PATH):
        if word.lower() in post['content'].lower():
            result.append(post)

    return result

def add_post(post: dict) -> dict:
    posts: List[dict] = load_json_in_list(PATH)
    posts.append(post)
    with open(PATH, 'w', encoding='utf-8') as file:
        # Посты, которые мы хотим добавить и файлы
        json.dump(posts, file)
    return post


