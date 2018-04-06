from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import MyModel
from ..sample_data import MOCK_DATA
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

@view_config(
    route_name='home', 
    renderer='../templates/index.jinja2'
    )
def my_home_view(request):
    return {}


@view_config(
    route_name='auth', 
    renderer='../templates/auth.jinja2'
    )
def my_login_view(request):
    if request.method == 'GET':
        try:
            username = request.GET['username']
            password = request.GET['password']
            print('User: {}, Pass: {}'.format(username, password))

            return HTTPFound(location=request.route_url('portfolio'))

        except KeyError:
            return {}
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print('User: {}, Pass: {}, Email: {}'.format(username, password, email))

        return HTTPFound(location=request.route_url('entries'))
    return HTTPNotFound()



@view_config(
    route_name='portfolio', 
    renderer='../templates/portfolio.jinja2'
    )
def my_view(request):
    return {
        'entries': MOCK_DATA
    }


@view_config(
    route_name='detail', 
    renderer='../templates/stock_detail.jinja2'
    )
def my_detail_view(request):
    for stock in MOCK_DATA:
        if stock['symbol'] == request.matchdict['symbol']:
            return {'stock': stock}


@view_config(
    route_name='add', 
    renderer='../templates/stock_add.jinja2'
    )
def my_add_view(request):
    return{}

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
