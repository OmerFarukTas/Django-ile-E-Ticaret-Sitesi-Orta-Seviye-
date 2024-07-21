from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from .models import Page ,Carousel
from django.contrib import messages
from .forms import CarouselForm ,PageForm
from django.contrib.admin.views.decorators import staff_member_required
from product.models import Category,Product

STATUS = 'published'

#User:
def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(status=STATUS).exclude(cover_image = '')
    context['products'] = Product.objects.filter(is_home=True,status=STATUS)
    return render(request,"home/index.html",context)  


def page_show(request,slug):
    context = dict()
    context['page']= get_object_or_404(Page,slug=slug)
    return render(request,'page/page.html',context)

#Admin:
@staff_member_required
def page_list(request):
    context = dict()
    context['page'] = Page.objects.all().order_by("-pk")
    return render(request,'manage/page_list.html',context)

def page_create(request):
    context = dict()
    context['title'] = "Page Create Form"
    context['form'] = PageForm()
    if request.method == "POST":
        form = PageForm(request.POST,request.FILES)
        print(form)
        if form.is_valid() == True:
            item = form.save(commit=False)
            item.slug = slugify(item.title.replace('ı','i'))
            item.save()
        messages.success(request, "Ekleme işlemi başarılı.")
    return render(request, "manage/page_create.html", context)

def page_update(request,pk):
    context = dict()
    item = Page.objects.get(pk=pk)
    context['title'] = f"title: {item.title} - pk:{item.pk} Page Update Form"
    context['form'] = PageForm(instance=item)
    if request.method == 'POST':
        form = PageForm(request.POST,request.FILES,instance=item)
        if form.is_valid() == True:
            item = form.save(commit=False)
            if item.slug == '':
                item.slug = slugify(item.title.replace('ı','i'))
            item.save()
            #return redirect('page_list')
            return redirect('page_update',pk)
        messages.success(request, "Güncelleme işlemi başarılı.")
    return render(request,'manage/page_create.html',context)

def page_delete(request,pk):
    item = Page.objects.get(pk=pk)
    item.status = "deleted"
    item.save()
    return redirect('page_list')

def manage_list(request):
    context = dict()
    return render(request,'manage/manage.html',context)

def carousel_list(request):
    context = dict()
    context['carousel'] = Carousel.objects.all().order_by("-pk")
    return render(request,'manage/carousel_list.html',context)

def carousel_update(request,pk):
    context = dict()
    item = Carousel.objects.get(pk=pk)
    context['title'] = f"title: {item.title} - pk:{item.pk} Carousel Update Form"
    context['form'] = CarouselForm(instance=item)
    if request.method == 'POST':
        form = CarouselForm(request.POST,request.FILES,instance=item)
        if form.is_valid() == True:
            form.save()
            #return redirect('carousel_list')
            return redirect('carousel_update',pk)
        messages.success(request, "Güncelleme işlemi başarılı.")
    return render(request,'manage/carousel_create.html',context)

def carousel_create(request):
    context = dict()
    context['title'] = "Carousel Create Form"
    context['form'] = CarouselForm()
    if request.method == "POST":
        form = CarouselForm(request.POST,request.FILES)
        print(form)
        if form.is_valid() == True:
            form.save()
        messages.success(request, "Ekleme işlemi başarılı.")
    return render(request, "manage/carousel_create.html", context)

def carousel_delete(request,pk):
    item = Carousel.objects.get(pk=pk)
    item.status = "deleted"
    item.save()
    return redirect("carousel_list")


