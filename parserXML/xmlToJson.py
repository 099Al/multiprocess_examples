#convertor
import json
import re
from bs4 import BeautifulSoup
import lxml
import unicodedata

def xmlToJson(dict):
    return json.dumps(dict)

def xmltodict(content,first_tag='fullstudy'):
    """
    :param content:  Content from xml-file
    :param first_tag: first element, which should be removed
    :return: dictinory
    """

    #Content from xml File
    content = re.sub('\n', '', content)
    content = re.sub('\r', '', content)
    content = re.sub('>\s+<', '><', content)
    data = unicodedata.normalize('NFKD', content)
    soup = BeautifulSoup(data, 'lxml')

    body = soup.find('body')

    if(first_tag.strip()!=''):
        struct = body.find(first_tag)
    else:
        struct=body

    if struct is None:
        print(f'tag "{first_tag}" is not found')
        #raise Exception (f'the element {first_tag} not found')
        return None
    else:
        return parserXML(struct)

def parserXML(struct):
    struct_all = struct.findAll(True, recursive=False)
    struct_dict = {}
    for strc in struct_all:
        tag = strc.name
        tag_name_prop = strc.attrs['name']


        if tag == 'struct':
            d = parserXML(strc)
            el = {tag_name_prop: d}
            struct_dict.update(el)
        elif tag == 'field':
            v = strc.text
            struct_dict[tag_name_prop] = v
        elif tag == 'list':
            l_elem = []
            for child in strc.contents:
                soap_child = BeautifulSoup(str(child), 'lxml').find('body')
                l_elem.append(parserXML(soap_child))
                el = {tag_name_prop: l_elem}
                struct_dict.update(el)
    return struct_dict



def parcerXML(row):
    filename = row['filename']
    content = row['content']
    dict_study = xmltodict(content,first_tag='fullstudy')
    return Row(std=dict_study)