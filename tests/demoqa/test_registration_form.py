import allure, os
from selene import have,be, command


@allure.title("Successful fill form")
def test_successful(setup_browser):
    browser = setup_browser


    with allure.step("Открываем форму"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Заполняем форму"):
        # Имя, Фамилия, Имейл, Пол, номер телефона
        browser.element('[id=firstName]').should(be.blank).type('Elena')
        browser.element('[id=lastName]').should(be.blank).type('Pirogova')
        browser.element('[id=userEmail]').should(be.blank).type('123@123.ru')
        browser.element('[id^=gender-radio][value=Female]+label').click()
        browser.element('[id=userNumber]').should(be.blank).type('8987654321')
        # дата рождения, год, месяц, день
        browser.element('#dateOfBirthInput').click()
        browser.element('select[class^=react-datepicker__year]').send_keys('1989')
        browser.element('.react-datepicker__month-select').send_keys('January')
        browser.element('[aria-label= "Choose Monday, January 2nd, 1989"]').click()
        # предметы, хобби, картинка, адрес
        browser.element('#subjectsInput').send_keys('English')
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('English')).click()
        browser.element('[id="hobbies-checkbox-2"]+label').perform(command.js.scroll_into_view).click()
        browser.element('#uploadPicture').set_value(
            os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir, os.path.pardir, 'resources/image.png')))
        browser.element('[id=currentAddress]').should(be.blank).type('Kazakhstan')
        # штат, город, submit
        browser.element('#state').perform(command.js.scroll_into_view).click().all(
            '[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
        browser.element('#city').click()
        browser.element('[id="react-select-4-option-0"]').click()
        browser.element('#submit').click()

    with allure.step("проверяем успешность регистрации"):
        browser.element('.table').all('td').should(have.texts(
            'Student Name', 'Elena Pirogova',
            'Student Email', '123@123.ru',
            'Gender', 'Female',
            'Mobile', '8987654321',
            'Date of Birth', '2 January,1989',
            'Subjects', 'English',
            'Hobbies', 'Reading',
            'Picture', 'image.png',
            'Address', 'Kazakhstan',
            'State and City', 'NCR Delhi'
        ))



        # browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
        # browser.element(".table-responsive").should(
        #     have.texts(first_name, last_name, "alex@egorov.com", "Some street 1"))