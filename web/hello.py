#!/usr/bin/env python

import cgi

def app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    #return ['Hello here']
    s = environ.get('QUERY_STRING')
    return s.replace("&", "\n") 

    qs_params = cgi.parse_qs(environ.get('QUERY_STRING'))
    return qs_params

    outp = []
    for k in qs_params.keys():
	#print k, qs_params[k]
        outp.append(k + "=" + qs_params[k] + "\n")

    return outp
