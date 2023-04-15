from setups import Users, History
from helpers.idgenerator import get__new_search_id


def get_user_id(id: int) -> int:
    """Возвращает локальный идентификатор пользователя """
    try:
        user = Users.get(Users.tg_id == id)
        return user.id
    except:
        return None

def add_user(id: int) -> int:
    """Добавляет нового пользователя в таблицу пользователей и возвращает локальный идентификатор"""
    user_id = get_user_id(id=id)
    if user_id:
        return user_id
    return Users.create(tg_id = id).save()

def add_new_search(user_id: int, kind: str) -> int:
    """
    Добавляет в таблицу истории запись о новом поиске и возвращает идентификатор поиска
    :param user_id: (int) идентификатор пользователя
    :param kind: (str) имя команды
    :return: (int) идентификатор записи
    """
    return History.create(user_id=user_id, search_kind=kind).save()

def cancel_search_by_user(search_id: int) -> None:
    """
    Обновляет таблицу истории. Выставляет флаг отмены поиска пользователем.
    :param search_id: (int) идентификатор записи в таблице истории
    """
    History.update({"cancel": True, "user_cancel": True}).where(id == search_id).execute()

def cancel_search_by_error(search_id: int) -> None:
    """
    Обновляет таблицу истории. Выставляет флаг отмены поиска из-за ошибки.
    :param search_id: (int) идентификатор записи в таблице истории
    """
    History.update({"cancel": True, "error_cancel": True}).where(id == search_id).execute()
