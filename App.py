import streamlit as st

st.set_page_config(layout="wide")

st.title("📖 Story Video Background App")

# 🔗 Ready-made free background links (Images + Videos)
backgrounds = {
    # Images
    "Peaceful Room": "https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg",
    "Dreamy Sky": "https://images.pexels.com/photos/1103970/pexels-photo-1103970.jpeg",
    "Warm Library": "https://images.pexels.com/photos/256541/pexels-photo-256541.jpeg",
    "Cozy Lights": "https://images.pexels.com/photos/112811/pexels-photo-112811.jpeg",
    "Blue Abstract": "https://images.pexels.com/photos/7130555/pexels-photo-7130555.jpeg",
    "Golden Sunset": "https://images.pexels.com/photos/210186/pexels-photo-210186.jpeg",
    "Forest Path": "https://images.pexels.com/photos/4827/nature-forest-trees-fog.jpeg",
    "Ocean Calm": "https://images.pexels.com/photos/127673/pexels-photo-127673.jpeg",
    "Night Sky Stars": "https://images.pexels.com/photos/1257860/pexels-photo-1257860.jpeg",
    "Mountain Peace": "https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg",

    # Videos
    "Abstract Lights (Loop)": "https://videos.pexels.com/video-files/856673/856673-hd_1920_1080_30fps.mp4",
    "Nature Waterfall (Loop)": "https://videos.pexels.com/video-files/855248/855248-hd_1920_1080_30fps.mp4",
    "Calm Ocean Waves": "https://videos.pexels.com/video-files/854936/854936-hd_1920_1080_30fps.mp4",
    "Flowing Clouds": "https://videos.pexels.com/video-files/2011016/2011016-hd_1920_1080_24fps.mp4",
    "City Night Lights": "https://videos.pexels.com/video-files/854940/854940-hd_1920_1080_30fps.mp4",
}

# Dropdown menu for selection
choice = st.selectbox("🎨 Choose Background:", list(backgrounds.keys()))

# Selected background link
selected_bg = backgrounds[choice]

# Show image or video
if selected_bg.endswith(".mp4"):
    st.video(selected_bg, loop=True, autoplay=True)
else:
    st.image(selected_bg, use_column_width=True)

# Story text input
story_text = st.text_area("✍️ Write your story text here")

# Show story text on screen
if story_text:
    st.markdown(
        f"<div style='padding:20px; font-size:22px; line-height:1.6; color:white; "
        f"text-shadow: 2px 2px 4px black;'>{story_text}</div>",
        unsafe_allow_html=True,
    )
