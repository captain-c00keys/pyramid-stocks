from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import Entry
from ..sample_data import MOCK_DATA
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
import requests
from . import DB_ERR_MSG
import os
from pyramid.security import NO_PERMISSION_REQUIRED

API_URL = ('https://api.iextrading.com/1.0')

@view_config(
    route_name='index', 
    renderer='../templates/index.jinja2',
    request_method='GET',
    permission=NO_PERMISSION_REQUIRED
    )
def my_home_view(request):
    return {} 


@view_config(
    route_name='portfolio_symbol', 
    renderer='../templates/stock_detail.jinja2',
    request_method = 'GET'
    )
def my_detail_view(request):
    symbol = request.matchdict['symbol']
    response = requests.get('{}/stock/{}/company'.format(API_URL, symbol))
    if response.status_code == 200:
        return {'company': response.json()}
    return HTTPNotFound()


@view_config(
    route_name='stock',
    renderer='../templates/stock_add.jinja2')
def stock_view(request):


    if request.method == 'POST':

        if 'symbol' not in request.POST:
            return HTTPNotFound()
        symbol = request.POST['symbol']
        response = requests.get('{}/stock/{}/company'.format(API_URL, symbol))
        if response.status_code == 200:
            try:
                query = request.dbsession.query(Entry)
                stock = query.filter(Entry.symbol == symbol).one_or_none()
            except DBAPIError:
                return DBAPIError(
                    DB_ERR_MSG, content_type='text/plain', status=500)
            if stock is None:
                request.dbsession.add(Entry(**response.json()))
            else:
                for key, value in response.json().items():
                    setattr(stock, key, value)
            return HTTPFound(location=request.route_url('portfolio'))
        return HTTPNotFound()
    try:
        # import pdb; pdb.set_trace()
        symbol = request.GET['symbol']
    except KeyError:
        return {}
    response = requests.get('{}/stock/{}/company'.format(API_URL, symbol))
    if response.status_code == 404:
        return {
            'message': f'''{
                symbol.upper()
            } is not available: ({
                request.text
            })'''
            }
    if response.status_code == 200:
        return {
            'company': response.json()
        }


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_pyramid_stocks_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
