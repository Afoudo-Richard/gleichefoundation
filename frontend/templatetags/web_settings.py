import json
from django import template
from gleichefoundation.settings import BASE_DIR


register = template.Library()


# @register.simple_tag(takes_context=True)
# def settings(context):
#     try:
#         settings_file = open(f'{BASE_DIR}/web_settings.json', "r")
#         settings_data = json.load(settings_file)
#         context = {**context, **settings_data}
#     except:
#         raise Exception("The setting  web_settings.json file")

#     return "asdf asdfasdfasd fasdf asdfa"


@register.simple_tag
def settings(arg):
    try:
        settings_file = open(f'{BASE_DIR}/web_settings.json', "r")
        settings_data = json.load(settings_file)
        data = settings_data[arg]

        settings_file.close
    except:
        raise Exception(f"The setting {arg} is not present in web_settings.json file")

    return data