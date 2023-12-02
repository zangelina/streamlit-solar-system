import streamlit as st
import os

#define the planets pages with mass and age parameters and image
def planetInfo(planet, mass, age, name):
    st.title(planet + " Weight and Age") #1st NEW
    imageName = os.path.join("planetpics/" + planet.lower() + ".jpeg")
    if planet == "Pluto":
        st.image(imageName, use_column_width = True)
        st.image("planetpics/welovepluto.png")
        st.caption("Some may say Pluto isn't a planet, but in our hearts, Pluto maintains its status. We should go ahead and call all the dwarf planets planets!") #2nd NEW
    else:
        st.image(imageName, use_column_width = True)
        st.caption(planet + ", in all its glory.") #2nd NEW
    st.header("Your weight and age on " + planet + ":")
    mercury_gravity = 3.7
    mercury_period = 4.15
    venus_gravity = 8.8
    venus_period = 1.62
    mars_gravity = 3.7
    mars_period = 0.531
    jupiter_gravity = 24.7
    jupiter_period = 0.084
    saturn_gravity = 10.5
    saturn_period = 0.034
    uranus_gravity = 9.0
    uranus_period = 0.012
    neptune_gravity = 11.7
    neptune_period = 0.006
    pluto_gravity = 0.49
    pluto_period = 0.004
    
    if planet == "Mercury":
        mercury_gravity = 3.7
        mercury_weight = round(mercury_gravity * mass/9.8,2) #mass referring to Earth weight before conversion
        mercury_mass = round(mass/9.8,2)
        mercury_age = round(mercury_period * age,2)
        st.write(name + ", you weigh " + str(mercury_weight) + " pounds on " + planet + "!")
        st.write(name + ", you are " + str(mercury_mass) + " kilograms on " + planet + "!")
        st.write(name + ", you are " + str(mercury_age) + " years old in Mercury years! One Earth year is around 4.15 Mercury years.")
    elif planet == "Venus":
        venus_weight = round(venus_gravity * mass/9.8,2)
        venus_mass = round(mass/9.8,2)
        venus_age = round(venus_period * age,2)
        st.write(name + ", you weigh " + str(venus_weight) + " pounds on " + planet + "!")
        st.write(name + ", you are " + str(venus_mass) + " kilograms on " + planet + "!")
        st.write(name + ", you are " + str(venus_age) + " years old in Venus years.")
    elif planet == "Mars":
        mars_weight = round(mars_gravity * mass/9.8,2)
        mars_mass = round(mass/9.8,2)
        mars_age = round(mars_period * age,2)
        st.write(name + ", you weigh " + str(mars_weight) + " pounds on " + planet + "!")
        st.write(name + ", you are " + str(mars_mass) + " kilograms on " + planet + "!")
        st.write(name + ", you are " + str(mars_age) + " years old in Mars years! One Earth year is around 0.531 Mars years.")
    elif planet == "Jupiter":
        jupiter_weight = round(jupiter_gravity * mass/9.8,2)
        jupiter_mass = round(mass/9.8,2)
        jupiter_age = round(jupiter_period * age,2)
        st.write(name + ", you weigh " + str(jupiter_weight) + " pounds on " + planet + "!")
        st.write(name + ", you are " + str(jupiter_mass) + " kilograms on " + planet + "!")
        st.write(name + ", you are " + str(jupiter_age) + " years old in Jupiter years! One Earth year is around 0.084 Jupiter years.")
    elif planet == "Saturn":
        saturn_weight = round(saturn_gravity * mass/9.8,2)
        saturn_mass = round(mass/9.8,2)
        saturn_age = round(saturn_period * age,2)
        st.write(name + ", you weigh " + str(saturn_weight) + " pounds on " + planet + "!")
        st.write(name + ", you are " + str(saturn_mass) + " kilograms on " + planet + "!")
        st.write(name + ", you are " + str(saturn_age) + " years old in Saturn years! One Earth year is around 0.034 Saturn years.")
    elif planet == "Uranus":
        uranus_weight = round(uranus_gravity * mass/9.8,2)
        uranus_mass = round(mass/9.8,2)
        uranus_age = round(uranus_period * age,2)
        st.write(name + ", you weigh " + str(uranus_weight) + " pounds on " + planet + "!")
        st.write(name + ", you are " + str(uranus_mass) + " kilograms on " + planet + "!")
        st.write(name + ", you are " + str(uranus_age) + " years old in Uranus years.")
    elif planet == "Neptune":
        neptune_weight = round(neptune_gravity * mass/9.8,2)
        neptune_mass = round(mass/9.8,2)
        neptune_age = round(neptune_period * age,2)
        st.write(name + ", you weigh " + str(neptune_weight) + " pounds on " + planet + "!")
        st.write(name + ", you are " + str(neptune_mass) + " kilograms on " + planet + "!")
        st.write(name + ", you are " + str(neptune_age) + " years old in Neptune years! One Earth year is around 0.006 Neptune years.")
    elif planet == "Pluto":
        pluto_weight = round(pluto_gravity * mass/9.8,2)
        pluto_mass = round(mass/9.8,2)
        pluto_age = round(pluto_period * age,2)
        st.write(name + ", you weigh " + str(pluto_weight) + " pounds on " + planet + "!")
        st.write(name + ", you are " + str(pluto_mass) + " kilograms on " + planet + "!")
        st.write(name + ", you are " + str(pluto_age) + " years old in Pluto years! One Earth year is around 0.004 Pluto years.")
    
    st.header("How we calculated your data:")
    st.write("For your weight, we took " + planet + "'s gravitational force multiplied by your mass, " + str(round(mass/9.8,2)) + " kg.")
    st.write("Remember, your mass always stays the same, regardless of your location! Conservation of mass 😆. Your mass is your Earth weight divided by 9.8 m/s^2.")
    st.write("For your age, " + str(age) + ", we multiplied by " + planet + "'s period around the Sun compared to the Earth to get your age on " + planet + ".")

#Create a planet selector
st.sidebar.title("Solar System Selector")
planet_choice = st.sidebar.selectbox("Select your planet of inhabitance!", ["Mercury","Venus","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"]) #3rd NEW

#Add input box for age and mass
age = st.sidebar.number_input("Your age (in Earth years, of course)", min_value = 1)
mass = st.sidebar.number_input("Your current weight, in Earth gravity (don't worry, we will do the number crunching for you to find your mass!)")

#Add input box for name
name = st.sidebar.text_input("Your name") #4th NEW

#Display selected planet data
if planet_choice == "Mercury":
    planetInfo("Mercury", mass, age, name)
elif planet_choice == "Venus":
    planetInfo("Venus", mass, age, name)
elif planet_choice == "Mars":
    planetInfo("Mars", mass, age, name)
elif planet_choice == "Jupiter":
    planetInfo("Jupiter", mass, age, name)
elif planet_choice == "Saturn":
    planetInfo("Saturn", mass, age, name)
elif planet_choice == "Uranus":
    planetInfo("Uranus", mass, age, name)
elif planet_choice == "Neptune":
    planetInfo("Neptune", mass, age, name)
elif planet_choice == "Pluto":
    planetInfo("Pluto", mass, age, name)
