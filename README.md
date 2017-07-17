# movie_trailers
Python3 script to generate a static HTML website that displays movie box art and trailers.

## Usage
Fork the repository and clone it to your local system. The code was mostly written in Python 3.6, so if you're using Python 2.7, be aware that some things
may be different.

## Installation
Once you have a local copy of the repository, go in to the entertainment_center.py file. In this file, you can create instances of the primary class Movie().

## Usage
After there have been sufficient instances of the class Movie() have been created, be sure to update the movie_list variable at the bottom. Once that is complete you can used ```fresh_tomatoes.open_movies_page(movies)``` movies being the list that were placed in the list above.

From this point you have two options. You can run the script using LINUX or UNIX by simply typing ```python3 entertainment_center.py``` from the movies directory. Alternatively, you can use the Python IDLE by typing, ```import entertainment_center``` from the movies directory or using the fn5 function to run the module from the default Python Editor.  

### Issues
You may notice an error, ```ERROR:browser_gpu_channel_host_factory.cc(103)] Failed to launch GPU process.``` that shows up in your terminal or Python shell. This error is a Browser specific error. If you want to fix the problem, I would recommend visiting https://superuser.com/questions/836832/how-can-i-enable-webgl-in-my-browser but do understand that any changes made can adversely affect your computer and that you make these changes at your own risk. Currently, the error has no ill-effect on the script being run.
