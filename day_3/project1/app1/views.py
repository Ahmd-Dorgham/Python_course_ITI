from django.http import HttpResponse

my_list_of_stuff = [
    {"id": 1, "title": "my cool book", "author": "me"},
    {"id": 2, "title": "another book", "author": "also me"},
]

def list_books(request):
    res = "<h1>books here</h1><ul>"
    for item in my_list_of_stuff:
        res = res + "<li>" + str(item['id']) + " - " + item['title'] + " " + item['author'] + "</li>"
    res = res + "</ul>"
    return HttpResponse(res)

def show_book(request, id):
    for item in my_list_of_stuff:
        if item["id"] == id:
            return HttpResponse("<h1>" + item['title'] + "</h1><p>" + item['author'] + "</p>")
    return HttpResponse("not found error thing")

def delete_book(request, id):
    for item in my_list_of_stuff:
        if item["id"] == id:
            my_list_of_stuff.remove(item)
            return HttpResponse("deleted book " + str(id))
    return HttpResponse("not found error thing")

def add_book(request):
    id = request.GET.get("id")
    for item in my_list_of_stuff:
        if item["id"] == id:
            return HttpResponse("already there")
    title = request.GET.get("title")
    author = request.GET.get("author")
    new_thing = {"id": int(id), "title": title, "author": author}
    my_list_of_stuff.append(new_thing)
    return HttpResponse("added")