from selene import browser, have
# from conftest import setup_browser

def test_search_element(setup_browser):
    browser.open("https://duckduckgo.com/")
    browser.element('[id=searchbox_input]').type('qa.guru').press_enter()
    browser.element('[id=web_content_wrapper]').should(have.text('https://qa.guru'))

def test_result_not_found(setup_browser):
    browser.open("https://duckduckgo.com/")
    searchedText = 'иромро'
    browser.element('[id=searchbox_input]').type(searchedText).press_enter()
    actualResult = 'По запросу '+searchedText+' результаты не найдены.'
    browser.element('//section[@data-testid="mainline"]//span').should(have.text(actualResult))


