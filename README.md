# scrape_template

Setting up a script to do scraping is not as easy as it should be.

For one thing, when one is using a new host (where one has not done scraping before), there seems
to be an arbitrary amount of crap that one has to deal with to get it working. For example, where is
your geckodriver executable? Where is the profile that the instance is going to use? Why does it need
a profile? It seems that every time I bring up a new system, there is a new set of stupidities that
need to be figured out.

But. Part of it can be made simpler.

This project shows a python script which is doing a little bit of scraping.

In order to execute this script, do this:

    git clone https://github.com/rkiddy/scrape_template.git scraper
    cd scraper
    virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python scraper.py

And that should be it! :--)



