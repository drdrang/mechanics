# Makefile for project notes.

mdfiles := $(wildcard *.md)
htmlfiles := $(patsubst %.md, %.html, $(mdfiles))

all: $(htmlfiles)

%.html: %.md header.tmpl footer.tmpl
	python buildPage.py $* > $@
	python buildRSS.py > index.xml

install:
	rsync -av *.html  ../build/
	rsync -av *.css   ../build/
	rsync -av  images ../build/

clean:
	rm $(htmlfiles)
