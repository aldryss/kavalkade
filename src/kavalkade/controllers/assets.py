from knappe.response import Response
from knappe.utils import file_iterator
from ..assets import assets_path

#@ToDo : Theme handling to match current game
class Assets():
    def stylesheet(request):
        return Response.from_file_iterator(filename='style.css', body=file_iterator(assets_path / 'style.css'))

    def js(request):
        return Response.from_file_iterator(filename='app.js', body=file_iterator(assets_path / 'app.js'))

