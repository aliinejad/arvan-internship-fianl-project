import inotify.adapters
import os

def _main():
    i = inotify.adapters.Inotify()

    i.add_watch('/etc/nginx/stream/')
    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
	
	if type_names[0] == 'IN_CREATE':
		print(type_names)
		os.system("/etc/init.d/nginx reload")

if __name__ == '__main__':
    _main()

