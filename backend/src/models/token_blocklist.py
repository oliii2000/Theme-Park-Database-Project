from datetime import datetime
from sqlmodel import SQLModel, Field

class TokenBlocklist(SQLModel, table=True):
    __tablename__ = "token_blocklist"
    
    jti: str = Field(primary_key=True, nullable=False, max_length=400)
    expiry_at: datetime = Field(nullable=False)