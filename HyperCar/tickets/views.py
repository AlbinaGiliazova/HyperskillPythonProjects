from django.views import View
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from collections import deque

queue = {"change_oil": deque(),
         "inflate_tires": deque(),
         "diagnostic": deque()}
id = 0
next = None

def calc_queue(queue, link):
    res = len(queue["change_oil"]) * 2
    if link == "change_oil":
        return res
    res += len(queue["inflate_tires"]) * 5
    if link == "inflate_tires":
        return res
    res += len(queue["diagnostic"]) * 30
    return res

def process_queue(queue):
    if queue["change_oil"]:
        return queue["change_oil"].popleft()
    if queue["inflate_tires"]:
        return queue["inflate_tires"].popleft()
    if queue["diagnostic"]:
        return queue["diagnostic"].popleft()

class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        html = '<h2>Welcome to the Hypercar Service!</h2>'
        return HttpResponse(html)


class MenuView(TemplateView):
    template_name = "tickets\\menu.html"


class TicketView(View):

    def get(self, request, link, *args, **kwargs):
        link = link.split("//")[-1]
        time = calc_queue(queue, link)
        global id
        id += 1
        queue[link].append(id)
        context = {"ticket_number": id,
                   "minutes_to_wait": time}
        return render(request, "tickets\\ticket.html",
                      context=context)

class ProcessingView(View):

    def get(self, request, *args, **kwargs):
        context = {"change_oil_queue": len(queue["change_oil"]),
                   "inflate_tires_queue": len(queue["inflate_tires"]),
                   "diagnostic_queue": len(queue["diagnostic"])}
        return render(request, "tickets\\processing.html",
                      context=context)

    def post(self, request, *args, **kwargs):
        global next
        next = process_queue(queue)
        return redirect("/next")

class NextView(View):

    def get(self, request, *args, **kwargs):
        if next:
            context = {"next": next}
            return render(request, "tickets\\next.html",
                      context=context)
        else:
            return render(request, "tickets\\no_next.html")
