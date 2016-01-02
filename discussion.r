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

data2Sub$sourcePos1 <- data2Sub$sourcePos1 - 0.5
data2Sub$sourcePos2 <- data2Sub$sourcePos2 - 0.5
data2Sub$targetPos1 <- data2Sub$targetPos1 - 0.5
data2Sub$targetPos2 <- data2Sub$targetPos2 - 0.5

# Do explorations on how number target followers may affect result
model5 <- lm(sourcePos2 ~ targetPos2 + sourcePos1 + targetPos1 + targetFollowers, data=data2Sub)
summary(model5)

data2Sub$perFriend <- data2Sub$targetPos2/data2Sub$sourceFriends
model6 <- lm(sourcePos2 ~ perFriend + sourcePos1 + targetPos1 + targetFollowers, data=data2Sub)
summary(model6)

summary(profile$followers_count)
sum(profile$followers_count > 10000)
sum(profile$followers_count > 500)
cutPoints <- c(0, 50, 100, 200, 300, 400, 500, 1000, 2000, 3000, 4000, 5000, 10000, 20000, 50000, 100000, 100000000)
count <- c()
for (i in (1: length(cutPoints))){
    thisCount <- sum(profile$followers_count >= cutPoints[i] & profile$followers_count < cutPoints[i+1])
    count <- c(count, thisCount)
}

library(ggplot2)
intervals <- c("[0, 50)", "[50, 100)", "[100, 200)", "[200, 300)", "[300, 400)",
               "[400, 500)", "[500, 1000)", "[1000, 2000)", "[2000, 3000)", "[3000, 4000)",
               "[4000, 5000)", "[5000, 10000)", "[10000, 20000)", "[20000, 50000)",
               "[50000, 100000)", "[100000, )")
followers <- data.frame(Interval=intervals, Count=count[1:16], lowerBound=cutPoints[1:16])
followers$Interval <- as.character(followers$Interval)
followers$Interval <- factor(followers$Interval, levels=intervals) # arrange in a specific order
ggplot(data=followers, aes(x=Interval, y=Count)) + geom_bar(stat="identity", fill="tomato") + ggtitle("Distribution of Follower Numbers") + theme(axis.text.x = element_text(angle = 45, hjust = 1), plot.title=element_text(family="Times", face="bold", size=20), axis.text=element_text(family="Times", face="bold", size=12), panel.background = element_blank())


data2Sub$targetMedia <- data2Sub$targetFollowers <= 500
model7 <- lm(sourcePos2 ~ perFriend + sourcePos1 + targetPos1 + targetMedia, data=data2Sub)
summary(model7)

for (cut in cutPoints[2: 16]) {
    print(cut)
    data2Sub$targetMedia <- data2Sub$targetFollowers < cut
    print(summary(lm(sourcePos2 ~ perFriend + sourcePos1 + targetPos1 + targetMedia, data=data2Sub)))
}
