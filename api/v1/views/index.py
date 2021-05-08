#!/usr/bin/python3
"""get the status of this page """
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False, methods=('GET',))
def get_status():
    """get the status of this page """
    mydict = {'status': 'OK'}
    return mydict
