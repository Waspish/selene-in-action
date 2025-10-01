from time import sleep

from selene import browser, have, be, by, command
from selene.core import match


def test_complete_todo():
    browser.open('/')

    # Store elements in variables for reuse
    todo_input = browser.element('.new-todo')
    todo_list = browser.all('.todo-list>li')

    # Perform multiple actions on the same element
    todo_input.should(be.blank)
    todo_input.type('Buy groceries').press_enter()
    todo_input.perform(command.select_all)
    todo_input.should(be.blank)
    todo_input.type('Walk the dog').press_enter()

    # Use the stored collection
    # todo_list.with_(timeout=browser.config.timeout * 1.5).should(have.size(2))
    todo_list[0].element('.toggle').should(match.element_is_selected.not_)
    todo_list[0].element('.toggle').click()
    todo_list[0].element('.toggle').should(match.element_is_selected)
    # todo_list[0].should(have.no.css_class('completed'))
    todo_list[0].should(have.exact_text('Buy groceries'))
    todo_list.should(have.size(2))
    todo_list.should(have.exact_texts('Buy groceries', 'Walk the dog'))
    todo_list.by(have.css_class('completed')).should(have.exact_texts('Buy groceries'))
    todo_list.by(have.no.css_class('completed')).should(
        have.exact_texts('Walk the dog')
    )





# def test_complete_todo_2(driver):
#     driver.get('https://todomvc.com/examples/emberjs/todomvc/dist/')
#     assert driver.find_element(*by.css('.new-todo')).get_attribute('value') == ''
