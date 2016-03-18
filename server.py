#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import argparse
import asyncio, json
import functools
from aiohttp import web

async def handle(resource, request):
    print('200 - {0} - {1}'.format(request.path, json.dumps(resource)))
    return web.json_response(resource)

async def not_found(request):
    print('404 - {}'.format(request.path))
    return web.Response(body=None, status=404)

if __name__ == "__main__":
    app = web.Application()
    parser = argparse.ArgumentParser(description='Really simple JSON server.')
    parser.add_argument('routes_file', type=str, help='routes JSON file describing path to resource resolution')
    parser.add_argument('--port', type=int, default=8080, help='port number')

    args = parser.parse_args()
    with open(args.routes_file) as fp:
        routes = json.loads(fp.read())
        for path, resource in routes.items():
            print('Registering {0} -> {1}'.format(path, resource))
            for method in ['GET', 'POST', 'PUT', 'PATCH', 'HEAD']:
                app.router.add_route(method, path, functools.partial(handle, resource))
        app.router.add_route('*', '/{tail:.*}', not_found)
    web.run_app(app, port=args.port)
