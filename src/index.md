# Introduction #

This is a set of web pages devoted to solving all of the problems in J.P. Den Hartog's book *Mechanics*. I'm doing this because:

1. I've been out of academe a long time and I miss doing these kinds of problems regularly.

2. Engineering students learn by solving problems and seeing problems solved. An online library of solved problems can help more students than I would ever be able to teach in a classroom, even if I were to spend an entire career in teaching.

2. It's a way of contributing to the Internet community. Like the little programs I post [my blog][6], this will be a way for me to give something back to the online world from which I've taken so much.

## The book ##

I've chosen *Mechanics* because it has a good selection of problems, it's [cheap][1] and [readily][2] [available][3], and it's not, as far as I know, being used in classrooms today. My goal is to show students how these problems are solved, not to do their homework for them. (If you're familiar with the book, you know that the answers to all the problems are given in the back. I don't think that detracts from the value of a solutions manual; there's a big difference between a fully-worked-out solution and one-word or one-number answer.)

![book][]

It's not my intention to reproduce the problems here--solutions manuals usually don't restate the problems, and besides, I don't want Dover coming after me for copyright violations. Just get a copy of the book. If $10-15 is too much, you can probably find a copy in your school library.

## The equations ##

Equations are a big part of most solutions. To handle the mathematics, I'm using a JavaScript program called [jsMath][], a spectacular bit of coding from David Cervone of Union College in Schenectady, New York. You should see a little white rectangle labeled "jsMath" in the bottom right corner of your browser's window. Click on it, and a box will pop up that will allow you to configure jsMath for your computer. I suggest you [download a set of TeX fonts][4] for your computer. [TeX][5] is the preeminent system for typesetting mathematics and the pages will look much better if you use these fonts. You'll know you've done the font installation correctly when equations like \(E = mc^2 \) and

\[ P(x < a) = \int_{-\infty}^a e^{-\frac{(x - \mu)^2}{2 \sigma^2}} dx \]

look right, scale right, and print right.

## Navigating the site ##

At the moment, navigation is pretty rudimentary. The chapter links in the sidebar to the right will take you to pages with links to the individual problems associated with each chapter. At the bottom of each problem page are links to the previous and subsequent problems.

If you want to jump right to a specific problem, you can also enter its URL directly:

`http://www.leancrew.com/mechanics/problem123.html`

The problem numbers are always given in three-digit form, with leading zeros if necessary (e.g., the first problem is 'problem001.html').

This is a work in progress, so many of the solutions haven't been written yet. If you try to open an unwritten solution, you'll get a Not Found error in your browser.

## RSS feed ##

You can follow the progress of the site by subscribing to its RSS feed. Your browser's address bar should have an RSS button that will allow you to subscribe. If that doesn't work, the feed's address is 

    http://www.leancrew.com/mechanics/index.xml

which you can manually paste into your feed reader.

New feed items will be generated when:

1. I add a new solution.
2. I edit an old solution.

At present, the feed does not provide full entries for new or edited pages, just the problem number and a brief description. Changes elsewhere in the site, like to this page, will not generate new feed items.



[1]: http://www.buy.com/retail/product.asp?sku=30085228&loc=106&sp=1
[2]: http://store.yahoo.com/doverpublications/0486607542.html
[3]: http://www.amazon.com/exec/obidos/tg/detail/-/0486607542/qid=1138201008/sr=8-1/ref=sr_8_xs_ap_i1_xgl14/102-3200201-1168123?v=glance&s=books&n=507846
[jsMath]: http://www.math.union.edu/locate/jsMath/
[4]: http://www.math.union.edu/~dpvc/jsMath/download/jsMath-fonts.html
[5]: http://www.tug.org/
[book]: images/book-cover.png
[6]: http://www.leancrew.com/all-this
