from pydantic import BaseModel, ConfigDict


class Model(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    pass


class IdMixin(Model):
    id: int
