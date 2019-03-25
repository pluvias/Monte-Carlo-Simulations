clear, clc;
% The Simpson (triangular) distrubution

% Parameters:
alpha = 16; betta = 36; % Given: (betta-alpha) > 0

% The probability density function (PDF):
f = @(x)(2*(1-abs(alpha+betta-2*x)/(betta-alpha))) /(betta-alpha);

N = 100000; % Sample length.

X = zeros(1,N); % Array for random variables.

% Divide the range into 1000 points:
x = linspace(alpha,betta,1000);

% Count the density for each x:
F = f(x);

for i=1:N
    X(i) = alpha + 0.5*(betta-alpha)*(rand()+rand());
end

[yh, xh] = hist(X,100) % Show histogram.
yh = yh/(length(X)*(xh(2)-xh(1))); % Count the density on the histogram.

plot (x,F,'r', xh,yh,'b') 
grid on

title( ['Simpson distribution with parameters \alpha = ',num2str(alpha),' , \beta = ',num2str(betta)] )
legend('Theoretical','Empirical')

