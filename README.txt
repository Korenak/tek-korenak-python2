# tek-korenak-python2
Flask Project
Atom was the editor used in this project
Conda was the python flavor used

to begin(after download and unzip)
navigate to directory korenak_andrew_python2
do not stop at tek-korenak-python2 as this is not where the files will successfully run.

conda create -n venv flask   #name venv whatever you want
conda activate venv #use whatever you named it
pip install -r requirements.txt
# At some point I needed to make a brand new virtual env, so a fresh one is best if
you run into errors with one you tried updating to work.
At time of submission everything has been tested and I get no errors in cmd when
running.

!!!!!
You will have to change the config.py page to reflect the path of your mysql
server
!!!!!

python dbinit.py

#this will establish classes and run the site. However, to fill
the MySQL database with the list of 20 puppies and owners you must exit out of
the site then v
python filldb.py

after filling the data feel free to mess around in the site by adding
puppies+owner removing puppies, and looking at a list of all puppies registered
to the neighborhood along with their ID and owners

HTML templates are in the templates folder
you can see in forms.py where I made Dog name and owner name required fields as
super basic data validation to prevent empty dog or owner fields. DataRequired
only checks T F if anything is there. There are other validation options that
could allow from a list of characters or deny based on a list of characters.

Once you are done poking around the site you can move on to the pand.py file
in pand.py I import my tables back from the MySQL server as pandas dataframes

Shapes of dataframes, merging dataframes, adding a column of colors to datafames,
counting the number of times one of those colors appeared.
Even a command at the
end to create a color_count.csv file, grab that csv file, convert it back into
a data frame, then load it to the MySQL database! Un-needed steps, but it shows
that the concept of saving and loading as csv is possible, and even putting
things back up into MySQL server after manipulation is doable.
I love how you can go into the website make a bunch of new or delete a bunch of
 dogs, and then run pand.py again to see the new results.
