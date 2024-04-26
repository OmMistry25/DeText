import streamlit as st

def extract_text_from_file(uploaded_file):
    # Get file extension
    file_extension = uploaded_file.name.split(".")[-1]
    
    if file_extension == "txt":
        # Read text file directly
        text = uploaded_file.read().decode("utf-8")
    else:
        st.error("Invalid file format. Please upload a .txt, .docx, or .pdf file.")
        return None
    
    return text.lower()

# List of keywords to search for
keywords = [
    "Delve", "Harnessing", "At the heart of", "In essence", "Facilitating", 
    "Intrinsic", "Integral", "Core", "Facet", "Nuance", "Culmination", 
    "Manifestation", "Inherent", "Confluence", "Underlying", "Intricacies", 
    "Epitomize", "Embodiment", "Iteration", "Synthesize", "Amplify", 
    "Impetus", "Catalyst", "Synergy", "Cohesive", "Paradigm", "Dynamics", 
    "Implications", "Prerequisite", "Fusion", "Holistic", "Quintessential", 
    "Cohesion", "Symbiosis", "Integration", "Encompass", "Unveil", "Unravel", 
    "Emanate", "Illuminate", "Reverberate", "Augment", "Infuse", "Extrapolate", 
    "Embody", "Unify", "Inflection", "Instigate", "Embark", "Envisage", 
    "Elucidate", "Substantiate", "Resonate", "Catalyze", "Resilience", 
    "Evoke", "Pinnacle", "Evolve", "Digital Bazaar", "Tapestry", "Leverage", 
    "Centerpiece", "Subtlety", "Immanent", "Exemplify", "Blend", 
    "Comprehensive", "Archetypal", "Unity", "Harmony", "Conceptualize", 
    "Reinforce", "Mosaic"
]

# lower keyword list
keywords = [keyword.lower() for keyword in keywords]


st.title("AI Text Detection App")
st.write("Enter text to check for specific keywords.")


# Option 2: Text Input
text_input = st.text_area("Enter text here:")

if text_input:
    text = text_input.lower()
else:
    st.info("Please upload a file or enter text.")
    text = None  # Set text to None if no input is provided

if text:
    found_keywords = []
    for keyword in keywords:
        if keyword in text:
            found_keywords.append(keyword)

    if found_keywords:
        st.write("**Found Keywords:**")
        for keyword in found_keywords:
            st.success(f"- {keyword}")
    else:
        st.write("No keywords found in the text.")
