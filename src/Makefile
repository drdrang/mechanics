# Makefile for project notes.

mdfiles := $(wildcard *.md)
htmlfiles := $(patsubst %.md, %.html, $(mdfiles))

all: $(htmlfiles)

%.html: %.md project.info header.tmpl footer.tmpl
	python buildPage.py $* > $@

install:
	cp -f *.html  ../build/
	cp -f *.css   ../build/
	cp -rf images ../build/

clean:
	rm $(htmlfiles)
