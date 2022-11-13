def save_picture(picture) -> str: # возвращает путь
    filename = picture.filename
    path = f"./uploads/images/{filename}"
    picture.save(path)

    return path

