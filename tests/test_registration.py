import os
from selene import browser, have


def test_registration_with_valid_data():
    browser.open("/automation-practice-form")

    # WHEN
    browser.element("#firstName").type("Lasha")
    browser.element("#lastName").type("Bas")
    browser.element("#userEmail").type("lasha@mail.ru")
    browser.element('[value="Female"] + label').click()
    browser.element("#userNumber").type("79263530000")

    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click()
    browser.all(".react-datepicker__month-select option").element_by(
        have.exact_text("September")
    ).click()
    browser.element(".react-datepicker__year-select").click()
    browser.all(".react-datepicker__year-select option").element_by(
        have.exact_text("2001")
    ).click()
    browser.all(".react-datepicker__day").element_by(have.exact_text("15")).click()

    browser.element("#subjectsInput").type("Computer Science").press_enter()
    browser.all("[for^=hobbies]").element_by(have.exact_text("Reading")).click()
    browser.element("#uploadPicture").type(f"{os.getcwd()}/Grogu.jpg")

    browser.element("#currentAddress").type("Bolshaya Sadovaya Street 302-bis")
    browser.element("#state").click()
    browser.all("#state div").element_by(have.exact_text("NCR")).click()
    browser.element("#city").click()
    browser.all("#city div").element_by(have.exact_text("Delhi")).click()

    browser.element("#submit").press_enter()

    # THEN
    browser.element(".modal-title").should(have.text("Thanks for submitting the form"))
    browser.all(".table").all("td").should(
        have.exact_texts(
            ("Student Name", "User Test"),
            ("Student Email", "test@ya.ru"),
            ("Gender", "Female"),
            ("Mobile", "7123456789"),
            ("Date of Birth", "15 September,2001"),
            ("Subjects", "Computer Science"),
            ("Hobbies", "Reading"),
            ("Picture", "Grogu.jpg"),
            ("Address", "Bolshaya Sadovaya Street 302-bis"),
            ("State and City", "NCR Delhi"),
        )
    )
