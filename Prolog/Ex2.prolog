% Reverse
my_reverse([], Acc, Acc).
my_reverse([X|Xs], Acc, Result) :-
    my_reverse(Xs, [X|Acc], Result).
my_reverse(L, Result) :- 
    my_reverse(L, [], Result).

% Member
member(X, [X|_], true).
member(X, [_|Y], Result) :-
    member(X, Y, Result).
member(_, [], false).
member(X, L) :-
    member(X, L, true).

% palindrome
palindrome(L) :-
    my_reverse(L, L).

% Sorted
sorted([]).
sorted([_]).
sorted([X, Y|Rest]) :-
    X =< Y,
    sorted([Y|Rest]).


% Base case: The permutation of an empty list is an empty list.
permutation([], []).

% Recursive case:
% P is a permutation of [X|L] if we can select X from [X|L], and P is the result
% of placing X at the front of a permutation of the remaining elements L.
permutation(L, [X|P]) :-
    select(X, L, Rest),  % Select X from L, and Rest is the list without X.
    permutation(Rest, P).  % Recursively find the permutation of Rest.