The program runs from script.py

It returns results from eBay.

Insert the path to chromedriver in baseclass.py (chrome_path).
https://chromedriver.chromium.org/downloads

Insert the path to your preferred directory where you want 
CSV file to be created (csv_file_path).

1) It will ask what to search for.
2) It will ask how many posting to include.

The program will only include "Buy It Now" options.
The program will skip any posting where the price is in range.

(Example of skipped posting - price $100 to $200)

Any conditions can be removed or changed for different results.

This version does not utilize some functions in baseclass.py,
but they are left there in case someone finds them useful.
