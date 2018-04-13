from pyramid.view import notfound_view_config
from pyramid.httpexceptions import HTTPFound


@notfound_view_config(renderer='../templates/404.jinja2')
def notfound_view(request):
    request.response.status = 404
    return HTTPFound(location=request.route.url('auth'))
