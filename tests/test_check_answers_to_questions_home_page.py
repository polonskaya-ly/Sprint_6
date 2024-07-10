import pytest
import allure
from ..constants import Constants
from ..pages.home_page import HomePage


@pytest.mark.usefixtures("driver")
class TestCheckAnswers:
    @pytest.mark.parametrize('question, answer', [(Constants.questions[0], Constants.answers[0]),
                                                  (Constants.questions[1], Constants.answers[1]),
                                                  (Constants.questions[2], Constants.answers[2]),
                                                  (Constants.questions[3], Constants.answers[3]),
                                                  (Constants.questions[4], Constants.answers[4]),
                                                  (Constants.questions[5], Constants.answers[5]),
                                                  (Constants.questions[6], Constants.answers[6]),
                                                (Constants.questions[7], Constants.answers[7])])
    @allure.title("Соотвествие вопроса и ответа")
    def test_check_answers(self, question, answer):
        home_page = HomePage(self.driver)
        home_page.check_answers_to_questions(question,answer)
