import datetime
import hashlib
import json
import os  # imports operating system module
import textwrap
from io import BytesIO
from os.path import exists
from pathlib import Path

import requests
from PIL import Image, UnidentifiedImageError
from zipfile import ZipFile
import misc
import shortuuid
import models, tags, versions, creators
import logging

# create logger
logger = logging.getLogger('scanner')
logger.setLevel(logging.DEBUG)


def get_models(model, scan_path_name, save_path_name, model_type, api_key='', extensions=('.safetensors', '.ckpt', '.pt', '.bin', '.zip')):
    logger.info(f"Scanning {model}")
