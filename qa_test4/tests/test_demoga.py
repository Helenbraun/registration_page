from selene import browser, have, be

from qa_test.model.registration_page_one import RegistrationFormPage
from qa_test.model.user_data import User, Subjects

from qa_test.model import registration_page_one


# GIVEN
def test_authorization(in_browser):
    user = User(
        first_name='Test',
        last_name='Testovuy',
        email='Perty@mail.ru',
        gender='Male',
        phone_number='89078905674',
        date_of_birth_year='1990',
        date_of_birth_month='May',
        date_of_birth_day='23',
        hobby='Sports',
        subject=Subjects.biology.value,
        upload_filename='../resourses/py.jpg',
        currentAddress='Avenu',
        state="NCR",
        city='Karnal'
    )

    registration_page = RegistrationFormPage()
    registration_page.page_open()


    registration_page.type_first_name(user.first_name)
