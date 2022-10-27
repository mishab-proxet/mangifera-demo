from dataclasses import dataclass

from shared.model import BaseModel


@dataclass
class User(BaseModel):
    name: str
