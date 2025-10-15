from selene import browser, have, be

from qa_test.model.registration_page_one import RegistrationFormPage
from qa_test.model.user_data import User, Subjects




# GIVEN
def test_authorization(in_browser):
    student = User(
        first_name="Test",
        last_name='Testovuy',
        email='Perty@mail.ru',
        gender='Male',
        phone_number='89078905674',
        date_of_birth_year='1990',
        date_of_birth_month='Oct',
        date_of_birth_day='23',
        subject=Subjects.biology,
        hobby='Music',
        upload_filename='../resourses/py.jpg',
        currentAddress='Avenu',
        state="NCR",
        city='Karnal'
    )

    registration_page = RegistrationFormPage()
    registration_page.page_open()

    registration_page.type_first_name(student.first_name)
    registration_page.type_last_name(student.last_name)
    registration_page.type_email(student.email)
    registration_page.choose_gender(student.gender)
    registration_page.type_phone_number(student.phone_number)
    #registration_page.input_date_of_birth(student.date_of_birth_day, student.date_of_birth_month, student.date_of_birth_year)
    registration_page.type_subject(student.subject.value)
    registration_page.choose_hobby(student.hobby)
    registration_page.upload_picture(student.upload_filename)

    registration_page.submit_form()

