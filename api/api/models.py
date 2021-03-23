from sqlalchemy import Column, DateTime, Integer, String

from .database import Base


class Person(Base):
    __tablename__ = "person"

    person_id = Column(Integer, primary_key=True)
    gender_concept_id = Column(Integer, nullable=False)
    birth_datetime = Column(DateTime, nullable=False)
    race_concept_id = Column(Integer, nullable=False)
    ethnicity_concept_id = Column(Integer, nullable=False)


class VisitOccurrence(Base):
    __tablename__ = "visit_ocurrence"

    visit_occurrence_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    visit_concept_id = Column(Integer, nullable=False)
    visit_start_datetime = Column(DateTime, nullable=False)
    visit_end_datetime = Column(DateTime, nullable=False)


class ConditionOccurrence(Base):
    __tablename__ = "condition_occurrence"

    person_id = Column(Integer, nullable=False)
    condition_concept_id = Column(Integer, primary_key=True)
    condition_start_datetime = Column(DateTime, nullable=False)
    condition_end_datetime = Column(DateTime, nullable=False)
    visit_occurrence_id = Column(Integer, nullable=False)


class DrugExposure(Base):
    __tablename__ = "drug_exposure"

    drug_exposure_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    drug_concept_id = Column(Integer, nullable=False)
    drug_exposure_start_datetime = Column(DateTime, nullable=False)
    drug_exposure_end_datetime = Column(DateTime, nullable=False)
    visit_ocurrence_id = Column(Integer, nullable=False)


class Concept(Base):
    __tablename__ = "concept"

    concept_id = Column(Integer, primary_key=True)
    concept_name = Column(String, nullable=False)
    domain_id = Column(String, nullable=False)


class Death(Base):
    __tablename__ = "death"

    person_id = Column(Integer, primary_key=True)
    death_date = Column(DateTime, nullable=False)
