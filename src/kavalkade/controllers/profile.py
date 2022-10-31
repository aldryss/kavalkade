import colander
import deform
from knappe.response import Response
from knappe.routing import Router
from knappe_deform import FormPage, trigger
import re

def discord_handle(node, value):
    if type(value) is not str or not re.match(r'(.+)#([0-9]{4})', value):
        raise colander.Invalid('Value is not a Discord handle')

class ProfileSchema(colander.Schema):
    username = colander.SchemaNode(
        colander.String(),
        title="Pseudo"
    )

    discord = colander.SchemaNode(
        colander.String(),
        title="Handle Discord",
        validator=discord_handle
    )

class Profile(FormPage):

    schema = ProfileSchema

    @trigger('save', title="Sauvegarder")
    def save(self, request):
        try:
            form = self.get_form(request)
            appstruct = form.validate(request.data.form)
            
        except deform.exception.ValidationFailure as exception:
            return {
                "error" : None,
                "rendered_form": exception.render()
            }