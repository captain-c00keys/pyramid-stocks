def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/index')
    config.add_route('auth', '/register')
    config.add_route('stock', '/stock_add')
    config.add_route('portfolio', '/portfolio')
    config.add_route('portfolio/{symbol}', '/stock_detail')
