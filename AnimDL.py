from lxml import etree, html
from slugify import slugify

import requests


class Anime:
    def __init__(self):
        self.title = False
        self.qualities = []
        self.batch = False
        self.date = False
        self.links = []


class AnimDL:
    def __init__(self, anim_id):
        self.id = anim_id
        self.quality = False
        self.anime = Anime()
        self.parser = etree.HTMLParser()
        self.load()

    def load(self):
        url = f"https://anime-list6.gq/anime/{self.id}"
        page = requests.get(url)
        tree = etree.fromstring(page.text, self.parser)

        self.anime.title = slugify(tree.xpath('//h1/text()')[0], separator=" ")

        qualities = tree.xpath('//*[@data-parent="download_box2" and @data-tab]')
        for i in qualities:
            self.anime.qualities.append(i.text)

        self.anime.links += tree.xpath('//*[@class="uk-switcher donws_link"]')

    def select_quality(self, index):
        if index > len(self.anime.qualities):
            return False
        self.quality = index
        links = self.anime.links[index].find("li").findall("a")
        self.anime.links = []
        for link in links:
            self.anime.links += [link.attrib['href']]
