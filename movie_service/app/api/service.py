import os
import httpx


CAST_SERVICE_HOST_URL = os.environ.get('CAST_SERVICE_HOST_URL') or 'http://cast_service:8000/api/v1/casts/'


def is_cast_present(cast_id: int):
    r = httpx.get(f'{url}{cast_id}')
    return r.status_code == 200
