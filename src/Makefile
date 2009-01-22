# Makefile for site.

mdfiles := $(wildcard *.md)
htmlfiles := $(patsubst %.md, %.html, $(mdfiles))


all: $(htmlfiles)
	python buildRSS.py > index.xml
	python buildJS.py > problemCounters.js

%.html: %.md header.tmpl footer.tmpl
	python buildPage.py $* > $@

install: all
	rsync -av *.html  ../build/
	rsync -av *.css   ../build/
	rsync -av *.xml	  ../build/
	rsync -av *.js 	  ../build/
	rsync -av  images ../build/

clean:
	rm chapter*.md
	rm index.xml
	rm $(htmlfiles)

	
	