from bs4 import BeautifulSoup


def generate_new_html_errors(errors):
    soup = BeautifulSoup(str(errors), 'html.parser')
    tag_li = soup.find_all('li')[::2]

    dict_messages = {}

    for tag in tag_li:
        # Extraemos el mensaje
        msg = tag.select('li ul li')[0].get_text()

        # Extraemos el nombre del campo que validamos.
        str_tag = str(tag)
        start = str_tag.find('<li>') + len('<li>')
        end = str_tag.rfind('<ul')
        field_name = str_tag[start:end]

        # creamos el diccionario de errores.
        dict_messages[field_name] = msg

    return dict_messages




