from pydantic import BaseModel, StrictInt, StrictStr, StrictBool

class PostUserResponseSuccess(BaseModel):
    value: StrictBool

class PostUserResponseError(BaseModel):
    code: StrictInt
    message: StrictStr