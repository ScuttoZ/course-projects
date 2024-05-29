# Coding projects

This repository contains scripts and files related to projects that I created while undergoing courses / certifications.

Context for each file will be provided below, as well as instructions on how to use them in case someone wants to copy some and experiment himself/herself.
<details>
<summary>Hands-on Introduction to Linux Commands and Shell Scripting - IBM Course</summary>

### Scope
Creating a script that, for a chosen city, performs a bit of ETL in order to summarizes temperature information gathered using [wttr.in](https://github.com/chubin/wttr.in), an open source weather forecast service. In particular, the challenge was to create a *rx_poc.sh* script that would update a *rx_poc.log* file with the following information about the city of choice:
1. **year**: current year;
2. **month**: current month;
3. **day**: current day;
4. **obs_tmp**: current temperature;
5. **fc_temp**: forecast temperature for tomorrow at noon.

The script would be launched periodically (every 24h) using **cron**.
### My solution
The script *rx_poc.sh* I created has 2 lines dedicated to the selection of the city:
1. the name of the city itself, used in the calls to wttr.in;
2. the time zone of the city, used to retrieve the local date.

The script first retrieves the weather data and stores it in a time-stamped report, written to a txt file named *raw_data_yyyymmdd.txt*, with *"yyyymmdd"* being the user's system's current date.

It then parses the raw data in order to extract the two aforementioned temperatures, *obs_tmp* and *fc_temp*.

### Course's solution
```bash
1. #! /bin/bash
2.
3. # create a datestamped filename for the raw wttr data:
4. today=$(date +%Y%m%d)
5. weather_report=raw_data_$today
6.
7. # download today's weather report from wttr.in:
8. city=Casablanca
9. curl wttr.in/$city --output $weather_report
10.
11. # use command substitution to store the current day, month, and year in corresponding shell variables:
12. hour=$(TZ='Morocco/Casablanca' date -u +%H) 
13. day=$(TZ='Morocco/Casablanca' date -u +%d) 
14. month=$(TZ='Morocco/Casablanca' date +%m)
15. year=$(TZ='Morocco/Casablanca' date +%Y)
16.
17. # extract all lines containing temperatures from the weather report and write to file
18. grep °C $weather_report > temperatures.txt
19.
20. # extract the current temperature 
21. obs_tmp=$(head -1 temperatures.txt | tr -s " " | xargs | rev | cut -d " " -f2 | rev)
22.
23. # extract the forecast for noon tomorrow
24. fc_temp=$(head -3 temperatures.txt | tail -1 | tr -s " " | xargs | cut -d "C" -f2 | rev | cut -d " " -f2 |rev)
25.
26. # create a tab-delimited record
27. # recall the header was created as follows:
28. # header=$(echo -e "year\tmonth\tday\thour_UTC\tobs_tmp\tfc_temp")
29. # echo $header>rx_poc.log
30.
31. record=$(echo -e "$year\t$month\t$day\t$obs_tmp\t$fc_temp")
32. # append the record to rx_poc.log
33. echo $record>>rx_poc.log
```

</details>
<details>
<summary>Developing AI Applications with Python and Flask - IBM Course</summary>
<details>
<summary>Practice Project: Sentiment Analysis</summary>

### Scope
Creating a Python web app using Flask and integrating Embeddable Watson AI libraries to make the web app showcase AI-based abilities. The library in question is the NLP library, which includes functions for sentiment analysis, emotion detection, text classification and language detection, among others.
Sentiment analysis is often performed on textual data to help businesses monitor brand and product sentiment in customer feedback, and understanding customer needs. It helps attain the attitude and mood of the wider public which can then help gather insightful information about the context.

### Solution
The web app uses a function that was implemented as a [package](https://github.com/ScuttoZ/course-projects/tree/main/flask_project/SentimentAnalysis) to make API calls to Watson AI. The call is used to retrieve label and score information about an input text. This information informs the response that the web app gives in the user interface. The project includes a [test file](https://github.com/ScuttoZ/course-projects/blob/main/flask_project/test_sentiment_analysis.py) made with unittest.
</details>
<details>
<summary>Final Project: Emotion Detector</summary>


</details>
</details>
