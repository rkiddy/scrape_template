# scrape_template

Setting up a script to do scraping is not as easy as it should be.

For one thing, when one is using a new host (where one has not done scraping before), there seems
to be an arbitrary amount of crap that one has to deal with to get it working. For example, where is
your geckodriver executable? Where is the profile that the instance is going to use? Why does it need
a profile? It seems that every time I bring up a new system, there is a new set of stupidities that
need to be figured out.

But. Part of it can be made simpler.

This project shows a python script which is doing a little bit of scraping.

You will still have to figure out how to install either the firefox driver executable and set
the environment variable (somewhere) so that its location is discoverable. There may be several
ways to install these things. An easy was to install the Chrome driver is:

     sudo apt install chromium-chromedriver

In order to execute this script, do this:

     git clone https://github.com/rkiddy/scrape_template.git scraper
     cd scraper
     virtualenv .venv
     ./.venv/bin/python -m pip install -r requirements.txt
     ./.venv/bin/python scraper.py

I put a line into my ~/.bash_aliases file that has:

     alias tp='./.venv/bin/python'

Then I can say:

    tp -m pip install -r requirements.txt
    tp scraper.py

And that should be it! :--)


