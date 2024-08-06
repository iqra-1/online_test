# app/schemas.py
from pydantic import BaseModel
from typing import List, Optional


class UserBase(BaseModel):
    username: str


class UserCreate(BaseModel):
    username: str
    password: str


class User(UserBase):
    id: int

    model_config = {"from_attributes": True}


class TestBase(BaseModel):
    title: str
    description: str


class TestCreate(TestBase):
    pass


class Test(TestBase):
    id: int

    model_config = {"from_attributes": True}


class QuestionBase(BaseModel):
    text: str
    test_id: int


class QuestionCreate(QuestionBase):
    pass


class Question(QuestionBase):
    id: int

    model_config = {"from_attributes": True}


class AnswerBase(BaseModel):
    text: str
    is_correct: bool
    question_id: int


class AnswerCreate(AnswerBase):
    pass


class Answer(AnswerBase):
    id: int

    model_config = {"from_attributes": True}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class TestResults(BaseModel):
    test_id: int
    user_id: int
    score: float
    total_questions: int
    correct_answers: int

    model_config = {"from_attributes": True}


class TestResultsCreate(BaseModel):
    test_id: int
    user_id: int
    score: float
    total_questions: int
    correct_answers: int
