from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent.parent
''' / '''

ENV_FILE = ROOT_DIR / '.env'
''' /.env '''

STORAGE_DIR = ROOT_DIR / 'storage'
''' /storage/ '''

SQLITE_FILE = STORAGE_DIR / 'database.sqlite3'
''' /storage/database.sqlite3 '''
