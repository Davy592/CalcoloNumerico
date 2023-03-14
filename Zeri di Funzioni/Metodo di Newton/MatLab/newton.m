function [alpha, it]=newton(f, x0, tol, itmax)
%Metodo di Newton
%
%
it=0;
arresto=0;
while ~arresto && it<itmax
    it=it+1;
    x1=x0-f(x0)/f(x0,1);
    arresto=abs(x1-x0)<tol;
    x0=x1;
end
if ~arresto
    warning("Precisione non raggiunta");
end
alpha=x1;