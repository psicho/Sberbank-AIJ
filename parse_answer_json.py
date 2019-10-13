import json
import os

# Categorical files
text = {"tasks": []}
choice = {"tasks": []}
multiple_choice = {"tasks": []}
order = {"tasks": []}
matching = {"tasks": []}
other = {"tasks": []}


def json_load(file_name):
    json_file = []
    with open(file_name, "r") as newses:
        json_file = json.load(newses)

    return json_file


def sort_to_category(path_files='example/tests'):
    list_files = os.listdir(path=path_files)
    for file_name in list_files:
        # print(file_name)
        json_file = json_load(path_files + '/' + file_name)
        print(json_file)

        len_task = len(json_file['tasks'])
        for i in range(len_task):
            if json_file['tasks'][i]['question']['type'] == 'text':
                text["tasks"].append(json_file['tasks'][i])
            elif json_file['tasks'][i]['question']['type'] == 'choice':
                choice["tasks"].append(json_file['tasks'][i])
            elif json_file['tasks'][i]['question']['type'] == 'multiple_choice':
                multiple_choice["tasks"].append(json_file['tasks'][i])
            elif json_file['tasks'][i]['question']['type'] == 'order':
                order["tasks"].append(json_file['tasks'][i])
            elif json_file['tasks'][i]['question']['type'] == 'matching':
                matching["tasks"].append(json_file['tasks'][i])
            else:
                other["tasks"].append(json_file['tasks'][i])

            # print(json_file['tasks'][i]['id'])
    print('text["tasks"]', len(text["tasks"]), 'шт.')
    print('choice["tasks"]', len(choice["tasks"]), 'шт.')
    print('multiple_choice["tasks"]', len(multiple_choice["tasks"]), 'шт.')
    print('order["tasks"]', len(order["tasks"]), 'шт.')
    print('matching["tasks"]', len(matching["tasks"]), 'шт.')
    print('other["tasks"]', len(other["tasks"]), 'шт.')

# print(os.listdir(path="example/tests"))


sort_to_category()


