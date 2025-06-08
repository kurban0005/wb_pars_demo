import requests
import re
import csv
from main_app.parser.models import Products


class ParseVideocards:
    def __init__(self, url: str):
        self.brand_id = self.__get_brand_id(url)

    @staticmethod
    def __get_brand_id(url: str):
        regex = "(?<=brands).+(?=sort)"
        brand = re.search(regex, url)
        if not brand:
            raise ValueError("Не удалось извлечь brand ID из URL.")
        list1 = list(brand[0])
        list2 = list1[1:-1]
        brand_name = ''.join(list2)
        print(brand_name)
        response = requests.get(f'https://static-basket-01.wbbasket.ru/vol0/data/brands/{brand_name}.json')
        if response.status_code != 200:
            raise ValueError(f"Не удалось получить данные бренда: {response.status_code}")
        brand_id = response.json().get("id")
        print(brand_id)
        return brand_id

    def parse_all_videocards(self):
        _page = 1
        self.__create_csv()
        while True:
            params = {
                'ab_testing': 'false',
                'appType': '1',
                'brand': f'{self.brand_id}',
                'curr': 'rub',
                'dest': '123585706',
                'hide_dtype': '13',
                'lang': 'ru',
                'page': f'{_page}',
                'sort': 'popular',
                'spp': '30',
                'xsubject': '3274',
            }
            response = requests.get('https://catalog.wb.ru/brands/v2/catalog', params=params)
            if response.status_code != 200:
                print(f"Ошибка запроса: {response.status_code}")
                break
            items_info = Products(**response.json()["data"])
            if not items_info.products:
                break
            self.__save_csv(items_info)
            _page += 1

    def parse_12gb_videocard(self):
        _page = 1
        self.__create_csv()
        while True:
            params = {
                'ab_testing': 'false',
                'appType': '1',
                'brand': f'{self.brand_id}',
                'curr': 'rub',
                'dest': '123585706',
                'hide_dtype': '13',
                'lang': 'ru',
                'page': f'{_page}',
                'sort': 'popular',
                'spp': '30',
                'xsubject': '3274',
                'f74650': '608963',
            }
            response = requests.get('https://catalog.wb.ru/brands/v2/catalog', params=params)
            if response.status_code != 200:
                print(f"Ошибка запроса: {response.status_code}")
                break
            items_info = Products(**response.json()["data"])
            if not items_info.products:
                break
            self.__save_csv(items_info)
            _page += 1

    def parse_8gb_videocard(self):
        _page = 1
        self.__create_csv()
        while True:
            params = {
                'ab_testing': 'false',
                'appType': '1',
                'brand': f'{self.brand_id}',
                'curr': 'rub',
                'dest': '123585706',
                'hide_dtype': '13',
                'lang': 'ru',
                'page': f'{_page}',
                'sort': 'popular',
                'spp': '30',
                'xsubject': '3274',
                'f74650': '80586',
            }
            response = requests.get('https://catalog.wb.ru/brands/v2/catalog', params=params)
            if response.status_code != 200:
                print(f"Ошибка запроса: {response.status_code}")
                break
            items_info = Products(**response.json()["data"])
            if not items_info.products:
                break
            self.__save_csv(items_info)
            _page += 1

    def parse_motherboards_ddr5(self):
        _page = 1
        self.__create_csv()
        while True:
            params = {
                'ab_testing': 'false',
                'appType': '1',
                'brand': f'{self.brand_id}',
                'curr': 'rub',
                'dest': '123585706',
                'hide_dtype': '13',
                'lang': 'ru',
                'page': f'{_page}',
                'sort': 'popular',
                'spp': '30',
                'xsubject': '3690',
                'f143479': '764274091',
            }
            response = requests.get('https://catalog.wb.ru/brands/v2/catalog', params=params)
            if response.status_code != 200:
                print(f"Ошибка запроса: {response.status_code}")
                break
            items_info = Products(**response.json()["data"])
            if not items_info.products:
                break
            self.__save_csv(items_info)
            _page += 1

    def parse_top_47(self):
        _page = 1
        self.__create_csv()
        while True:
            params = {
                'ab_testing': 'false',
                'appType': '1',
                'brand': f'{self.brand_id}',
                'curr': 'rub',
                'dest': '123585706',
                'frating': '1',
                'hide_dtype': '13',
                'lang': 'ru',
                'page': f'{_page}',
                'sort': 'popular',
                'spp': '30',
            }
            response = requests.get('https://catalog.wb.ru/brands/v2/catalog', params=params)
            if response.status_code != 200:
                print(f"Ошибка запроса: {response.status_code}")
                break
            items_info = Products(**response.json()["data"])
            if not items_info.products:
                break
            self.__save_csv(items_info)
            _page += 1


    @staticmethod
    def __create_csv():
        with open("main_app/parser/wb_data.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'название', 'бренд', 'цена', 'скидка', 'наличие', 'рейтинг'])

    @staticmethod
    def __save_csv(items: Products):
        with open("main_app/parser/wb_data.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for product in items.products:
                for size in product.sizes:
                    writer.writerow([
                        product.id,
                        product.name,
                        product.brand,
                        size.price.basic,
                        size.price.total,
                        product.volume,
                        product.rating
                    ])

# if __name__ == "__main__":
#     ParseVideocards("https://www.wildberries.ru/brands/msi?sort=popular&page=1&xsubject=3274").parse_all_videocards()
