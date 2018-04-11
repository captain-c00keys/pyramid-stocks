from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPBadRequest
from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import Stock
from . import DB_ERR_MSG
import requests
import os


# https: // pixabay.com/api/docs/
API_KEY = os.environ.get('API_KEY', '')


@view_config(route_name='portfolio', renderer='../templates/portfolio.jinja2',
             request_method='GET')
def entries_view(request):
    try:
        query = request.dbsession.query(Stock)
        all_entries = query.all()
    except DBAPIError:
        return Response(DB_ERR_MSG, content_type='text/plain', status=500)

    return {'entries': all_entries}
