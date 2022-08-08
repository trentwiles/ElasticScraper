# ElasticScraper
Scrape Elastic Search servers exposed to the open internet via Censys.

## How to use this

You'll need an API ID and secret from the Censys website. Sign up, create an account, and go to settings.

![](https://file.coffee/u/PDsqUeeH7JhPLUXIrvs-1.png)

Copy those tokens. Next, open the v2.py file and place your tokens in the correct area.

![image](https://user-images.githubusercontent.com/59586759/183437277-36826716-68af-4daa-bd9f-4ae0fbb07110.png)

Run the script by typing `python3 v2.py` in the terminal. You'll then see the folder you are in populate with dumped Elastic Search databases.
