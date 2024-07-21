from django import forms
from page.models import Page,Carousel

class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ['title','cover_image',]


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title','cover_image', 'content', 'status',]