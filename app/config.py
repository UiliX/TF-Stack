from flask_imp.config import ImpConfig, FlaskConfig

from app.globals import FLASK_SECRET_KEY

FLASK_CONFIG = FlaskConfig(
    secret_key=FLASK_SECRET_KEY,
)

# ImpConfig usually handles database configs
# in this case there are no database connections
IMP_CONFIG = ImpConfig()
