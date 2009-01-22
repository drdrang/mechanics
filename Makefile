all:
	cd src && python buildChapters.py
	cd src && make

install: all
	cd src && make install

clean:
	cd src && make clean
