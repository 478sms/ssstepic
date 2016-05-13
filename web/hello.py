import cgi

def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    qs = cgi.parse_qs(env['QUERY_STRING'])
    return ['%s=%s<br>' % (k, qs[k]) for k in qs]
