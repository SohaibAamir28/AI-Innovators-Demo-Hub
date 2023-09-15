import streamlit as st

# Page Title
st.title("Quantum-Scribe: AI-Powered Automatic Manuscript Generation")

# Project Idea
st.subheader("Idea")
st.write("Quantum-Scribe is a pioneering AI project that pushes the boundaries of content creation. Leveraging the power of natural language processing and deep learning, our system generates well-structured, coherent manuscripts, reports, and articles on a wide range of topics. Whether you're a student, researcher, or writer, Quantum-Scribe streamlines the writing process, enabling you to focus on ideas and insights rather than struggling with words. Our project is poised to transform how information is documented, shared, and disseminated in various fields. Join us in reshaping the future of written communication.")

# Benefits
st.subheader("Benefits")
st.write("Quantum-Scribe offers the following benefits:")
st.write("- Time-Saving: Quantum-Scribe accelerates content creation, freeing up your time.")
st.write("- Enhanced Creativity: Say goodbye to writer's block and hello to inspired writing.")
st.write("- High-Quality Content: Expect content that meets the highest standards.")
st.write("- Wide Range of Topics: Quantum-Scribe covers diverse subjects, from academic research to marketing materials.")

# Search Box
text_box_content = "Quantum-Scribe"
user_input = st.text_area("Quantum-Scribe | AI Manuscript Generation | Revolutionizing Content Creation", value=text_box_content)

url = 'https://github.com/SohaibAamir28/Quantum-Scribe/blob/main/Quantum_Scribe_Fine_Tuning.ipynb'
st.markdown(f'''
<a href={url}><button style="background-color:GreenYellow;">Stackoverflow</button></a>
''',
unsafe_allow_html=True)

# Page Summary
st.subheader("Summary")
st.write("Quantum-Scribe revolutionizes content creation using AI. Our project aims to automate the generation of high-quality manuscripts, reports, and articles, saving time and enhancing creativity.")

# Footer
st.text("© 2023 Hack Whizzes Team")
