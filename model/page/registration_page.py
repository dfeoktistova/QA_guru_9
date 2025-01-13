from selene import browser, by, have
import os


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.user_number = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.month_of_birth = browser.element('[class="react-datepicker__month-select"]')
        self.year_of_birth = browser.element('[class="react-datepicker__year-select"]')
        self.day_of_birth = browser.element('[class="react-datepicker__day react-datepicker__day--011"]')
        self.subjects = browser.element('#subjectsInput')
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit_button = browser.element('#submit')
        self.close_button = browser.element('#closeLargeModal')

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def register(self, user):
        self.first_name.click().type(user.first_name)

        self.last_name.click().type(user.last_name)

        self.user_email.click().type(user.email)

        browser.element(by.text(user.gender.value)).click()

        self.user_number.click().type(user.user_number)

        self.date_of_birth.click()
        self.year_of_birth.click().element(by.text(user.birth_year)).click()
        self.month_of_birth.click().element(by.text(user.birth_month)).click()
        self.day_of_birth.click()

        self.subjects.click().type(user.subjects).press_enter()

        browser.element(by.text(user.hobbies.value)).click()

        path = os.path.dirname(os.path.abspath(__file__))
        self.picture.set_value(os.path.abspath(f'{path}/../../resources/{user.picture}'))

        self.address.click().type(user.address)

        self.state.click().element(by.text(user.state.value)).click()

        self.city.click().element(by.text(user.city.value)).click()

        self.submit_button.click()

    def should_have_registered(self, user):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.element("[class='table-responsive']").should(have.text(f'{user.first_name} {user.last_name}'))
        browser.element("[class='table-responsive']").should(have.text(user.email))
        browser.element("[class='table-responsive']").should(have.text(user.gender.value))
        browser.element("[class='table-responsive']").should(have.text(user.user_number))
        browser.element("[class='table-responsive']").should(
            have.text(f'{user.birth_day} {user.birth_month},{user.birth_year}'))
        browser.element("[class='table-responsive']").should(have.text(user.subjects))
        browser.element("[class='table-responsive']").should(have.text(user.hobbies.value))
        browser.element("[class='table-responsive']").should(have.text(user.picture))
        browser.element("[class='table-responsive']").should(have.text(user.address))
        browser.element("[class='table-responsive']").should(have.text(f'{user.state.value} {user.city.value}'))
