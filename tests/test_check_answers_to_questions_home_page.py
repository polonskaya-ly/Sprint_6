import pytest
import allure
from ..constraints import Constraints
from ..pages.home_page import HomePage


@pytest.mark.usefixtures("driver")
class TestCheckAnswers:

    driver = None

    @pytest.mark.parametrize('question, answer', [(Constraints.questions[0], Constraints.answers[0]),
                                                  (Constraints.questions[1], Constraints.answers[1]),
                                                  (Constraints.questions[2], Constraints.answers[2]),
                                                  (Constraints.questions[3], Constraints.answers[3]),
                                                  (Constraints.questions[4], Constraints.answers[4]),
                                                  (Constraints.questions[5], Constraints.answers[5]),
                                                  (Constraints.questions[6], Constraints.answers[6]),
                                                (Constraints.questions[7], Constraints.answers[7])])
    @allure.title("Соотвествие вопроса и ответа")
    def test_check_answers(self, question, answer):
        home_page = HomePage(self.driver)
        home_page.check_answers_to_questions(question,answer)
