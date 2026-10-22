import streamlit as st

st.header(f"Selected Department: {st.session_state.selected_department}")

st.write("The notices for the internal assessment")
container_for_internal_assessment_notice = st.container(border= True)

[col1, col2, col3, col4] = container_for_internal_assessment_notice.columns(4, wrap = True)

[col5, col6, col7, col8] = container_for_internal_assessment_notice.columns(4, wrap = True)


sem_1_notice = col1.file_uploader(label = "Semester I Internal Assessment Notice", type = "pdf",  
                                                       key = "semI_notice", )
sem_2_notice = col2.file_uploader(label = "Semester II Internal Assessment Notice", type = "pdf", 
                                                       key = "semII_notice", )
sem_3_notice = col3.file_uploader(label = "Semester III Internal Assessment Notice", type = "pdf", 
                                                       key = "semIII_notice", )
sem_4_notice = col4.file_uploader(label = "Semester IV Internal Assessment Notice", type = "pdf", 
                                                       key = "semIV_notice", )
sem_5_notice = col5.file_uploader(label = "Semester V Internal Assessment Notice", type = "pdf", 
                                                       key = "semV_notice", )
sem_6_notice = col6.file_uploader(label = "Semester VI Internal Assessment Notice", type = "pdf", 
                                                       key = "semVI_notice", )
sem_7_notice = col7.file_uploader(label = "Semester VII Internal Assessment Notice", type = "pdf", 
                                                       key = "semVII_notice", )
sem_8_notice = col8.file_uploader(label = "Semester VIII Internal Assessment Notice", type = "pdf", 
                                                       key = "semVIII_notice", )