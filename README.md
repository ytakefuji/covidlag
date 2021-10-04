# covidlag
Data science is useful to investigate the progression of the pandemic. 
This repository proposes a new tool covidlag for analyzing a lag time 
between infection peaks and death peaks. 
Covidlang is a open-source program which can provide the lag time and 
the death rate per infection.

Polynomial curve-fitting algorithm is used for detecting infection peaks and death peaks.
The lag time is a difference between a infection peak and a death peak.
The average death rate per infection can be also calculated.
In shorter lag time, we must treat infected patients in urgent manners.
In longer lag time, we must provide sufficient hospital accomodation.
In higher death rate per infection, we must strengthen policies.

# How to install covidlag
Covidlag is available in public and can be installed by the PyPI packaging:

$ pip install covidlag

# How to run covidlag
Run the following command composed of the country name, sampled days, the degree
of polynomial curve-fitting, and options (L: left, R: right, C: center):

$ covidlag Japan 400 13 L

This example shows the 13th degree polynomial curve-fitting has 
r-squared of infections:0.923 and r-squared of deaths:0.706.
The death peaks are [152 267 374].
The case peaks are [27 133 252 258].
The number of death peak is [88 92 54].
The number of case peak is [526 4421 5902 20029]

<img src='Japan.png' height=480 width=640>

$ covidlag 'United States' 600 13 L

<img src='United States.png' height=480 width=640>

$ covidlag Canada 400 13 L

<img src='Canada.png' height=480 width=640>
