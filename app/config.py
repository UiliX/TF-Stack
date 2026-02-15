from flask_imp.config import ImpConfig, FlaskConfig

FLASK_CONFIG = FlaskConfig(
    secret_key="02f65a5c46cf19b06833ad85cc7eab5f3d87e5c91164325f",
)

# ImpConfig usually handles database configs
# in this case there are no database connections
IMP_CONFIG = ImpConfig()
