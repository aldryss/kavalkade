import pathlib
from chameleon.zpt.template import PageTemplateFile
from chameleon.zpt.loader import TemplateLoader
from knappe.ui import SlotExpr, slot, UI, Layout
from knappe.request import RoutingRequest as Request
import typing as t
from knappe.decorators import html
from kavalkade.controllers.base import Base

PageTemplateFile.expression_types['slot'] = SlotExpr

@slot.register
@html('menu')
def menu(request: Request, view: t.Any, context: t.Any, name: t.Literal['menu']):
    return Base.menu(request)

ui = UI(
    templates = TemplateLoader(
        str(pathlib.Path(__file__).parent / "./templates"),
        default_extension=".pt"
    )
)

ui.layout = Layout(ui.templates["layout"])
