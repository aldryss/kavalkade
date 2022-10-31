from knappe.meta import HTTPMethodEndpointMeta
from knappe.decorators import html

class Base(metaclass=HTTPMethodEndpointMeta):

    def menu(request):
        return {}
