def save_picture(picture) -> str: # возвращает путь
    filename = picture.filename
    path = f"./uploads/images/{filename}"
    picture.save(path)

    return path

def check_picture_resolution(picture) -> str:
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    filename = picture.filename
    extension = filename.split('.')[-1]
    if extension not in ALLOWED_EXTENSIONS:
        return 'Формат файла не подходит'