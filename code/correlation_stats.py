from correlation import pearson, spearman, kendall


def get_correlation_stats(dataFrame):
    correlation_scores = []
    colmNames = list(dataFrame)

    relevantPersonalityDataColmNames = colmNames[:5]
    relevantSARTDataColmNames = colmNames[5:]

    correlation_scores = {}

    # 5 colmns in Personality Data, 2 Colmns in Sart Data
    for personalityColm in relevantPersonalityDataColmNames:
        for sartColm in relevantSARTDataColmNames:
            personalityData = dataFrame[personalityColm]
            sartData = dataFrame[sartColm]

            pearsonScore = pearson(list(personalityData), list(sartData))
            spearmanScore = spearman(list(personalityData), list(sartData))
            kendallScore = kendall(list(personalityData), list(sartData))
            
            correlation_scores[personalityColm+" - "+sartColm] = [pearsonScore, spearmanScore, kendallScore]

    return dataFrame, correlation_scores