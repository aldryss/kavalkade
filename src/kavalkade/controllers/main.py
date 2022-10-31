from knappe.decorators import html
from . import router

@router.register('/')
@html('index')
def main(self, request):
    return {}