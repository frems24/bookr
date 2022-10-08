from django.http import HttpResponse


def index(request):
    name = request.GET.get("name") or "świecie"
    return HttpResponse(f"Witaj, {name}!")
