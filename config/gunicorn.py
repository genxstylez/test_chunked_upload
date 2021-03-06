import multiprocessing

workers = (2 * multiprocessing.cpu_count()) + 1
worker_class = 'gevent'
loglevel = 'debug'
accesslog = '-'
errorlog = '-'
forwarded_allow_ips = '*'
secure_scheme_headers = {
    # 'X-FORWARDED-PROTOCOL': 'ssl',
    'X-FORWARDED-PROTO': 'https',
    # 'X-FORWARDED-SSL': 'on',
}
preload_app = False
limit_request_line = int(4094 / 4)
limit_request_fields = int(100 / 2)
keepalive = 2 * 2
