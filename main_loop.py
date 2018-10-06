from cscrape import do_scrape
import time
import sys
import traceback

while True:
        print("{}: Starting scrape cycle".format(time.ctime()))
        try:
            print("Hi")
            do_scrape()
        except KeyboardInterrupt:
            print("Exiting....")
            sys.exit(1)
        except Exception as exc:
            print("Error with the scraping:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print("{}: Successfully finished scraping".format(time.ctime()))
        time.sleep(30)