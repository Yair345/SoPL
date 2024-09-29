% parent(Parent, Child)
parent(yossi, danny).
parent(yossi, yael).
parent(ronit, danny).
parent(ronit, yael).
parent(danny, yonatan).
parent(danny, tamar).
parent(yael, yonatan).
parent(yael, tamar).

parent(yair, noam).
parent(yair, yarin).
parent(shir, noam).
parent(shir, yarin).

parent(noam, omer).
parent(noam, revaya).
parent(noa, omer).
parent(noa, revaya).

% male(Name)
male(yossi).
male(danny).
male(yonatan).
male(yair).
male(noam).
male(yarin).
male(omer).

% female(Name)
female(ronit).
female(yael).
female(tamar).
female(shir).
female(revaya).
female(noa).

% married(Spouse1, Spouse2)
married(yossi, ronit).
married(danny, yael).
married(yair, shir).
married(noam, noa).


% functions
married(X, Y) :-
    married(Y, X).

father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

son(X, Y) :-
    parent(Y, X),
    male(X).

daughter(X, Y) :-
    parent(Y, X),
    female(X).

grandfather(X, Y) :-
    father(X, Z),
    parent(Z, Y).

grandmother(X, Y) :-
    mother(X, Z),
    parent(Z, Y).

grandson(X, Y) :-
    son(X, Z),
    parent(Y, Z).

granddaughter(X, Y) :-
    daughter(X, Z),
    parent(Y, Z).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y).

uncle_no_blood_connection(X, Y) :-
    married(X, Z),
    sibling(Z, W),
    parent(W, Y).

son_of_aunt(X, Y) :-
    son(X, Z),
    sibling(Z, W),
    mother(W, Y).
    
% This could be both brother and sister because unclearaty in Hebrew
brother_in_law(X, Y) :-
    married(X, Z),
    sibling(Z, Y).
brother_in_law(X, Y) :-
    brother_in_law(Y, X).

niece(X, Y) :-
    daughter(X, Z),
    sibling(Z, Y).

cousin(X, Y) :-
    parent(Z, X),
    sibling(Z, W),
    parent(W, Y).

second_cousin(X, Y) :-
    parent(Z, X),
    parent(W, Y),
    cousin(Z, W).


