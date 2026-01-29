import os
from pathlib import Path
import time
import sys
import objects
import logging

from objects import Database, Tag, Device
from objects.connections import TCPConnection
import common.constants as constants
from core.Downloader import Downloader
from core.socketHandler import SocketHandler
from core.tagHandler import tagHandler

def main():
    try:
        connection = TCPConnection('eth0', 'joe-z-flex', '10.80.14.125')
        Tag1 = Tag('Tag1', 1)
        list = [Tag1]
        test = Database('C:\\Users\\joe.zink\\OneDrive - HMS Industrial Networks\\Desktop\\module-autotest\\win_app\\databases\\AO8.cd32', 789, list)

        Downloader()
        
        flex = Device('joe-z-flex', list)

        Downloader.download_build(flex, connection, test)

    except Exception as e:
        logging.error(f'error occurred during execution of Main, {e}')

main()