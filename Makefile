all:
	find . ! -name "*.py" ! -name "*.cpp" ! -name ".gitignore" ! -name "README" -maxdepth 1 -type f
