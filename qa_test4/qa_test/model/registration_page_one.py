import os

from selene.support.shared import browser
from selene import have

import tests



class RegistrationFormPage:
    def __init__(self):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.email = browser.element("#userEmail")
        self.gender = browser.all('[name=gender]').element_by(have.value('Male')).element('..')
        self.phone_number = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        #self.date_of_birth_day = browser.element(f'.react-datepicker__day--0{self.date_of_birth_day}').click()
        #self.date_of_birth_month = browser.element('.react-datepicker__month-select')
        #self.date_of_birth_year = browser.element('.react-datepicker__year-select')
        self.subject = browser.element('#subjectsInput')
        #self.hobby = browser.element('[for=hobbies-checkbox-3]')
        self.upload_filename = browser.element('#uploadPicture')
        self.currentAddress = browser.element('#currentAddress')

    @staticmethod
    def page_open():
        browser.open("/automation-practice-form")

    def type_first_name(self, first_name):
        self.first_name.type(first_name)

    def type_last_name(self, last_name):
        self.last_name.type(last_name)

    def type_email(self, email):
        self.email.type(email)

    def choose_gender(self, value):
        self.gender.click()

    def type_phone_number(self, phone_number):
        self.phone_number.type(phone_number)


    #def input_date_of_birth(self, date_of_birth_day, date_of_birth_month, date_of_birth_year):
     #self.date_of_birth.click()
     #self.date_of_birth_month.type(date_of_birth_month)
     #self.date_of_birth_year.type(date_of_birth_year)
     #self.date_of_birth_day(date_of_birth_day)



    def type_subject(self, subject):
      self.subject.type(subject).press_enter()


    def choose_hobby(self, hobby):
      self.hobby.click()

    def upload_picture(self, upload_filename):
      self.upload_filename.type(os.path.abspath(os.path.join(os.path.dirname(tests.__file__), 'resources/py.jpg')))


    def type_currentAddress(self, currentAddress):
      self.currentAddress.type(currentAddress)
