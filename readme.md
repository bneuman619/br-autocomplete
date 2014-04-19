This is a lightweight web app for looking up NBA players on [Basketball Reference](http://basketball-reference.com) and doing cool stuff with the data you get back.

To run it, you need:  
*Python 2.7*  
*Flask*  
*iPython*  
*iPython Notebook*  
*pandas/matplotlib/numpy/etc*
*sqlalchemy*

Once you get all that working, run the Flask webapp via **'python app.py'**

Then run the iPython notebook server via **'ipython notebook'**

When you run the Notebook, make sure you do it from the application's root directory.

Then navigate to [localhost:5000/](http://localhost:5000/) in the browser.

You can search for NBA players on the index page. Your searches should auto-complete, thanks to the **[google-suggest-api](https://github.com/haochi/jquery.googleSuggest)**

Running a search should do behind-the-scenes magic to scrape Basketball-Reference and generate an iPython Notebook from which you can do stuff with the stats, like **graph them using .plot()**.

Running the search will redirect you to a page which displays the corresponding iPython Notebook in an iframe.

Still need to do lots of work to clean up how you access the scraped data, then document it so users can actually manipulate the data. The Notebook format will be perfect for an inline 'readme' on how to manipulate the data.

Then need to set up a DB so we don't need to hit up B-R all the time.
