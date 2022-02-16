#Loading Libraries for this project
install.packages("caTools")

library(tidyverse) # metapackage with lots of helpful functions
library(ggplot2) # Data visualization
library(plotly) # Interactive data visualizations
library(psych) # Will be used for correlation visualizations
library(rattle) # Graphing decision trees
library(caret) # Machine learning
library(caTools)
library(InformationValue)

#Loading the dataset into R environment
heart_rel_data <- read.csv("/Users/apoor/Desktop/Anjali/MSDAIS/Stats/Project/framingham.csv",header=TRUE,sep=",")

#Attaching the data with headers
attach(heart_rel_data)

#Data Exploration
str(heart_rel_data)

paste("There are",nrow(heart_rel_data),"data rows")
paste("There are",sum(complete.cases(heart_rel_data)),"complete data rows")
paste("There are",sum(!complete.cases(heart_rel_data)),"incomplete data rows")

#Visualization with Outliers
boxplot(totChol)
boxplot(BMI)
boxplot(heartRate)
boxplot(glucose)

#Correlation----------Explanation needed
boxplot(heartRate~currentSmoker)
boxplot(age~male)
boxplot(age ~ currentSmoker)
boxplot(age ~ diabetes)

#Summary of entire data
summary(heart_rel_data)

#Checking NA values in each column
colSums(is.na(heart_rel_data))

#Assumptions:
#We can drop education as it is not playing any major role as a risk factor to predict the outcome of disease

#Removing education column
heart_rel_data_clean <- subset(heart_rel_data, select = -c(education))
head(heart_rel_data_clean)

#Removing NA values
heart_data<-(na.omit(heart_rel_data_clean))
heart_data

#Checking NA values in each column
colSums(is.na(heart_data))

#Removing outliers
#https://medium.com/geekculture/essential-guide-to-handle-outliers-for-your-logistic-regression-model-63c97690a84d


#Converting categorical variables(data types) into factors
heart_data$male <- as.factor(heart_data$male)
heart_data$currentSmoker <- as.factor(heart_data$currentSmoker)
heart_data$BPMeds <- as.factor(heart_data$BPMeds)
heart_data$prevalentStroke <- as.factor(heart_data$prevalentStroke)
heart_data$prevalentHyp <- as.factor(heart_data$prevalentHyp)
heart_data$diabetes <- as.factor(heart_data$diabetes)
heart_data$TenYearCHD <- as.factor(heart_data$TenYearCHD)

#Checking data types after conversion to factors
str(heart_data)

#Taking Training dataset and Testing dataset
set.seed(30)
heart_datasplit <- sample.split(heart_data$TenYearCHD, SplitRatio = 0.7)
training_heart_data <- heart_data[heart_datasplit==T,]
testing_heart_data <- heart_data[heart_datasplit==F,]
nrow(training_heart_data)
nrow(testing_heart_data)


#Creation of Logistic regression model
?glm()
logistic_model <- glm(TenYearCHD~., data = training_heart_data, family = "binomial")
summary(logistic_model)

#Threshold value(alpha) is set to be 0.5 in our model as it is morally neutral

#Hypothesis Test 1

#H0: The fit of the model with independent variables is as good with the fit of model without independent variable
#Ha: The fit of the independent variable of model is better than the model without independent variable


#p-value calculation
1-pchisq(2240.5 - 1958.9,2623-2609 )

#Here in this model, we can see that Residual deviance is less than the Null deviance. So, the model fits better
#p values is less than the threshold value so we are keeping the H0 and rejecting the Ha


#Hypothesis Test 2

#Identifying Simple and Complicated model

model1<-glm(training_heart_data$TenYearCHD~training_heart_data$totChol,family=binomial(link="logit"))
summary(model1)

model2<-glm(training_heart_data$TenYearCHD~training_heart_data$totChol+training_heart_data$sysBP,family=binomial(link="logit"))
summary(model2)

#Null deviance: 3202.8  on 3748  degrees of freedom
#Residual deviance: 3031.2  on 3746  degrees of freedom
attach(training_heart_data)
#model3<-glm(training_heart_data$TenYearCHD~training_heart_data$totChol+training_heart_data$sysBP+
 #             training_heart_data$diabetes+training_heart_data$age+training_heart_data$currentSmoker+training_heart_data$male+training_heart_data$prevalentStroke+
  #            training_heart_data$diaBP,family=binomial(link="logit"))

model3<-glm(TenYearCHD~totChol+sysBP+
              diabetes+age+currentSmoker+male+prevalentStroke+
              diaBP,family=binomial(link="logit"))
summary(model3)

#Null deviance: 3202.8  on 3748  degrees of freedom
#Residual deviance: 2852.6  on 3740  degrees of freedom

#Now Null deviance's DOF is matching with model2 null deviance's DOF. So, we'll compare residual deviance

anova(model2,model3,test="Chisq")

#Since the p-value is very low(less than the threshold value). SO, we are rejecting the H0 and accepting the Ha.
#And hence, determing that the more complicated model is better fit.


pred_model <- predict(model3,newdata = testing_heart_data,type = "response")
summary(pred_model)

pred_test_data <- ifelse(pred_model>0.5,1,0)
summary(pred_test_data)

# The columns are actuals, while rows are predicteds.
#predicted=predict(model3,type="response")
#predicted

#Need explanation of plotROC
plotROC(testing_heart_data$TenYearCHD, pred_test_data)
#AUROC: 0.523

#Need explanation of Concordance
Concordance(testing_heart_data$TenYearCHD, pred_test_data)


# The columns are actuals, while rows are predicteds.
sensitivity(testing_heart_data$TenYearCHD, pred_test_data, threshold = 0.5)
#[1] 0.06395349

specificity(testing_heart_data$TenYearCHD, pred_test_data, threshold = 0.5)
# [1] 0.9832109


confusionMatrix(testing_heart_data$TenYearCHD, pred_test_data, threshold = 0.5)


#0   1
#0 937 161
#1  16  11

#Though we have accuracy as 84.82262 % but this model is not able to predict people who have the risk of heart disease correctly

(937+11)/(161+16+937+11)
#Overall Accuracy with threshold as 0.5 as 84.27%

#So, we ll take optimum cut off value using sensitivity and specificity
opt_cut_off =  (  0.06+0.9832109)-1
opt_cut_off
#[1] 0.0432109

confusionMatrix(testing_heart_data$TenYearCHD, pred_test_data, threshold = opt_cut_off)
(161/(161+11))
#Accuracy for predicted values with optimum cut off as 0.04 is 93.60%

