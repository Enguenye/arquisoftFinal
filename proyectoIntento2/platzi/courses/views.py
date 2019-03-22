
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Courses
from .models import Cajas
from .models import Productos


@method_decorator(csrf_exempt, name='dispatch')
class CourseList(ListView):
    model = Courses


@method_decorator(csrf_exempt, name='dispatch')
class CourseDetail(DetailView):
    model = Courses


@method_decorator(csrf_exempt, name='dispatch')
class CourseCreation(CreateView):
    model = Courses
    success_url = reverse_lazy('courses:list')
    fields = ['fecha', 'cantidad','tipo']


@method_decorator(csrf_exempt, name='dispatch')
class CourseUpdate(UpdateView):
    model = Courses
    success_url = reverse_lazy('courses:list')
    fields = ['fecha', 'cantidad', 'tipo']


@method_decorator(csrf_exempt, name='dispatch')
class CourseDelete(DeleteView):
    model = Courses
    success_url = reverse_lazy('courses:list')


@method_decorator(csrf_exempt, name='dispatch')
class CajaList(ListView):
    model = Cajas


@method_decorator(csrf_exempt, name='dispatch')
class CajaDetail(DetailView):
    model = Cajas


@method_decorator(csrf_exempt, name='dispatch')
class CajaCreation(CreateView):
    model = Cajas
    success_url = reverse_lazy('courses:list')
    fields = ['identificador', 'certificada']


@method_decorator(csrf_exempt, name='dispatch')
class CajaUpdate(UpdateView):
    model = Cajas
    success_url = reverse_lazy('courses:list')
    fields = ['identificador', 'certificada']


@method_decorator(csrf_exempt, name='dispatch')
class CajaDelete(DeleteView):
    model = Cajas
    success_url = reverse_lazy('courses:list')


@method_decorator(csrf_exempt, name='dispatch')
class ProductoList(ListView):
    model = Productos


@method_decorator(csrf_exempt, name='dispatch')
class ProductoDetail(DetailView):
    model = Productos


@method_decorator(csrf_exempt, name='dispatch')
class ProductoCreation(CreateView):
    model = Productos
    success_url = reverse_lazy('courses:list')
    fields = ['identificador', 'precio','cantidad']


@method_decorator(csrf_exempt, name='dispatch')
class ProductoUpdate(UpdateView):
    model = Productos
    success_url = reverse_lazy('courses:list')
    fields = ['identificador', 'precio', 'cantidad']


@method_decorator(csrf_exempt, name='dispatch')
class ProductoDelete(DeleteView):
    model = Productos
    success_url = reverse_lazy('courses:list')
