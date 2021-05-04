import nginx
c = nginx.Conf()
s = nginx.Server()

s.add(
     nginx.Key('listen', '12346'),
     nginx.Comment('Yes, python-nginx can read/write comments!'),
     nginx.Key('proxy_pass', '194.5.192.202:22'),
#     nginx.Key('proxy_protocol', 'on'),
#     nginx.Key('set_real_ip_from', '$proxy_protocol_addr')
 )
c.add(s)
nginx.dumpf(c, '/etc/nginx/stream/mysite1.conf')
