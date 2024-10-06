*** Settings ***
Documentation       Keywords for google chrome

Library             Browser


*** Keywords ***
Open Google Chrome
    [Documentation]    Open Google Chrome
    [Arguments]    ${url}
    New Page    url=${url}
