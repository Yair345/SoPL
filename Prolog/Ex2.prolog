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

