import streamlit as st

st.header(f"Selected Department: {st.session_state.selected_department}")

st.write("The notices for the internal assessment")
container_for_internal_assessment_notice = st.container(border= True)

container_for_internal_assessment_notice.file_uploader(label = "Semester I Internal Assessment Notice", type = "pdf",  
                                                       key = "semI_notice")
container_for_internal_assessment_notice.file_uploader(label = "Semester II Internal Assessment Notice", type = "pdf", 
                                                       key = "semII_notice")
container_for_internal_assessment_notice.file_uploader(label = "Semester III Internal Assessment Notice", type = "pdf", 
                                                       key = "semIII_notice")
container_for_internal_assessment_notice.file_uploader(label = "Semester IV Internal Assessment Notice", type = "pdf", 
                                                       key = "semIV_notice")
container_for_internal_assessment_notice.file_uploader(label = "Semester V Internal Assessment Notice", type = "pdf", 
                                                       key = "semV_notice")
container_for_internal_assessment_notice.file_uploader(label = "Semester VI Internal Assessment Notice", type = "pdf", 
                                                       key = "semVI_notice")
container_for_internal_assessment_notice.file_uploader(label = "Semester VII Internal Assessment Notice", type = "pdf", 
                                                       key = "semVII_notice")
container_for_internal_assessment_notice.file_uploader(label = "Semester VIII Internal Assessment Notice", type = "pdf", 
                                                       key = "semVIII_notice")