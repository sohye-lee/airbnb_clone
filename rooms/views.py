# from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import render
# from django.http import Http404
# from django.shortcuts import render, redirect
# from django.urls import reverse
from . import models

class HomeView(ListView):
    model = models.Room
    paginate_by = 10
    paginate_orphans = 3
    ordering = "created"
    page_kwarg = 'page'
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # now = timezone.now() 
        # context["now"] = now
        return context

# CLASS VIEW
class RoomDetail(DetailView):
    model = models.Room
    

class EditRoomView(UpdateView):
    model = models.Room
    template_nme = "rooms/room_edit.html"
    fields = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
    )

def search(request):
    return render(request, "books/search.html")


# FUNCTION VIEW
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         # return redirect(reverse("core:home")) <--* to home (always should use reverse)*-->
#         raise Http404()





# from math import ceil
# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator, EmptyPage
# from . import models

# def all_rooms(request):

    # ===== MANUAL =====
    # page = request.GET.get('page', 1)
    # page = int(page or 1)
    # page_size = 10
    # limit = page_size * page
    # offset = page_size * (page - 1)
    # all_rooms = models.Room.objects.all()[offset:limit]
    # page_count = ceil(models.Room.objects.count() / page_size)
    # return render(request, "rooms/all_rooms.html", context={'rooms': all_rooms, 'page': page, "page_count": page_count, "page_range": range(1, page_count+1)})

    # ===== WITH DJANGO =====
    # page = request.GET.get('page')
    # room_list = models.Room.objects.all()
    # paginator = Paginator(room_list, 10, orphans=3)
    # rooms = paginator.get_page(page)

    # ===== IF DEBUG WANTED WITH PAGENUMBER =====
    # page = request.GET.get('page', 1)
    # room_list = models.Room.objects.all()
    # paginator = Paginator(room_list, 10, orphans=3)
    # try:
    #     rooms = paginator.page(int(page))
    #     return render(request, "rooms/all_rooms.html", { "pages": rooms })
    # except EmptyPage:
    #     return redirect("/")