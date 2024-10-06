*** Settings ***
Documentation       Testing

Resource            import.resource


*** Test Cases ***
Open Google Chrome 1
    [Documentation]    test 1
    [Tags]    test-1    vps
    Open Google Chrome    url=https://www.google.com/en
    Close Browser

Open Google Chrome 2
    [Documentation]    test 2
    [Tags]    test-2    search
    Open Google Chrome    url=https://www.google.com/en
    Close Browser
