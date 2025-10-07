РАБОЧИЙ ТЕСТ 
без PJ
def open():
    browser.open("https://demoqa.com/automation-practice-form")


    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys('month')
        browser.element('.react-datepicker__year-select').send_keys('year')
        browser.element(f'.react-datepicker__day--0{day}').click()


def test_correct_completion():
    registration_page = RegistrationFormPage()
    registration_page.open()

    type_first_name('Test')

    browser.element("#lastName").type("Testov")
    browser.element("#userEmail").type("Test@mail.ru")
    # browser.element('[name=gender][value=Male]+label').click()
    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
    browser.element('#userNumber').type('89067894556')
    browser.element('#subjectsInput').type('Commerce').press_enter()
    browser.element('[for=hobbies-checkbox-3]').perform(command.js.scroll_into_view)
    browser.element('[for=hobbies-checkbox-3]').click()
    # browser.element('#react - select - 3 - input').element_by(have.exact_text('Uttar Pradesh')).click()
    browser.element('#currentAddress').type('Moscow')

    registration_page.fill_date_of_birth('1999', 'March', '20')

    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(tests.__file__), 'resources/py.jpg')))
    browser.element('#submit').click()

    browser.element('.table').all('td').even.should(
        have.exact_texts('Test Testov', 'Test@mail.ru', 'Male', '8906789455', '20 March,1999', 'Commerce', 'Music',
                         'py.jpg', 'Moscow', ''))
