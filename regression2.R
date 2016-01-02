setwd("~/Documents/15fall/Thesis/Columbia")
data <- read.csv("data/final_new.csv", stringsAsFactors = FALSE)

# Pool all pairs across all days, remove observations with neutral labels
data1 <- data.frame(source=rep(data$source, 3), target=rep(data$target, 3),
                    sourceLab=c(data$sourceLab1, data$sourceLab2, data$sourceLab3),
                    targetLab=c(data$targetLab1, data$targetLab2, data$targetLab3),
                    sourcePos=c(data$sourcePos1, data$sourcePos2, data$sourcePos3),
                    targetPos=c(data$targetPos1, data$targetPos2, data$targetPos3))

data1Pos <- data1[data1$sourceLab == "pos" & data1$targetLab == "pos", ]
data1Pos$sourcePos <- data1Pos$sourcePos - 0.5
data1Pos$targetPos <- data1Pos$targetPos - 0.5
model1_pos <- lm(sourcePos ~ targetPos, data=data1Pos)
summary(model1_pos)

data1Neg <- data1[data1$sourceLab == "neg" & data1$targetLab == "neg", ]
data1Neg$sourcePos <- 0.5 - data1Neg$sourcePos
data1Neg$targetPos <- 0.5 - data1Neg$targetPos
model1_neg <- lm(sourcePos ~ targetPos, data=data1Neg)
summary(model1_neg)

data1Sub <- data1[data1$sourceLab != "neutral" & data1$targetLab != "neutral", ]
data1Sub$sourcePos <- data1Obj$sourcePos - 0.5
data1Sub$targetPos <- data1Obj$targetPos - 0.5
model1_sub <- lm(sourcePos ~ targetPos, data=data1Sub)
summary(model1_sub)

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

data2Pos <- data2[data2$sourceLab2 == "pos" & data2$targetLab2 == "pos", ]
data2Pos$sourcePos1 <- data2Pos$sourcePos1 - 0.5
data2Pos$sourcePos2 <- data2Pos$sourcePos2 - 0.5
data2Pos$targetPos1 <- data2Pos$targetPos1 - 0.5
data2Pos$targetPos2 <- data2Pos$targetPos2 - 0.5
model2_pos <- lm(sourcePos2 ~ targetPos2 + sourcePos1 + targetPos1, data=data2Pos)
summary(model2_pos)

data2Neg <- data2[data2$sourceLab2 == "neg" & data2$targetLab2 == "neg", ]
data2Neg$sourcePos1 <- data2Neg$sourcePos1 - 0.5
data2Neg$sourcePos2 <- data2Neg$sourcePos2 - 0.5
data2Neg$targetPos1 <- data2Neg$targetPos1 - 0.5
data2Neg$targetPos2 <- data2Neg$targetPos2 - 0.5
model2_neg <- lm(sourcePos2 ~ targetPos2 + sourcePos1 + targetPos1, data=data2Neg)
summary(model2_neg)


data2Sub <- data2[data2$sourceLab1 != "neutral" & data2$sourceLab2 != "neutral" &
                      data2$targetLab1 != "neutral" & data2$targetLab2 != "neutral", ]
data2Sub$sourcePos1 <- data2Sub$sourcePos1 - 0.5
data2Sub$sourcePos2 <- data2Sub$sourcePos2 - 0.5
data2Sub$targetPos1 <- data2Sub$targetPos1 - 0.5
data2Sub$targetPos2 <- data2Sub$targetPos2 - 0.5
model2_sub <- lm(sourcePos2 ~ targetPos2 + sourcePos1 + targetPos1, data=data2Sub)
summary(model2_sub)

# Control for "sentiment per friend" for source node
data2Pos$perFriend <- data2Pos$targetPos2/data2Pos$sourceFriends
model31_pos <- lm(sourcePos2 ~ targetPos2 + sourcePos1 + targetPos1 + sourceFriends, data=data2Pos)
summary(model31_pos)
model32_pos <- lm(sourcePos2 ~ perFriend + sourcePos1 + targetPos1, data=data2Pos)
summary(model32_pos)

data2Neg$perFriend <- data2Neg$targetPos2/data2Neg$sourceFriends
model31_neg <- lm(sourcePos2 ~ targetPos2 + sourcePos1 + targetPos1 + sourceFriends, data=data2Neg)
summary(model31_neg)
model32_neg <- lm(sourcePos2 ~ perFriend+ sourcePos1 + targetPos1, data=data2Neg)
summary(model32_neg)

data2Sub$perFriend <- data2Sub$targetPos2/data2Sub$sourceFriends
model31_sub <- lm(sourcePos2 ~ targetPos2 + sourcePos1 + targetPos1 + sourceFriends, data=data2Sub)
summary(model31_sub)
model32_sub <- lm(sourcePos2 ~ perFriend + sourcePos1 + targetPos1, data=data2Sub)
summary(model32_sub)

# Do explorations on how number target followers may affect result
model41_pos <- lm(sourcePos2 ~ targetPos2 + sourcePos1 + targetPos1 + sourceFriends + targetFollowers, data=data2Pos)
summary(model41_pos)
model42_pos <- lm(sourcePos2 ~ perFriend  + sourcePos1 + targetPos1 + targetFollowers, data=data2Pos)
summary(model42_pos)

model41_neg <- lm(sourcePos2 ~ targetPos2 + sourcePos1 + targetPos1 + sourceFriends + targetFollowers, data=data2Neg)
summary(model41_neg)
model42_neg <- lm(sourcePos2 ~ perFriend + sourcePos1 + targetPos1 + targetFollowers, data=data2Neg)
summary(model42_neg)

model41_sub <- lm(sourcePos2 ~ targetPos2 + sourcePos1 + targetPos1 + sourceFriends + targetFollowers, data=data2Sub)
summary(model41_sub)
model42_sub <- lm(sourcePos2 ~ perFriend + sourcePos1 + targetPos1 + targetFollowers, data=data2Sub)
summary(model42_sub)

# Add number of followers as dummy variable
data2Pos$media <- data2Pos$targetFollowers > 500
model51_pos <- lm(sourcePos2 ~ targetPos2 + sourcePos1 + targetPos1 + sourceFriends + media, data=data2Pos)
summary(model51_pos)

data2Neg$media <- data2Neg$targetFollowers > 500
model51_neg <- lm(sourcePos2 ~ targetPos2 + sourcePos1 + targetPos1 + sourceFriends + media, data=data2Neg)
summary(model51_neg)

data2Sub$media <- data2Sub$targetFollowers > 500
model51_sub <- lm(sourcePos2 ~ targetPos2 + sourcePos1 + targetPos1 + sourceFriends + media, data=data2Sub)
summary(model51_sub)
