import streamlit as st
import docx2txt
from PyPDF2 import PdfReader

def extract_text_from_file(uploaded_file):
   # Get file extension
   file_extension = uploaded_file.name.split(".")[-1]
  
   if file_extension == "txt":
       # Read text file directly
       text = uploaded_file.read().decode("utf-8")
   elif file_extension == "docx":
       # Extract text from docx
       text = docx2txt.process(uploaded_file)
   elif file_extension == "pdf":
       # Extract text from pdf
       pdf_reader = PdfReader(uploaded_file)
       text = ""
       for page in pdf_reader.pages:
           text += page.extract_text()
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
   "Reinforce", "Mosaic", "Aims to bridge", "Aims to democratize",
   "Aims to foster innovation and collaboration", "Becomes increasingly evident",
   "Behind the Veil", "Breaking barriers", "Breakthrough has the potential to revolutionize the way",
   "Bringing us", "Bringing us closer to a future", "By combining the capabilities", "By harnessing the power",
   "Capturing the attention", "Continue to advance", "Continue to make significant strides",
   "Continue to push the boundaries", "Continues to progress rapidly", "Crucial to be mindful",
   "Crucially", "Cutting-edge", "Drive the next big", "Encompasses a wide range of real-life scenarios",
   "Enhancement further enhances", "Ensures that even", "Essential to understand the nuances", "Excitement",
   "Exciting opportunities", "Exciting possibilities", "Exciting times lie ahead as we unlock the potential of",
   "Excitingly", "Expanded its capabilities", "Expect to witness transformative breakthroughs",
   "Expect to witness transformative breakthroughs in their capabilities", "Exploration of various potential answers",
   "Explore the fascinating world", "Exploring new frontiers", "Exploring this avenue",
   "Foster the development", "Future might see us placing", "Groundbreaking way",
   "Groundbreaking advancement", "Groundbreaking study", "Groundbreaking technology",
   "Have come a long way in recent years", "Hold promise", "Implications are profound",
   "Improved efficiency in countless ways", "In the fast-paced world",
   "Innovative service", "Intrinsic differences", "It discovered an intriguing approach",
   "It remains to be seen", "It serves as a stepping stone towards the realization",
   "Latest breakthrough signifies", "Latest offering",
   "Let’s delve into the exciting details", "Main message to take away",
   "Make informed decisions", "Mark a significant step forward",
   "Mind-boggling figure", "More robust evaluation",
   "Navigate the landscape",
   "Notably",
   "One step closer",
   "One thing is clear",
   "Only time will tell",
   "Opens up exciting possibilities",
   "Paving the way for enhanced performance",
   "Possibilities are endless",
   "Potentially revolutionizing the way",
   "Push the boundaries",
   "Raise fairness concerns",
   "Raise intriguing questions",
   "Rapid pace of development",
   "Rapidly developing",
   "Redefine the future",
   "Remarkable abilities",
   "Remarkable breakthrough",
   "Remarkable proficiency",
   "Remarkable success",
   "Remarkable tool",
   "Remarkably",
   "Renowned",
   "Represent a major milestone",
   "Represents a significant milestone in the field",
   "Revolutionize the way",
   "Revolutionizing the way",
   "Risks of drawing unsupported conclusions",
   "Seeking trustworthiness",
   "Significant step forward",
   "Significant strides",
   "The necessity of clear understanding",
   "There is still room for improvement",
   "Transformative power",
   "Truly exciting",
   "Uncover hidden trends",
   "Understanding of the capabilities",
   "Unleashing the potential",
   "Unlocking the power",
   "Unraveling",
   "We can improve understanding and decision-making",
   "Welcome your thoughts",
   "What sets this apart",
   "What’s more",
   "With the introduction"
]


keywords = [keyword.lower() for keyword in keywords]




st.title("Detect AI generated texts! :mag_right:")
st.write("Upload a text file, Word document, PDF, or directly enter text to check for specific keywords.")


# Option 1: File Uploader
uploaded_file = st.file_uploader("Choose a file (optional)", type=["txt", "docx", "pdf"])


# Option 2: Text Input
text_input = st.text_area("Or enter text here:")


if uploaded_file is not None:
   text = extract_text_from_file(uploaded_file)
elif text_input:
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

