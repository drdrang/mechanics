# Makefile for project notes.

mdfiles := $(wildcard *.md)
htmlfiles := $(patsubst %.md, %.html, $(mdfiles))

all: $(htmlfiles)
	python buildRSS.py > index.xml

%.html: %.md header.tmpl footer.tmpl
	python buildPage.py $* > $@

install:
	rsync -av *.html  ../build/
	rsync -av *.css   ../build/
	rsync -av *.xml	  ../build/
	rsync -av  images ../build/

clean:
	rm $(htmlfiles)
