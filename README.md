# IphoneInStock
This little app is an attempt to simplify the search for a new iPhone model in the first couple of weeks following the release. The bot takes advantage of Telegram's awesome bot API. It was successfully deployed on Replit and used to acquire 3 iPhones of different colors and configurations in NYC and California.

To achieve continuous integration of the service on Replit, which requires the webpage to be open for the script to run, I deployed a supplementary local server that would be running in the main module, keeping the script alive, hence the name.

For privacy reasons, the Telegram ids of all the people that have used the service have been edited out.

To run the app, add the desired product to your cart on apple.com, click go to bag, and then, in the developer tools, locate a bagx cookie file generated upon opening the cart. Copy the file and paste it in place of the "cookies" content in main.py

Below is a demonstration of when a desired iPhone was found.
![IMG_3925](https://github.com/turpitka/IphoneInStock/assets/111830322/02428729-8e57-48f3-b676-d558738b21ea)
