import streamlit as st

def password_checker(password):
    score = 0
    tips = []

    if len(password) >=8:
        score += 1
    else:
        tips.append("Use atleast 8 characters with atleast 1 special character and 1 digit")
    if any(c.isupper() for c in password):
            score += 1
    else:
            tips.append("Include Uppercase letter")  
    if any(c.islower() for c in password):
            score += 1
    else:
            tips.append("Include Lowercase letter")  
    if any(c.isdigit() for c in password):
            score += 1
    else:
            tips.append("Add a number (1-9)")   
    if any(c in "!@#$%^&*" for c in password):
            score += 1
    else:
            tips.append("Password must consist of a special character (!@#$%^&*)")
    return score, tips
    
def main():
           st.title("Password Strength Meter🔑")
           password = st.text_input("Enter your Password", type= "password")
           if password:
                score, tips = password_checker(password)
                if score == 5:
                    st.success("✅strong Password!")
                elif score == 3 or score == 4:
                    st.warning("⚠️Moderate Password")
                else:
                       st.error("❌Weak Password!")
                for tip in tips:
                       st.write(tip)

main()