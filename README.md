# King County Home Flipping

## Business Understanding

Our client, Seattle Home Flippers, wants to optimize their business by studying trends in the Seattle real estate business. They specifically want to know where they should investment and what to focus on in renovations. To identify answers to these questions, first we want to find the area with lowest average sale price, because they will have the most potential profit return on investment. Then, we wanted to find the key feature within a house that increases its value in the buyers eyes. By implementing the findings to both of these problems, Seattle Home Flippers will be able to increase their sale prices on renovated homes.
By building multiple-linear regression models, we are able to make predictions of home sale prices and identify the variables that influence the price most (have the most value).

## Data Understanding

We used a dataframe containing King County Housing information, which describes properties in the city of Seattle, Washington. Our client is a home flipper, therefore only concerned with how the interior of the house effects price, so we removed properties from the dataframe that had a view. We reasoned that views might unequally effect sale price and create unnecessary outliers that would hurt the model. To make the data more concise, we dropped information we deemed irrelevant or unimpactful to the business problem (year renovated, id, date, floors, latitude, longitude). We then grouped grade into 3 categories to provide more samples per section and organized living space area to provide information on houses with basements and the size of the basements. We decided to OneHot encode the zipcode category in order for the model to reflect the area each property was in. Finally, after viewing the correlation heatmap, we fixed colineraity and were ready to model.

![image](https://user-images.githubusercontent.com/106109221/177224097-818ad5a7-7457-4e6b-a2fe-b2ea22754571.png)

## Methods

First, we established a baseline model isolating sale price as the depend variable. Our first model was inaccurate, as shown by the low R squared score of .457. We then used log to improve the model and rid ourselves of outliers, which actually decreased R^2. Scrap it. To create a better model, we used the kitchen sink approach. After setting a standard scaler and transformer, the model improved, returning a R^2 of .827. After logging it, our final model returned R^2 of .86. This means that our model, which includes bedrooms, living area (sq. feet), lot area, condition, year built, zipcode, size of neighbors lots, size of basement, has a basement, and grade group (1-3), can explain about 86% of variance for price. 

##Results

![Housing regression model](https://user-images.githubusercontent.com/106109221/177225935-1c014b53-3c72-4af5-a6ed-1aeb585af104.png)

The model showed us that the variable with most correlation to sale price is the square footage of living space. To display this relationship, we created a scatterplot with a line of best fit set to show the positive linear relationship between the two variables. We found that, acording to the findings, every increase in area by 100 square feet will result in a 3.25% increase in sales price. 

![image](https://user-images.githubusercontent.com/106109221/177226180-d680339f-ccc0-4fb8-86d9-35b1f0cf05f9.png)

Additionally, we found that the zipcode with the lowest average sale price ($234,103) was 98002: Auburn, Washington.

![cheap zipcode seatlle housing](https://user-images.githubusercontent.com/106109221/177226324-bb730fd9-c843-4921-b2ac-3b399e1b5896.png)

##Recommendations

The data shows that Seattle Home Flippers should concentrate on size primarily; the more area they can provide, the more the house will sell for. Also, they should look into investing in homes in the Auburn community of Seattle. 

##References

Presentation: https://www.canva.com/design/DAFFF3RLExM/Qh0b7_hVQsitJx8OZRjb7A/edit?utm_content=DAFFF3RLExM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
Data: https://info.kingcounty.gov/assessor/esales/Residential.aspx

