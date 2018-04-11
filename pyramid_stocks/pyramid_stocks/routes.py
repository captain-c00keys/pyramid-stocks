def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=None)
    config.add_route('index', '/')
    config.add_route('auth', '/auth')
    config.add_route('stock', '/stock_add')
    config.add_route('logout', '/logout')
    config.add_route('portfolio', '/portfolio')
    config.add_route('portfolio_symbol', '/stock_detail{symbol}')
 