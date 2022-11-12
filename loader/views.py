"""Загрузка фото"""
from flask import Blueprint, render_template


# Создаем блюпринт
loader_blueprint = Blueprint('loader_blueprint',
                             __name__,
                             template_folder='templates')

@loader_blueprint.route('/post', methods=['GET'])
def add_post_page():
    """Добавить пост"""
    return render_template('post_form.html')

@loader_blueprint.route('/post',methods=['POST'])
def load_file_page():
    """Кладет загруженный файл в папку uploads"""
