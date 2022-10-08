from django.shortcuts import render


def index(request):
    name = request.GET.get("name") or "świecie"
    return render(request, "base.html", {"name": name})
