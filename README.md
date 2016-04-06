# Offshore Company Generator

Python project that generates an offshore company name using Markov chains on the ICIJ Leaks database and displays it on a web page.

Generator
---------

I used the > 100.000 offshore company database from the [ICIJ Offshore Leaks database](https://offshoreleaks.icij.org/about/download)

It covers approx. 1980 - 2010. These are not the __*Panama Papers*__ leaks yet, but *ICIJ* announced that they'll publish some data early May 2016.

- Using ```crunch.py```on the ``nodesNW.csv`` file from the database, we extract the relevant company information and save it in 3 *JSON* files

- Load the 3 *JSON* files, and setup a Markov chain on the names using ``markov.py`` (3-gram model)

I used this great tutorial for the Markov chain implementation: http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/

- Finally, add a random company entity, and a random address for extra fun (I didn't use Markov chains for these)

Web server
---------

I used [Bottle](http://bottlepy.org) micro-framework. It's ideal for this kind of project.

There are only 2 routes, one for the main page and another for the static images.

Since I already had a lighttpd server, I chose to use FastCGI with [flup](https://pypi.python.org/pypi/flup/1.0.2) to use lighttpd as backend
