import redis

r = redis.Redis(host='10.120.14.128', port=6379, decode_responses=True)
re_stock = r.hgetall('stock')

print(re_stock)