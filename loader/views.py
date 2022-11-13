"""Загрузка фото"""
from flask import Blueprint, render_template, request

# Создаем блюпринт
import functions
from loader import utils

loader_blueprint = Blueprint('loader_blueprint',
                             __name__,
                             template_folder='templates')


@loader_blueprint.route('/post')  # methods=['GET']
def post_page():
    """Отображает формочку с добавлением поста"""
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def load_file_page():
    """Кладет загруженный файл в папку uploads"""
    picture = request.files.get('picture')  # , None
    content = request.form.get('content')  # , None

    if not picture or not content:
        return "Нет картинки или текста"

    # В функцию передаем словарь с ключами из post.json и со значением переменных выше
    # Ключи далее передаем в формочку
    picture_path: str = '/' + utils.save_picture(picture)
    post: dict = functions.add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)
