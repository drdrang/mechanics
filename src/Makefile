# Makefile for project notes.

mdfiles := $(wildcard *.md)
htmlfiles := $(patsubst %.md, %.html, $(mdfiles))

all: chapters $(htmlfiles)
	python buildRSS.py > index.xml
	python buildJS.py > problemCount.js

%.html: %.md header.tmpl footer.tmpl
	python buildPage.py $* > $@

install:
	rsync -av *.html  ../build/
	rsync -av *.css   ../build/
	rsync -av *.xml	  ../build/
	rsync -av *.js 	  ../build/
	rsync -av  images ../build/

clean:
	rm $(htmlfiles)
	rm chapter*.md
	rm index.xml

chapters:
	python buildChapters.py
