from django.shortcuts import render
from django.views.generic import View, TemplateView, DeleteView, CreateView,ListView
from .models import Product
from .form import ProductForm
from django.http import HttpResponseRedirect, StreamingHttpResponse
import csv
from wsgiref.util import FileWrapper
import os

class Index(ListView):
    template_name = 'index.html'
    model = Product
    def get(self, request, *args, **kwargs):
        context = {
            'page_title': 'Хранилище товаров',
            'stored_products': self.model.objects.all()
        }
        return render(request, self.template_name, context)


class AddProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_new_product.html'
    title = 'Добавить товар'
    success_url = '/'
    def get(self, request, *args, **kwargs):
        context = {
            'page_title': 'Добавление товара',
            'form': self.form_class
        }
        return render(request, self.template_name, context)



def file_output(request):
    context = {
        'page_title': 'Подготовка файла CSV',
    }
    return render(request, 'output_csv_form.html', context)



def download(request):
    if request.method == 'GET':
        with open('output_files/output.csv', 'w', encoding='utf-8') as file:
            file_writer = csv.writer(file)
            for data in Product.objects.all():
                file_writer.writerow(data.name)
        file.close()

    file_link = 'output_files/output.csv'
    filename = os.path.basename(file_link)

    response = StreamingHttpResponse(FileWrapper(open(file_link, 'rb'), 8192), content_type="text/csv")
    response['Content-Length'] = os.path.getsize(file_link)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response