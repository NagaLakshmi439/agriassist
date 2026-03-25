def chatbot_reply(message):
    message = message.lower()

    # Crop suggestions
    if "crop" in message:
        return "Recommended crops: Rice, Wheat, Maize, Sugarcane"

    # Fertilizer advice
    elif "fertilizer" in message:
        return "Use NPK fertilizers and organic compost for better yield"

    # Soil related
    elif "soil" in message:
        return "Maintain balanced pH (6-7) and check nutrients like N, P, K, Mg"

    # Weather
    elif "weather" in message:
        return "Please use the weather module to check real-time weather"

    # Disease
    elif "disease" in message:
        return "Upload plant leaf image to detect diseases"

    # Default reply
    else:
        return "I am AgriAssist Bot 🌱. Ask me about crops, soil, fertilizers or weather!"
