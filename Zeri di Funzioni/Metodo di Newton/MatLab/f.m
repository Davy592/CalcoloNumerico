function y=f(x, ord)
% ord: ordine di derivazione
if nargin==1
    ord=0;
end
switch ord
    case 0
        y=x-cos(x);
    case 1
        y=1+sin(x);
    otherwise
        error("Ordine di derivazione non implementato");
end