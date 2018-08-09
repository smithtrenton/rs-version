import logging

from flask import Flask

from rs_version.osrs import find_version
from rs_version import versions


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/_cron/osrs',methods=['GET'])
def check_osrs():
    latest_entity = versions.get_latest(versions.OSRS_KIND)
    logging.info('Latest OSRS entity: {}'.format(latest_entity))
    last_version = latest_entity.get('version', 1)
    logger.info('Loaded last_version: {}'.format(last_version))
    current_version = find_version(last_version)
    logger.info('Found current_version: {}'.format(current_version))
    if current_version != last_version:
        logger.info('Updating version from {} to {}'.format(last_version, current_version))
        versions.update_entity(latest_entity, version=current_version)
        logger.info('Version entity update success')
    return 'Current OSRS: {}'.format(current_version)


@app.route('/current/osrs')
def display_osrs():
    latest_entity = versions.get_latest(versions.OSRS_KIND)
    return 'Current OSRS: {}'.format(latest_entity.get('version', 1))


@app.route('/_cron/rs3')
def check_rs3():
    return 'Missing implementation'


@app.route('/current/rs3')
def display_rs3():
    return 'Missing implementation'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
