daysOfScores = int (input ("How many days of scores? "))
totalScore = 0
dayCount = 0
dailyScoreText = "Enter score for day "
for dailyScore in range(1, daysOfScores + 1):
    dayCount = dayCount + 1
    dailyScorePrompt = dailyScoreText + str(dayCount) + ": "
    dailyScore = int(input(dailyScorePrompt))
    totalScore = dailyScore + totalScore
print ("The total score of the", daysOfScores, "days is", totalScore)