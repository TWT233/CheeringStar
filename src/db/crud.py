from typing import List, Tuple

from sqlalchemy.orm import Query

from . import models, get_db


def query(did: int) -> Query:
    return get_db().query(models.Binding).where(models.Binding.discord_id == did)


def get(did: int) -> List[models.Binding]:
    return query(did).all()


def bind(did: int, server: int, game_id: int):
    raw_q = query(did)

    if not raw_q.all():
        entry = models.Binding()
        entry.discord_id = did
    else:
        entry = raw_q.first()

    setattr(entry, f't{server}_2', getattr(entry, f't{server}_1'))
    setattr(entry, f't{server}_1', game_id)

    if not raw_q.all():
        get_db().add(entry)
    get_db().commit()


def unbind(did: int, server: int) -> Tuple[bool, str]:
    raw_q = query(did)

    if not raw_q.all():
        return False, 'not found'
    else:
        entry = raw_q.first()

    setattr(entry, f't{server}_1', getattr(entry, f't{server}_2'))
    setattr(entry, f't{server}_2', 0)
    get_db().commit()
    return True, ''
