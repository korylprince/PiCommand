This is a simple web interface for running commands and returning output. Related to [this stackoverflow question](http://stackoverflow.com/questions/17391558/how-to-execute-system-commands-with-a-button-press-on-a-html-file).

PiCommand

https://github.com/korylprince/PiCommand

#Installing#

If you're using debian, do 

    sudo apt-get update
    sudo apt-get install python-virtualenv
    cd /home/pi
    virtualenv PiCommand
    cd PiCommand
    . bin/activate
    pip install gunicorn
    git clone dfdf
    cd PiCommand
    ../bin/gunicorn -b 0.0.0.0:8000 command:application 

and browse to http://&lt;pi IP&gt;:8000/ 

#Usage#

All you need to do to add buttons is to edit the `buttons` variable in `command.py`. `buttons` is a list of tuples. The first item in each tuple is a python function that returns some output. The second item is the label the button will have on the web interface. Two examples are included.

Included is a basic init script (`picommand`). To have PiCommand start on system start run:

    sudo cp picommand /etc/init.d/
    sudo chown root:root /etc/init.d/picommand
    sudo update-rc.d picommand defaults

And use:

    sudo /etc/init.d/picommand start
    sudo /etc/init.d/picommand stop

To manage the service.

NOTE: Remember, everything will run as root privledges now! (You can change this with an argument to start-stop-daemon in the script.)

#Caveats#

This is really just a proof of concept, put together in a few hours. Don't open this to the outside world or malicious users. There aren't really any security checks.

If you have any issues or questions, email the email address below, or open an issue at: https://github.com/korylprince/PiCommand/issues

#License#

Code is Copyright 2013 Kory Prince (korylprince at gmail dot com)
This code is Public Domain. There is no warranty. Do whatever you want. It'd be nice if you sent me an email telling me someone used it though.
