from functions.mysoup import soup
def has_class(tag):
    return tag.has_attr('class')

def has_id(tag):
    return tag.has_attr('id')
# passing by parameter id and class
def has_id_para(tag):
    return soup.find(id=tag)

def has_class_para(tag):
    return soup.find(class_=tag)

def has_content(tag):
    return tag.has_attr('content')

def has_class_not_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

def has_not_class_not_id(tag):
    return not tag.has_attr('class') and not tag.has_attr('id')