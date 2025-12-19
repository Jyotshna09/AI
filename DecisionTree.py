def play_tennis(outlook, humidity, windy):
    if outlook == "Sunny":
        if humidity == "High":
            return "No"
        else:
            return "Yes"

    elif outlook == "Rain":
        if windy == "Strong":
            return "No"
        else:
            return "Yes"

    else: 
        return "Yes"
print(play_tennis("Sunny", "High", "Weak"))      
print(play_tennis("Sunny", "Normal", "Weak"))    
print(play_tennis("Rain", "High", "Strong"))     
print(play_tennis("Overcast", "High", "Weak"))   