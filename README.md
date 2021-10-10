# covidlag
Data science is useful to investigate the progression of the pandemic. 

covidlag is an open-source program which is available in public and 
can be installed by the PyPI package command (pip).
covidlag can calculate the lag time between infection peaks and death peaks.
covidlag can also compute death rate per infection or case fatality ratio (CFR).
CFR is the proportion of individuals diagnosed with a disease who die from 
that disease and is therefore a measure of severity among detected cases.

CFR is a dynamic value which is continuously changing. 
In the conventional methods, CFR is used for retrospective observational studies 
and are not suitable for continuous time series data.  

According to CDC:
https://www.cdc.gov/foodnet/reports/data/case-fatality.html

the CFR is calculated by:
CFR=(number of cases in which patient died/number of cases).

The CDC method for CFR is appropriate for annual statistics, 
but not for time series data analysis.

In the current CFR calculation, we need to determine two indicators: the number of sampled days and its range of start and ending dates. 

Two indicators significantly influence CFR.

COVID-19 variants and vaccinations can significantly change the lag time and the CFR so that the convetional distribution approaches are not suitable for ongoing time series data.

There is no algorithm to select two appropriate indicators.

The proposed algorithm is based on a robust correlation between infection and death.

The extreme values such as maxima and minima can be used for computing the accurate lag time and the CFR.


The detailed method is under review.


# How to install covidlag
Covidlag is available in public and can be installed by the following 
PyPI packaging command:

$ pip install covidlag

# How to run covidlag
covidlag needs at least three parameters (country name, sampled days, 
regression polinomial degree).

Run the following command composed of the country name, sampled days, the degree
of polynomial curve-fitting, and options (L: left, R: right, C: center):

$ covidlag Japan 400 13 L

This example is for "Japan" with the "13th" degree polynomial curve-fitting using 
"400" sampled days. 
The result shows the polynomial curve-fitting that r-squared of infections 
is 0.923 and r-squared of deaths is 0.706.
<pre>
The death peaks are [152 267 374].
death peak: 2021-01-29 <-
death peak: 2021-05-24 <-
death peak: 2021-09-08 <-

The case peaks are [27 133 252 258].
case peak: 2020-09-26
case peak: 2021-01-10 <-
case peak: 2021-05-09 <-
case peak: 2021-08-23 <-

The lag time between infections and deaths is 152-133=19 days, 267-252=15 days, 
and 374-258=16 days respectively.
</pre>

The number of every death peak is [88 92 54].

The number of every case peak is [526 4421 5902 20029]

Therefore, death rate of peaks or CFR is 88/4421=0.019, 92/5902=0.015, and
54/20029=0.0026 respectively.

The CFR is significantly decreasing.

<img src='https://github.com/ytakefuji/covidlag/raw/main/Japan.png' height=480 width=640>

$ covidlag 'United States' 600 13 L

<img src='https://github.com/ytakefuji/covidlag/raw/main/United States.png' height=480 width=640>
This example shows that r-squared of infections:0.803 and r-squared of deaths:0.733

The death peaks are [71 189 337 470 579]
<pre>
death peak: 2020-04-23
death peak: 2020-08-19
death peak: 2021-01-14
death peak: 2021-05-27
death peak: 2021-09-13

The case peaks are [52 156 315 448 566]

case peak: 2020-04-04
case peak: 2020-07-17
case peak: 2020-12-23
case peak: 2021-05-05
case peak: 2021-08-31
</pre>

The lag time between infections and deaths is 19 days, 33 days, 22 days, 22 days, 13 days.


The number of every death peak is [1944 1005 3109 632 1943].

The number of every case peak is [28858 57877 207829 44827 178454]

The death rate per infection is 1944/28858=0.067,1005/57877=0.017,
3109/207829=0.015,632/44827=0.014,1943/178454=0.011

CFR in the US is slowly decreasing. But, it is still high compared with that of Japan.

$ covidlag Canada 400 13 L

<img src='https://github.com/ytakefuji/covidlag/raw/main/Canada.png' height=480 width=640>
<pre>
death peak: 2020-09-07
death peak: 2021-01-06
death peak: 2021-05-08
death peak: 2021-09-25
case peak: 2020-09-07
case peak: 2020-12-26
case peak: 2021-04-21
case peak: 2021-09-19
</pre>
The lag time is 11 days, 17 days,...

The death rate per infection is 0.018,0.006,...
