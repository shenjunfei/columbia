data <- data.frame(alterSentDivFriend1000=data2Sub$perFriend*1000, 
                   alterSentPrevious=data2Sub$targetPos1,
                   egoSentNow=data2Sub$sourcePos2, 
                   egoSentPrevious=data2Sub$sourcePos1,
                   alterFollowers=data2Sub$targetFollowers)

model4 <- lm(egoSentNow ~ alterSentDivFriend1000 + egoSentPrevious + alterSentPrevious, data=data)
data$alterIsMedia <- data$alterFollowers < 200
model200 <- lm(egoSentNow ~ alterSentDivFriend1000 + egoSentPrevious + alterSentPrevious + alterIsMedia, data=data)
data$alterIsMedia <- data$alterFollowers < 2000
model2000 <- lm(egoSentNow ~ alterSentDivFriend1000 + egoSentPrevious + alterSentPrevious + alterIsMedia, data=data)

# Put model estimates into temporary data.frames:
model4Frame <- data.frame(Variable = rownames(summary(model4)$coef),
                          Coefficient = summary(model4)$coef[, 1],
                          SE = summary(model4)$coef[, 2],
                          Model = "Model 3")
model200Frame <- data.frame(Variable = rownames(summary(model200)$coef),
                            Coefficient = summary(model200)$coef[, 1],
                            SE = summary(model200)$coef[, 2],
                            Model = "Model 5, Cut Point = 200")
model2000Frame <- data.frame(Variable = rownames(summary(model2000)$coef),
                             Coefficient = summary(model2000)$coef[, 1],
                             SE = summary(model2000)$coef[, 2],
                             Model = "Model 5, Cut Point = 2000")
# Combine these data.frames
allModelFrame <- data.frame(rbind(model4Frame, model200Frame, model2000Frame))

# Specify the width of your confidence intervals
interval1 <- -qnorm((1-0.9)/2)  # 90% multiplier
interval2 <- -qnorm((1-0.95)/2)  # 95% multiplier

library(ggplot2)
# Plot
zp1 <- ggplot(allModelFrame, aes(colour = Model))
zp1 <- zp1 + geom_hline(yintercept = 0, colour = gray(1/2), lty = 2)
zp1 <- zp1 + geom_linerange(aes(x = Variable, ymin = Coefficient - SE*interval1,
                                ymax = Coefficient + SE*interval1),
                                lwd = 1, position = position_dodge(width = 1/2))
zp1 <- zp1 + geom_pointrange(aes(x = Variable, y = Coefficient, ymin = Coefficient - SE*interval2,
                                 ymax = Coefficient + SE*interval2),
                                 lwd = 1/2, position = position_dodge(width = 1/2),
                                 shape = 21, fill = "WHITE")
zp1 <- zp1 + coord_flip()
zp1 <- zp1 + ggtitle("Confidence Intervals of Variables") + theme(plot.title=element_text(family="Times", face="bold", size=20), axis.text=element_text(family="Times", face="bold", size=12), panel.background = element_blank())
print(zp1)  # The trick to these is position_dodge().

