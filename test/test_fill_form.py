from model.page.registration_page import RegistrationPage
from model.user.user import user


def test_fill_form():
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.register(user)
    registration_page.should_have_registered(user)


