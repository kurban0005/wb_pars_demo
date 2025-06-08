import time

from django.shortcuts import render
import csv
from .parser.parser import ParseVideocards

def read_csv_file():
    data = []
    with open('main_app/parser/wb_data.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def all_gpu_asus(request):
    parser = ParseVideocards("https://www.wildberries.ru/brands/asus?sort=popular&page=1")
    parser.parse_all_videocards()
    data = read_csv_file()
    context = {
        'data': data,
        'category':'Видеокарты',
        'brand':'Asus'
    }
    return render(request, 'main_app/all_gpu.html', context)


def all_gpu_msi(request):
    parser = ParseVideocards("https://www.wildberries.ru/brands/msi?sort=popular&page=1")
    parser.parse_all_videocards()
    data = read_csv_file()
    context = {
        'data': data,
        'category':'Видеокарты',
        'brand':'MSI'
    }
    return render(request, 'main_app/all_gpu.html', context)


def all_gpu_gigabyte(request):
    parser = ParseVideocards("https://www.wildberries.ru/brands/gigabyte?sort=popular&page=1")
    parser.parse_all_videocards()
    data = read_csv_file()
    context = {
        'data': data,
        'category':'Видеокарты',
        'brand':'Gigabyte'
    }
    return render(request, 'main_app/all_gpu.html', context)


def gpu_12gb_gigabyte(request):
    parser = ParseVideocards("https://www.wildberries.ru/brands/gigabyte?sort=popular&page=1")
    parser.parse_12gb_videocard()
    data = read_csv_file()
    context = {
        'data': data,
        'category':'Видеокарты 12гб',
        'brand':'Gigabyte'
    }
    return render(request, 'main_app/all_gpu.html', context)


def gpu_12gb_asus(request):
    parser = ParseVideocards("https://www.wildberries.ru/brands/asus?sort=popular&page=1")
    parser.parse_12gb_videocard()
    data = read_csv_file()
    context = {
        'data': data,
        'category':'Видеокарты 12гб',
        'brand':'ASUS'
    }
    return render(request, 'main_app/all_gpu.html', context)


def gpu_12gb_msi(request):
    parser = ParseVideocards("https://www.wildberries.ru/brands/msi?sort=popular&page=1")
    parser.parse_12gb_videocard()
    data = read_csv_file()
    context = {
        'data': data,
        'category':'Видеокарты 12гб',
        'brand':'MSI'
    }
    return render(request, 'main_app/all_gpu.html', context)


def gpu_8gb_gigabyte(request):
    parser = ParseVideocards("https://www.wildberries.ru/brands/gigabyte?sort=popular&page=1")
    parser.parse_8gb_videocard()
    data = read_csv_file()
    context = {
        'data': data,
        'category':'Видеокарты 8гб',
        'brand':'Gigabyte'
    }
    return render(request, 'main_app/all_gpu.html', context)

def gpu_8gb_asus(request):
    parser = ParseVideocards("https://www.wildberries.ru/brands/asus?sort=popular&page=1")
    parser.parse_8gb_videocard()
    data = read_csv_file()
    context = {
        'data': data,
        'category':'Видеокарты 8гб',
        'brand':'ASUS'
    }
    return render(request, 'main_app/all_gpu.html', context)


def gpu_8gb_msi(request):
    parser = ParseVideocards("https://www.wildberries.ru/brands/msi?sort=popular&page=1")
    parser.parse_8gb_videocard()
    data = read_csv_file()
    context = {
        'data': data,
        'category':'Видеокарты 8гб',
        'brand':'MSI'
    }
    return render(request, 'main_app/all_gpu.html', context)


def mb_gigabyte(request):
    parser = ParseVideocards("https://www.wildberries.ru/brands/gigabyte?sort=popular&page=1")
    parser.parse_motherboards_ddr5()
    data = read_csv_file()
    context = {
        'data': data,
        'category':'Материнские платы на ddr5',
        'brand':'Gigabyte'
    }
    return render(request, 'main_app/all_gpu.html', context)

def mb_asus(request):
    parser = ParseVideocards("https://www.wildberries.ru/brands/asus?sort=popular&page=1")
    parser.parse_motherboards_ddr5()
    data = read_csv_file()
    context = {
        'data': data,
        'category':'Материнские платы на ddr5',
        'brand':'ASUS'
    }
    return render(request, 'main_app/all_gpu.html', context)

def mb_msi(request):
    parser = ParseVideocards("https://www.wildberries.ru/brands/msi?sort=popular&page=1")
    parser.parse_motherboards_ddr5()
    data = read_csv_file()
    context = {
        'data': data,
        'category':'Материнские платы на ddr5',
        'brand':'MSI'
    }
    return render(request, 'main_app/all_gpu.html', context)



def top_gigabyte(request):
    parser = ParseVideocards("https://www.wildberries.ru/brands/gigabyte?sort=popular&page=1")
    parser.parse_top_47()
    data = read_csv_file()
    context = {
        'data': data,
        'category':'Материнские платы на ddr5',
        'brand':'Gigabyte'
    }
    return render(request, 'main_app/all_gpu.html', context)

def top_asus(request):
    parser = ParseVideocards("https://www.wildberries.ru/brands/asus?sort=popular&page=1")
    parser.parse_top_47()
    data = read_csv_file()
    context = {
        'data': data,
        'category':'Материнские платы на ddr5',
        'brand':'ASUS'
    }
    return render(request, 'main_app/all_gpu.html', context)

def top_msi(request):
    parser = ParseVideocards("https://www.wildberries.ru/brands/msi?sort=popular&page=1")
    parser.parse_top_47()
    data = read_csv_file()
    context = {
        'data': data,
        'category':'Материнские платы на ddr5',
        'brand':'MSI'
    }
    return render(request, 'main_app/all_gpu.html', context)




def index(request):
    '''Домашняя страница.'''
    return render(request, 'main_app/index.html')
