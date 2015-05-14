# Notes for Future Maintainers

As this is a senior-year capstone project, the original authors have graduated
and moved on. This document is a _very_ frank letter so that you know what to
expect if you adopt it. We're assuming the audience is a future senior capstone
group in Miami's CSE department. 

First, a list of skills and languages that you should be familiar with if you
hope to contribute: 

* Python
* JavaScript
* Web architecture (HTTP, REST, JSON)
* Web design (HTML, CSS)
* Linux administration & development

You should also know a little bit about functional programming - anonymous
functions, map/reduce, comprehensions, and other functional constructs are used
fairly extensively on both the server and client sides. In addition, you should
be familiar with the JavaScript environment, with a good understanding of
callbacks (learning Ember.js will be frustrating otherwise). 

The project should be thought of as two almost-entirely-separate components that
communicate via an API. This has several advantages (more responsive app,
separation of view code from business logic) and a few disadvantages (some code
duplication, overall increase in complexity). 

Of the two, the server is much simpler. It is located mainly in the `/api`
directory. It uses several libraries that completely smooth over the process of
moving data from a persistent data store (PostgreSQL) to an API. The web server
is **Flask**, a fairly minimal and modular server that handles the details of
speaking HTTP to browsers. A module called **SQLAlchemy** provides an abstraction
over the database so that _no raw SQL is used_. Instead, interactions are done
using its object-oriented wrapper. A module called **Flask-RESTful** sits on top
of SQLAlchemy, transforming the object-oriented model into a RESTful API.
Finally, another module, **Flask-Restless**, minimizes boilerplate by generating
GET/POST/PUT/DELETE methods for the RESTful objects and automatically
serializing them to JSON. 

[Flask](http://flask.pocoo.org/)

[Flask-RESTful](https://flask-restful.readthedocs.org/en/0.3.2/)

[Flask-Restless](https://flask-restless.readthedocs.org/en/latest/)

The client side is a single-page JavaScript application built using Ember.js. It
lives stand-alone inside the `/client` directory. If you've never done front-end
development before, it will probably take a while for you to get up to speed on
this (it's not jQuery). Ember is complex, but extremely powerful. I _strongly_
recommend using the `ember-cli` tool to manage it. 

The gist of it is that Ember keeps a local store of all objects in its _model_,
then uses _routes_ to transition between _templates_ that display the model in
various ways. When it encounters an object in its model that it doesn't have a
local cache of, it queries the server to fill-in the details of that model. It
keeps track of state by updating the URL, without needing to make a full
round-trip to request a new page from the server. When the user makes changes to
its local model, it pushes those changes back to the server. 

[Ember.js](http://emberjs.com/)

[ember-cli](http://www.ember-cli.com/)

[Todo-Flask-Ember (skeleton project)](https://github.com/gaganpreet/todo-flask-ember)

[JavaScript: The Good Parts](https://www.google.com/search?q=javascript+the+good+parts)

About the state of the project: it's "mostly" done, with lots of room for small
improvements. There were several things that we had the time and capability to
do, but that we had to wait on external services for, and did not get pushed
through before the end of the year.

Our implementation is far from perfect, as this was a learning experience for us
as well. None of us were JS or Python experts going into it, so there's lots of
code that is neither idiomatic nor efficient. There are some things that were on
our client's wish-list that we never got around to doing, as well as some things
that we wanted to fix or improve but didn't have time to work on. 

Here are some requirements that still need to be done:

* CAS single sign-on. The client needs users to be able to sign in with their
Miami UniqueIDs. This is actually quite easy to implement, but you need an
actual domain, and SSL enabled - both of which we couldn't do because IT
services took too long at the end of the year. 
* Mail system. We implemented a naive mailer that simply sends an email to
instructors that are teaching a course with a link to their section (so that
they can assert its compliance). However, this really needs to be bulk-mailed
using IT's mail queue system (again, it just took too long at the end of the
year on their end). 
* Banner import is 80% done, but rough around the edges. All of the data from
Banner displays client-side; now, it just needs to be saved as part of the model
and submitted back to the server. 


In addition, here are some ideas for improvement, or 'wish-list' items: 

* Pagination. The 'catalog' pages that list every course section, instructor,
etc. aren't paginated, and load every object at once. If the list of objects
grows too large (1000's), it could make things very slow. Loading them in
batches of ~25 and paging between them is a better idea. 
* Sorting. Our client wanted a way to sort search results by, e.g., last review
date or most sections. We didn't implement it. 
* Testing. We did it mostly by hand, meaning we probably missed tons of little
edge-cases and errors. Writing quality tests should probably be priority #1, as
it will let you make changes confidently and will teach you about the system.
* Styling / CSS clean-up. The CSS is straight-up awful. There are in-line styles
_everywhere_ and very frequent use of table layouts, hard-coded pixel widths,
and various other front-end sins. (This was the work of one of our group members
who took the 'just-make-it-work' approach. We didn't have time to fix it.
Sorry.)
* Quality Review notes. Our client asked if we could have document uploads to go
with the quality reviews for course versions, but we didn't implement it. There
is some disk space reserved on the production server for this purpose.

Now for total honesty: our implementation is probably more complicated than it
needs to be, and not all of our team members produced consistently high-quality
code. But still, we fulfilled most of our client's constantly-shifting
requirements in a limited time frame. 

We hope the project is in a good enough state for you to work with it
effectively. We tried our best to comment well and communicate throughout the
code. Our emails are in the Contact section of the readme if you have any
questions (or if you need a place to direct your hate-mail at!). 

    Michael Choate
    Alex Dana
    Blake Runkle
