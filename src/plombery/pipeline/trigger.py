from datetime import datetime
from typing import Optional, Any

from apscheduler.triggers.base import BaseTrigger
from pydantic import BaseModel


class Trigger(BaseModel):
    id: str
    name: str
    schedule: BaseTrigger
    description: Optional[str] = __doc__
    params: Any = None
    paused: bool = False
    next_fire_time: Optional[datetime] = None

    class Config:
        arbitrary_types_allowed = True

        json_encoders = {
            BaseTrigger: lambda v: str(v),
        }
