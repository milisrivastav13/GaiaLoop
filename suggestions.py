def eco_suggestions(transport, electricity, diet):
    tips = []
    if transport > 10:
        tips.append("🚴 Try biking, walking, or public transport for shorter distances.")
    if electricity > 10:
        tips.append("💡 Switch off unused appliances and try LED lights.")
    if diet == 2:
        tips.append("🥦 Reduce meat consumption a few days a week to lower emissions.")
    if not tips:
        tips.append("🌱 You're on the right path! Keep living sustainably.")
    return tips