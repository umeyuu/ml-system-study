from database import Base
from sqlalchemy import Column, DateTime, ForeignKey, String, Text
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.types import JSON


# PROJECTSテーブル
class Project(Base):
    __tablename__ = 'project'
    project_id = Column(String(255), primary_key=True, comment='主キー')
    project_name = Column(String(255), nullable=False, unique=True, comment="プロジェクト名")
    description = Column(Text, nullable=True, comment="説明")
    created_datetime = Column(DateTime(timezone=True), server_default=current_timestamp(), nullable=False)
    

