from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent.parent
''' / '''

ENV_FILE = ROOT_DIR / '.env'
''' /.env '''

STORAGE_DIR = ROOT_DIR / 'storage'
''' /storage/ '''

PARAMETERS_FILE = ROOT_DIR / 'app' / 'config' / 'parameters.py'
''' /storage/database.sqlite3 '''
