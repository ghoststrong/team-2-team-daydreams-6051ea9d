*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in the middle of the board     4             5             1                     NORTH         0           6           2
Move on the edge of the board       0             0             5                     SOUTH         0           0           6
Move on the edge of the board       0             1             7                     WEST          0           1           8
Move on the edge of the board       9             9             10                    NORTH         9           9           11
Move on the edge of the board       0             9             8                     NORTH         0           9           9
Move on the edge of the board       9             0             7                     EAST          9           0           8




*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}