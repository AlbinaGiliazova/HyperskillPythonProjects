from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views import View
from hypernews.settings import NEWS_JSON_PATH
import copy
import datetime
import json


def get_news():
    with open(NEWS_JSON_PATH) as json_file:
        news = json.load(json_file)
    return news


def get_dates(news, string=""):
    items = copy.deepcopy(news)
    items = sorted(items, key=lambda item: item["created"], reverse=True)
    for item in items:
        item["created"] = item["created"][:10]
    dates = dict()
    date = ""
    for item in items:
        if string and string not in item["title"]:  # search
            continue
        if item["created"] == date:
            dates[date].append(item)
        else:
            date = item["created"]
            dates[date] = [item]
    return dates


class ComingSoonView(View):
    def get(self, request, *args, **kwargs):
        html = \
'''
<title>HyperNews Page</title>
<h1>Coming soon</h1>
<a href="/news/" target="_blank">News</a>
'''
        # return HttpResponse(html)
        return redirect("/news/")


class NewsView(View):
    def get(self, request, link, *args, **kwargs):
        item = None
        link = int(link.strip("/").split("/")[-1])
        news = get_news()
        for i in news:
            if i['link'] == link:
                item = i
                break
        if not item:
            raise Http404
        return render(
            request, 'news/news.html', context={
                'item': item,
            })


class NewsListView(View):
    def get(self, request, *args, **kwargs):
        search = request.GET.get("q")
        news = get_news()
        dates = get_dates(news, search)
        context = {'dates': dates,}
        return render(
            request, 'news/index.html', context=context)


class NewsCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'news/create.html')

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        text = request.POST.get("text")
        created = datetime.datetime.now()
        created = created.strftime("%Y-%m-%d %H:%M:%S")
        news = get_news()
        link = len(news) + 1
        news.append({"created": created,
                     "text": text,
                     "title": title,
                     "link": link})
        with open(NEWS_JSON_PATH, "w") as json_file:
            json.dump(news, json_file)
        return redirect("/news/")
