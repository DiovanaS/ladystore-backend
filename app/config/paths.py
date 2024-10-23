from pathlib import Path


ROOT_DIR = Path.cwd()
''' / '''

ENV_FILE = ROOT_DIR / '.env'
''' /.env '''

PARAMETERS_FILE = ROOT_DIR / 'app' / 'config' / 'parameters.py'
''' /app/config/parameters.py '''

STORAGE_DIR = ROOT_DIR / 'storage'
''' /storage/ '''

DATABASE_FILE = STORAGE_DIR / 'database.sqlite3'
''' /storage/database.sqlite3 '''
