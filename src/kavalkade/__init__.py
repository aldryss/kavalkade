#Python stuff
import typing as t
from autoroutes import Routes
from dataclasses import dataclass, field
from tinydb import TinyDB

#UI Related
import pathlib
from chameleon.zpt.loader import TemplateLoader
from knappe.ui import SlotExpr, UI, Layout

#Ponies, horses and squires
from horseman.mapping import RootNode
from knappe.pipeline import Pipeline
from knappe.request import RoutingRequest as Request
from knappe.response import Response
from knappe.routing import Router
from knappe.types import Middleware

@dataclass
class Kavalkade(RootNode):
    database: TinyDB
    router: Router = field(default_factory=Router)
    middlewares: t.Iterable[Middleware] = field(default_factory=tuple)

    def __post_init__(self, middlewares=()):
        self.pipeline: Pipeline[Request, Response] = Pipeline(
            self.middlewares
        )
        
    def resolve(self, path, environ):
        endpoint = self.router.match_method(path, environ['REQUEST_METHOD'])

        ui = UI(
            templates = TemplateLoader(
                str(pathlib.Path(__file__) / "templates"),
                default_extension=".pt"
            )
        )
        ui.layout = Layout(ui.templates["layout"])

        return self.pipeline(endpoint.handler)(
            Request(
                environ,
                app=self,
                endpoint=endpoint,
                context={"ui": ui}
            )
        )