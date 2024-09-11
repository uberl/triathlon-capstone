Google Data Analytics Capstone Project

I have no rights to the data. It is publicly available here: https://www.datasport.de/anmeldeservice/triathlonnuernberg2024/ergebnisse#5_07AD35

Question: Where were the participants of my first triathlon from?

Steps:
1. Download raw data into list.json
2. Clean and structure data into data.csv:
    - format split times as hh:mm:ss for pandas
    - move relative placement in swmimming, biking, running into separate new columns
    - clean user input for "team"
    - merge mens' and womens' results
    - add a column "sex"
    - format nationality to iso-3 code, e.g. "GER" -> "DEU" (for plotly)
3. Create a chloropleth interactive map through plotly express:
    - categorize by count into the three categories (exactly 1, more than 1 , and germany)
    - create nice readable labels, e.g. "DEU" -> "Germany"
4. Adapt labels and styles
    - Title and subtitle
    - Hover Tooltip only shows Number Of Participants
  
Reasoning for the categorization:
Upon further inspection, basically all participants where from germany. A lot of participants where from single countries. Some neighbouring countries had 2-5 participants.


