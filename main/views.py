from flask import Blueprint, render_template, request
import functions

# для показывания фото

main_blueprint = Blueprint('main_blueprint',
                           __name__,
                           template_folder='templates')

@main_blueprint.route('/')
def main_page():
    return render_template('index.html')

@main_blueprint.route('/search/')
def search_post_page():
    try:
        search_query = request.args.get('s', '')
        posts = functions.search_by_word(search_query)

        return render_template('post_list.html', posts=posts, query=search_query)
    except FileNotFoundError:
        return "Файл для итерации не передан"

