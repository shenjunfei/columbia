setwd("~/Documents/15fall/Thesis/Columbia")
data <- read.csv("data/final.csv", stringsAsFactors = FALSE)

# Pool all pairs across all days, remove observations with neutral labels
data1 <- data.frame(source=rep(data$source, 3), target=rep(data$target, 3),
                    sourceLab=c(data$sourceLab1, data$sourceLab2, data$sourceLab3),
                    targetLab=c(data$targetLab1, data$targetLab2, data$targetLab3),
                    sourcePos=c(data$sourcePos1, data$sourcePos2, data$sourcePos3),
                    targetPos=c(data$targetPos1, data$targetPos2, data$targetPos3))

data1Sub <- data1[data1$sourceLab != "neutral" & data1$targetLab != "neutral", ]

model1 <- lm(sourcePos ~ targetPos, data=data1Sub)
summary(model1)

# Control for lagged dependent variable - ego's stable and intrinsic character
# If control for lagged independent varibale, results are similar
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

model2 <- lm(sourcePos2 ~ targetPos2 + sourcePos1 + targetPos1, data=data2Sub)
summary(model2)

# Control for "sentiment per friend" for source node
data2Sub$perFriend <- data2Sub$targetPos2/data2Sub$sourceFriends
model3 <- lm(sourcePos2 ~ perFriend + sourcePos1 + targetPos1, data=data2Sub)
summary(model3)

model4 <- lm(sourcePos2 ~ sourcePos1 + perFriend, data=data2Sub)
summary(model4)

# Do explorations on how number target followers may affect result
model5 <- lm(sourcePos2 ~ targetPos2 + sourcePos1 + targetPos1 + targetFollowers, data=data2Sub)
summary(model5)

model6 <- lm(sourcePos2 ~ perFriend + sourcePos1 + targetPos1 + targetFollowers, data=data2Sub)
summary(model6)
