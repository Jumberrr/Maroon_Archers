import streamlit as st

# Sample data: Replace this with your actual data
power_plant_data = {
    "01ANGAT_M": ["https://github.com/Jumberrr/Maroon_Archers/blob/main/Capstone/images/01ANGAT_M%20count.PNG", "https://github.com/Jumberrr/Maroon_Archers/blob/main/Capstone/images/01ANGAT_M%20snake.PNG", "https://github.com/Jumberrr/Maroon_Archers/blob/main/Capstone/images/01ANGAT_M%20time%20dist.PNG"],
    "01BAUANG_GS1": ["https://github.com/Jumberrr/Maroon_Archers/blob/main/Capstone/images/01BAUANG_GS1%20count.PNG", "https://github.com/Jumberrr/Maroon_Archers/blob/main/Capstone/images/01BAUANG_GS1%20snake.PNG", "https://github.com/Jumberrr/Maroon_Archers/blob/main/Capstone/images/01BAUANG_GS1%20time%20dist.PNG"],
    # Add more entries as needed
}

# Streamlit app
def main():
    st.title("Watts Up Pinas?!")

    # Dropdown for selecting resource_id
    selected_resource_id = st.selectbox("Select a generator (resource_id)", list(power_plant_data.keys()))

    # Display the selected resource_id
    st.write(f"Selected generator (resource_id): {selected_resource_id}")

    # Display the corresponding images
    images = power_plant_data.get(selected_resource_id, [])
    for i, image_url in enumerate(images, start=1):
        st.image(image_url, caption=f"Image {i}", use_column_width=True)

if __name__ == "__main__":
    main()
