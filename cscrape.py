from craigslist import CraigslistForSale
from slackclient import SlackClient

# https://newjersey.craigslist.org/search/sss?query=kindle&sort=rel



def do_scrape():
    cl = CraigslistForSale(site = "newjersey", category="sss?query=MACBOOK&sort=rel&search_distance=5&postal=07307")

    results = cl.get_results(sort_by="newest", geotagged=True, limit= 10)
    for result in results:
        SLACK_TOKEN = "xoxp-452187027302-450086424528-450729972611-cb8062777467a37f65e543f519b73687"
        SLACK_CHANNEL = "#craigslist"

        sc = SlackClient(SLACK_TOKEN)

        desc = "{0} | {1} | {2} | {3} | <{4}>".format(result["name"], result["datetime"], result["price"], result["geotag"], result["url"])

        sc.api_call(
            "chat.postMessage", channel=SLACK_CHANNEL, text = desc, username= "pybot", icon_emoji="robot_face:"
        )

