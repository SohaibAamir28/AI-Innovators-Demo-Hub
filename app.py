import streamlit as st

def main():
    st.title("QuantumScribe Demo")
    st.write("Welcome to the QuantumScribe demonstration.")

    # Add a button that links to the GitHub notebook
    if st.button("Quantum-Scribe Demo"):
        st.write("Redirecting to Quantum-Scribe GitHub notebook...")
        st.markdown("[GitHub Notebook](https://github.com/SohaibAamir28/Quantum-Scribe/blob/main/Quantum_Scribe_Fine_Tuning.ipynb)")

if __name__ == "__main__":
    main()
