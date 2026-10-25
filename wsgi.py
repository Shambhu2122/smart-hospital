"""Production WSGI entrypoint; leaves the original dashboard unchanged."""
import os
from server import app, init

if not os.environ.get('HOSPITAL_SECRET'):
    raise RuntimeError('Set HOSPITAL_SECRET in your hosting environment before starting.')
if not os.environ.get('HOSPITAL_DB_PATH'):
    raise RuntimeError('Set HOSPITAL_DB_PATH to a PERSISTENT disk location before starting.')
if os.environ.get('HOSPITAL_HTTPS') != '1':
    raise RuntimeError('Set HOSPITAL_HTTPS=1 and configure HTTPS at the hosting provider.')
os.makedirs(os.path.dirname(os.path.abspath(os.environ['HOSPITAL_DB_PATH'])),exist_ok=True)
with app.app_context():
    init()
