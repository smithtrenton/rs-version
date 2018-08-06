import logging

from flask import Flask

from rs_version.osrs import Version
from rs_version.osrs.version import find_version


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route('/_cron/osrs')
def check_osrs():
    last_version = Version.latest()
    logger.info('Loaded last_version: {}'.format(last_version))
    current_version = find_version(last_version.version)
    logger.info('Found current_version: {}'.format(current_version))
    if current_version != last_version.version:
        logger.info('Updating version from {} to {}'.format(last_version.version, current_version))
        Version(version=current_version, bucket_path='').put()
        logger.info('Version entity update success')
    return 'Current OSRS: {}'.format(current_version)


@app.route('/_cron/rs3')
def check_rs3():
    return
