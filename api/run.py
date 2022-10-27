import json
import logging
from dataclasses import asdict

from api.models import User


if __name__ == "__main__":
    user = User(name="Misha", id=0)
    logging.warning(json.dumps(asdict(user), indent=2, sort_keys=True))