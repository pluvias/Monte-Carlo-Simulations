clear, clc;
% The Erlang distribution. Simulation with the von Neumann (rejection) method.

% Parameters of distribution:
k = 3; % positive integer, the "shape".
lambda = 5.5; % positive real number, the "rate".

N = 10000; % Sample length.
X = zeros(1,N); % Array for values.
x1 = 0; x2 = 20; % x variable's interval.

% Divide the range into 1000 points:
x = linspace(x1,x2,1000);

% The probability density function (PDF)of Erlang distribution:
f = @(x)(lambda * (lambda*x).^(k-1) .* exp(-lambda*x) ) / factorial(k-1);

% Compute density for each x:
F = f(x);

% Find max value:
Fmax = max(F);

n = 1; % Counter.

while n <= N % Until we get the right amount of numbers from the sample.
    
    % Generate random points:
    xpoint = x1 + (x2 - x1)*rand;
    ypoint = Fmax*rand;
    
    if ypoint <= f(xpoint) % If the point is below the graph.
        X(n) = xpoint; % Save this point.
        n = n+1;
    end
end

[yh, xh] = hist(X,100); % Show histogram.
yh = yh/(length(X)*(xh(2)-xh(1))); % Compute the density on the histogram.

plot (x,F,'r', xh,yh,'b') 
grid on

title( ['Rejection method for the Erlang distribution with parameters k = ',num2str(k),' , \lambda = ',num2str(lambda)] )
legend('Theoretical','Empirical')
