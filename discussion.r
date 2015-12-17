setwd("~/Documents/15fall/Thesis/Columbia")
data <- read.csv("data/final.csv", stringsAsFactors = FALSE)
profile <- read.csv("data/allProfile.csv")

# data2 is equivalent to data2 in regression.R
data2 <- data.frame(source=rep(data$source, 2), target=rep(data$target, 2),
                    sourceLab1=c(data$sourceLab1, data$sourceLab2),
                    sourcePos1=c(data$sourcePos1, data$sourcePos2),
                    sourceLab2=c(data$sourceLab2, data$sourceLab3),
                    sourcePos2=c(data$sourcePos2, data$sourcePos3),
                    targetLab1=c(data$targetLab1, data$targetLab2),
                    targetPos1=c(data$targetPos1, data$targetPos2),
                    targetLab2=c(data$targetLab2, data$targetLab3),
                    targetPos2=c(data$targetPos2, data$targetPos3),
                    sourceFriends=rep(data$sourceFriends, 2),
                    targetFollowers=rep(data$targetFollwers, 2))

data2Sub <- data2[data2$sourceLab1 != "neutral" & data2$sourceLab2 != "neutral" &
                      data2$targetLab1 != "neutral" & data2$targetLab2 != "neutral", ]

# Do explorations on how number target followers may affect result
model5 <- lm(sourcePos2 ~ targetPos2 + sourcePos1 + targetPos1 + targetFollowers, data=data2Sub)
summary(model5)

data2Sub$perFriend <- data2Sub$targetPos2/data2Sub$sourceFriends
model6 <- lm(sourcePos2 ~ perFriend + sourcePos1 + targetPos1 + targetFollowers, data=data2Sub)
summary(model6)

summary(profile$followers_count)
sum(profile$followers_count > 10000)
sum(profile$followers_count > 500)
level <- c("[0, 100]", "(100, 500]", "(500, 1000]", "(1000, 2000]", "(2000, 5000]", 
           "(5000, 10000]", "(10000, 50000]", "(50000, 100000]", "(100000, )")
count <- c(160, 697, 534, 510, 529, 378, 727, 208, 359)

data2Sub$targetPop <- data2Sub$targetFollowers <= 500
model7 <- lm(sourcePos2 ~ perFriend + sourcePos1 + targetPos1 + targetPop, data=data2Sub)
summary(model7)

library(ggplot2)

qplot(level, data=followers, geom="bar")

ggplot(data=followers, aes(x=range, y=count)) + geom_bar(stat="identity")
