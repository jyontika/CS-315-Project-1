# CS-315-Project-1
#### @authors: Jyontika Kapoor, Ashley You, Ryan Boone, Audrey Yip, Josie Ramírez, Miraya Gupta
##### Project Topic: Followers

This project is conducted by six students at Wellesley College CS-315: Data Science for the Web.
We are replicating a TikTok experiment paper by Boeker and Urman at the University of Zurich.

#### Methods to run tests:
1. Please clone the repo; leave the files in its folder
2. Open the control_saves.py and testing_saves.py
3. Run both at the same by opening two terminals and entering each of the lines below (one in each terminal):

```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```


'''python -m pytest tests/tiktok/test_active.py --html=report_active.html'''


