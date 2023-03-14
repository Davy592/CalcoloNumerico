function [alpha, it]=zero(f, a, b, tol, itmax)
    %METODO DELLE SUCCESSIVE BISEZIONI
    %Sintassi:
    %   [alpha, it]=bisezioni(f, a, b, tol, itmax)
    %
    %Parametri di input{
    %   f: funzione di cui ricevere uno zero
    %   [a,b]: intervallo di lavoro
    %   tol: precisione richiesta
    %   itmax: numero massimo di iterate consentite
    %}
    %
    %Parametri di output{
    %   alpha: approssimazione di uno zero di f
    %   it: numero di iterate eseguite
    %}
fa=f(a); %se metto ';' non vedro' a video il risultato di questa assegnazione
fb=f(b);
if fa*fb>0
    error("La funzione non cambia segno agli estremi dell'intervallo");
end
it=0; %contatore di iterate
while b-a>tol && it<itmax
    c=(b+a)/2;
    fc=f(c);
    if fc==0 
        break
    elseif fa*fc<0
        b=c;
    else
        a=c;
        fa=fc;
    end
    it=it+1;
end
alpha=c;
if b-a>tol
    warning("Precisione non raggiunta");
end