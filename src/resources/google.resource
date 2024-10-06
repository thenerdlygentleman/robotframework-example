*** Settings ***
Documentation       Keywords for google

Library             Browser
Resource            chrome.resource


*** Variables ***
${URL}          https://www.google.com/en
${SEARCH}       //*[@id="APjFqb"]


*** Keywords ***
Search In Google
    [Documentation]    Search for a keyword in google and make a screenshot
    [Arguments]    ${keyword}
    Open Google Chrome    url=${URL}
    Click    "Accept all"
    Fill Text    ${SEARCH}    ${keyword}
    Press Keys    ${SEARCH}    Enter
    Wait For Elements State
    ...    ${SEARCH}
    ...    visible
    Take Screenshot
    Close Browser
