from google.cloud import datastore

client = datastore.Client()

LATEST_KEY_ID = 'latest'

OSRS_KIND = 'OSRS'
RS3_KIND = 'RS3'

def get_latest(kind):
    key = client.key(kind, LATEST_KEY_ID)
    entity = client.get(key)
    if entity is None:
        entity = datastore.Entity(key=key)
    return entity


def update_entity(entity, version=None, jar=None):
    entity.update({
        'version': version or entity.get('version'),
        'jar': jar or entity.get('jar'),
    })
    client.put(entity)


def update_latest(kind, version=None, jar=None):
    entity = get_latest(kind)
    update_entity(entity, version=version, jar=jar)
