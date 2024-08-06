# app/models.py
from sqlalchemy import Column, Float, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(128))
    is_admin = Column(Boolean, default=False)


class Test(Base):
    __tablename__ = "tests"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    description = Column(String(255))


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(255), index=True)
    test_id = Column(Integer, ForeignKey("tests.id"))

    test = relationship("Test", back_populates="questions")


class Answer(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(255), index=True)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("questions.id"))

    question = relationship("Question", back_populates="answers")


Test.questions = relationship("Question", order_by=Question.id, back_populates="test")
Question.answers = relationship("Answer", order_by=Answer.id, back_populates="question")


class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, index=True)
    test_id = Column(Integer, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    score = Column(Float)
    total_questions = Column(Integer)
    correct_answers = Column(Integer)
    user = relationship("User")
