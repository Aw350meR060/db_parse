""" Проверка сохранения порядка атрибутов посредством minidom_fixed """

import sys
from xml.dom import minidom
import minidom_fixed


def execute_test(prompt, document_class):
    """ Основной тест """
    print('*** {} ***'.format(prompt))
    dom = document_class()
    element = dom.createElement('test')
    element.setAttribute('name', 'id_CNTR_V')
    element.setAttribute('description', 'Первичный ключ таблицы CNTR_VID')
    element.setAttribute('type', 'LARGEINT')
    element.setAttribute('align', 'L')
    element.setAttribute('width', '11')
    dom.appendChild(element)
    dom.writexml(sys.stdout, '', '  ', '\n', 'utf-8')


execute_test('xml.dom.minidom', minidom.Document)
execute_test('minidom_fixed', minidom_fixed.Document)
