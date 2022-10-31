from knappe.routing import Router

from kavalkade.controllers.index import Index
from kavalkade.controllers.profile import Profile
from kavalkade.controllers.assets import Assets

router = Router()

router.register('/')(Index)
router.register('/profile')(Profile)
router.register('/style.css')(Assets.stylesheet)
router.register('/app.js')(Assets.js)
#router.register('/images/{image}')(Assets.image)
