import logging
import socket
import struct

import requests


logger = logging.getLogger(__name__)


HOST = 'oldschool1.runescape.com'
PORT = '43594'
SOCKET_PARAMS = (HOST, PORT)
VERSION_RANGE = (1, 500)


def _create_struct(version):
    return struct.pack('>bi', 15, version)


def _check_response(response):
    unpacked = struct.unpack('b', response)[0]
    return unpacked != 6


def check_version(version):
    version_socket = socket.create_connection(SOCKET_PARAMS)
    if version_socket:
        version_socket.send(_create_struct(version))
        response = version_socket.recv(1)
        if response:
            return _check_response(response)

    return False


def find_version(starting_version):
    if starting_version not in range(*VERSION_RANGE):
        raise 'Version out of range: {}'.format(starting_version)

    logger.info('Checking version: {}'.format(starting_version))
    if not check_version(starting_version):
        logger.info('Version not found, incrementing...')
        return find_version(starting_version + 1)

    logger.info('Version matches!')
    return starting_version
