#!/usr/bin/python3
from models.engine.file_storage import FileStorage

# create a unique FileStorage instance for your application.
storage = FileStorage()

# Call reload() method on this variable to load objects from
# the json file.
storage.reload()
