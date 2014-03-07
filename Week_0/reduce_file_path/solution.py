def reduce_file_path(path):
	dirs = path.split("/")
	final_dirs = []
	for dir_str in dirs:
		if dir_str == '..':
			if len(final_dirs):
				del final_dirs[-1]
		elif dir_str != '.' and dir_str != '':
			final_dirs.append(dir_str)			
	return '/' + '/'.join(final_dirs)

def main():
	print(reduce_file_path("/")	)
	print(reduce_file_path("/srv/../"))
	print(reduce_file_path("/srv/www/htdocs/wtf/"))
	print(reduce_file_path("/srv/www/htdocs/wtf"))
	print(reduce_file_path("/srv/./././././"))
	print(reduce_file_path("/etc//wtf/"))
	print(reduce_file_path("/etc/../etc/../etc/../"))
	print(reduce_file_path("//////////////"))
	print(reduce_file_path("/../"))

if __name__ == '__main__':
	main()