*** Settings ***
Documentation       Testing

Library             Browser
Resource            ${EXECDIR}/python/robotframework/resources/import.resource


*** Variables ***
${SEARCH_NAME}      lego


*** Test Cases ***
Open VPS News
    [Documentation]    Open VPS news page
    [Tags]    vps
    Open Google Chrome    url=https://viewpointsystem.com/en
    Click    "News"
    Take Screenshot
    Close Browser

Search In Google
    [Documentation]    Search in google
    [Tags]    search
    Search In Google    ${SEARCH_NAME}
