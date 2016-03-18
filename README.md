# really-simple-json-server

see: http://szborows.blogspot.com/2016/03/really-simple-json-server.html

# how to run using Dockerfile?
`docker run -it -p 80 -v $PWD:/app:ro szborows/aiohttp-python351 /bin/bash -c "/app/server.py --port 6543
/app/example_routes_file.json"`
