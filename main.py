# ЗАДАЧА-1
import requests

# возвращает отфильтрованный список geo_logs, содержащий только визиты из России


def create_list(geo_logs):
    filtred_list = []
    for visit in geo_logs:
        for country in visit.values():
            if 'Россия' in country:
                filtred_list.append(visit)

    return filtred_list


# выводит все уникальные гео-ID из значений словаря ids
def unique_numbers(ids):
    unique_values = []
    for value in ids.values():
        for number in value:
            if number not in unique_values:
                unique_values.append(number)
    return unique_values


# возвращает название канала с максимальным объемом
def maximum_volume(stats):
    max_amount = 0
    for title, amount in stats.items():
        if amount > max_amount:
            max_amount = amount
            top_title = title
    return top_title


# ЗАДАЧА-2

with open('token_yd.txt', 'r') as file_object:
    token_yd = file_object.read().strip()


class YaUploader:
    def __init__(self):
        self.token_yd = token_yd

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token_yd)
        }

# создание папки на я-диске
    def create_folder(self, path):
        headers = self.get_headers()
        folder_url = "https://cloud-api.yandex.net/v1/disk/resources"
        response = requests.put(f'{folder_url}?path={path}', headers=headers)

        return response

# удаление папки на я-диске
    def delete_folder(self, path):
        headers = self.get_headers()
        folder_url = "https://cloud-api.yandex.net/v1/disk/resources"
        response = requests.delete(f'{folder_url}?path={path}', headers=headers)

        return response

# проверка папки на наличие
    def get_folder(self, path):
        headers = self.get_headers()
        folder_url = "https://cloud-api.yandex.net/v1/disk/resources"
        response = requests.get(f'{folder_url}?path={path}', headers=headers)

        return response
