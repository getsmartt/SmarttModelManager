import hashlib
import uuid
from urllib.parse import urlparse
from os.path import splitext
import requests
import errno
import os
import shutil
import random


def get_hash(model):
    buff_size = 65536  # let's read stuff in 64kb chunks!

    sha256 = hashlib.sha256()

    with open(model, 'rb') as h:
        while True:
            data = h.read(buff_size)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()


def contrasting_text_color(hex_str):
    (r, g, b) = (hex_str[:2], hex_str[2:4], hex_str[4:])
    return '000' if 1 - (int(r, 16) * 0.299 + int(g, 16) * 0.587 + int(b, 16) * 0.114) / 255 < 0.5 else 'fff'


def max_contrasting_text_color(hex_str):
    (rs, gs, bs) = (int(hex_str[:2], 16), int(hex_str[2:4], 16), int(hex_str[4:], 16))
    flip_ys = .342
    trc = 2.4
    rco = 0.2126729
    gco = 0.7151522
    bco = 0.0721750
    ys = (rs / 255.0) ** trc * rco + (gs / 255.0) ** trc * gco + (bs / 255.0) ** trc * bco
    return 'fff' if ys <= flip_ys else '000'


def random_color():
    hexadecimal = "#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    return hexadecimal


def remove_bad_chars(value):
    delete_chars = '\\/:*?"<>|'
    for c in delete_chars:
        value = value.replace(c, '')
    return value


def get_url_extension(url):
    """Return the filename extension from url, or ''."""
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return ext  # or ext[1:] if you don't want the leading '.'


def fetch_json(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        j = response.json()
        return j
    else:
        return {response.status_code}


# def move_files():
def list_files_recursively(directory, extensions=('.safetensors', '.ckpt', '.pt', '.bin', '.zip')):
    for root, dirs, files in os.walk(directory):
        filenames = [f for f in files if not f[0] == '.']
        for filename in filenames:
            if filename.endswith(extensions):
                yield os.path.join(root, filename)  # this joins together strings separated by commas


def list_matches_recursively(directory, old_name, extensions=('.safetensors', '.ckpt', '.pt', '.bin', '.zip')):
    files = os.listdir(directory)
    for filename in files:
        if filename.startswith(old_name) and not filename.endswith(extensions) and not filename == old_name:
            yield os.path.join(directory, filename)  # this joins together strings separated by commas


def safe_move(src, dst):
    """Rename a file from ``src`` to ``dst``.

    *   Moves must be atomic.  ``shutil.move()`` is not atomic.
        Note that multiple threads may try to write to the cache at once,
        so atomicity is required to ensure the serving on one thread doesn't
        pick up a partially saved image from another thread.

    *   Moves must work across filesystems.  Often temp directories and the
        cache directories live on different filesystems.  ``os.rename()`` can
        throw errors if run across filesystems.

    So we try ``os.rename()``, but if we detect a cross-filesystem copy, we
    switch to ``shutil.move()`` with some wrappers to make it atomic.
    """
    try:
        os.rename(src, dst)
    except OSError as err:

        if err.errno == errno.EXDEV:
            # Generate a unique ID, and copy `<src>` to the target directory
            # with a temporary name `<dst>.<ID>.tmp`.  Because we're copying
            # across a filesystem boundary, this initial copy may not be
            # atomic.  We intersperse a random UUID so if different processes
            # are copying into `<dst>`, they don't overlap in their tmp copies.
            copy_id = uuid.uuid4()
            tmp_dst = "%s.%s.tmp" % (dst, copy_id)
            shutil.copyfile(src, tmp_dst)

            # Then do an atomic rename onto the new name, and clean up the
            # source image.
            os.rename(tmp_dst, dst)
            os.unlink(src)
        else:
            raise
