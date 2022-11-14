"""Загрузка фото"""
import logging
from json import JSONDecodeError

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


def success(post):
    return render_template('post_uploaded.html',
                           post=post)


@loader_blueprint.route('/post', methods=['POST'])
def load_file_page():
    picture = request.files.get('picture')  # , None
    content = request.form.get('content')  # , None

    # Проверка
    utils.check_picture_resolution(picture)

    if not picture or not content:
        return "Нет картинки или текста"
    try:
        picture_path: str = '/' + utils.save_picture(picture)
    except FileNotFoundError:
        logging.info('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'

    post = {'pic': picture_path, 'content': content}
    functions.add_post(post)
    return success(post)
