import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Taskeen Ali Khan , M.Phil.
##### *Portfolio* 
''')

image = Image.open('tk.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''**Research Assistant**    
        Government Paramedical Institute of Medical Technologies.
- Focus areas: Biochemistry, Molecular Medicine, Pathology and Microbiology Lab Work.
- Contributing to the development of future healthcare professionals.
- Bridging the gap between fundamental science and practical applications in medicine.
- Plays a vital role in understanding human health and disease.
- Develop new drugs, diagnostics, and treatments for a variety of medical conditions.
- Uses techniques from molecular biology, genetics, microbiology and biochemistry to understand the genetic
and molecular basis of disease.
- Aims to develop new therapies that target the underlying causes of disease, rather than just the symptoms.
- Conducted hands-on lab activities, guiding students through experiments and analysis.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse justify-content-center" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Master of Philosophy** (Medical Micro-Biology (M.Phil), *Quaid-i-azam University, Islamabad, Pakistan*','2020-2022')
st.markdown('''
- **GPA:** `3.9`
- **Research thesis entitled:** `Biosynthesis of silver nanoparticles from novel Bischofia Javanica plant loaded chitosan hydrogel: as antimicrobial and wound healing agent.`  
- **Thesis Summary:**  
The current study aimed to develop a new anti-bacterial approach that would surpass antibiotics in therapeutics and will efficiently deal with diverse nature of microbes. The study comprised of synthesis of Ag nano particles using green synthesis technology and its characterization by XRD, FTIR and SEM. Biochemical identificatio  o  bacteria  species  anti-microbia  susceptibilit  profie,  anti-bifilm  ssay and application of Ag nano particles on wound healing in rat model. NPs were applied on burnt wound of rat model and its activity was recorded up to 21 days. A good epithelialization was achieved, as well as a strong wound closure. In comparison to chitosan, silver nanoparticles incorporating membranes demonstrated a high amount of angiogenesis and speedy wound healing 
''')


txt('**Bachelors of Science** (Micro Biology), *Shaheed Benazir Bhutto women university, Peshawar, Pakistan*',
'2013-2018')
st.markdown('''
- GPA: `3.21`
- **Research thesis entitled:** ` Molecular detection of Active HCV in Peshawar ( April-Dec 2017 )"`  
- **Thesis Summary:**  
  Hepatitis C virus (HCV), a blood-borne virus that infects the liver, affects an estimated 4 million Americans, with 3.2 million chronically infected. A study looking at HCV prevalence among 221 people (mostly men) aged 18-80 found a higher infection rate in males (11%) compared to females (8%). The study also showed the highest infection rate (16.41%) in those aged 41-60, with no infections detected in the 10-20 age group. These findings highlight the need for an HCV vaccine to prevent infection, especially considering that behaviors like unsafe drug use and unclean medical instruments can spread the virus.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Research Assistant**, Government Paramedical Institute of Medical Technologies, Pakistan',
'2022-`Current`')
st.markdown('''
- **Focus areas:**
- Biochemistry, Molecular Medicine, Pathology and Microbiology Lab Work.
- Contributing to the development of future healthcare professionals.
- Bridging the gap between fundamental science and practical applications in medicine.
- Plays a vital role in understanding human health and disease.
- Develop new drugs, diagnostics, and treatments for a variety of medical conditions.
- Uses techniques from molecular biology, genetics, microbiology and biochemistry to understand the genetic
and molecular basis of disease.
- Aims to develop new therapies that target the underlying causes of disease, rather than just the symptoms.
- Conducted hands-on lab activities, guiding students through experiments and analysis
''')

txt('**Lecturer**, Riphah international University Pakistan Swat campus (Part time), Pakistan',
'2022-2023')

st.markdown('''
- **Courses taught:**
- Microbiology, Medical Instrumentation
- **Responsibilities:**
- Empowering future healthcare professionals.
- Guiding students through laboratory practicals, Microbiology and pathology labs.
- Bridging the gap between scientific knowledge and its medical applicatio
- Development of new therapies, such as targeted therapy and immunotherapy
''')

txt('**Publications**, antimicrobial and wound healing agent',
'2022')
st.markdown('''
**Biosynthesis of silver nanoparticles from novel Bischofia javanica plant loaded chitosan hydrogel:** as antimicrobial and wound healing agent **Khan, T.A.** et al. Biosynthesis of silver nanoparticles from novel Bischof ia javanica plant loaded chitosan hydrogel: as antimicrobial and wound healing agent. Biomass Conv. Bioref. **13**, 15531–15541 (2022).      
https://doi.org/10.1007/s13399-022-02960-w
''')

txt('**Projects**, Biosynthesis of silver nanoparticles from novel Bischofia Javanica plant loaded chitosan hydrogel: antimicrobial and wound healing agent, Pakistan',
'2020-2022')
st.markdown('''
- Worked on Bio-synthesis of novel nanomaterials as Antimicrobial, Anticancer and wound healing agent.
- Developing metallic nanoparticles (Ag, Fe, Cu) for diverse applications.
- The current study has made a solution to antibiotic resistance by determining the individual and combined efficacies of nanoparticles and antibiotics.
- The study has found that nanoparticles or their combination with antibiotics is a potential alternative way to solve microbial resistance problems.
- In addition, mixing a hydrogel matrix with AgNPs provides considerable wound-healing and antimicrobial activity.
- Concluded that AgNPs should be a selective therapeutic in the field of medicine
- Expected results were obtained from experiments that were performed.
- Published research findings and presented at conferences
- Presented at **International Science seminar organized by Dr Zyta Ziora (The university of Queensland Australia) 28 March 2024.**      
**Molecular detection of active HCV:**
- This molecular study was carried out on active Hepatitis C Virus infection in Peshawar region between AprilDecember 2017.
- The present study was conducted at GENE Tech Diagnostic and Research Laboratory Peshawar, Pakistan.          
**Project on HCV** in the lab of Peshawar Medical Collage ( Oct-December 2017).           
**Internship as microbiologist** in Khyber Teaching Hospital ( December 2017-Feb 2018).
''')

txt('**HONOURS AND AWARDS**, Honours and Awards',
'2008-2024')
st.markdown('''
**Received** 
- Excellent student school award 2008-2010.
- School topper award in matric 2010.
- Laptop from the Government of Pakistan for talented students Scheme.(2014).
- Funding Member of Shaukat Khanum Memorial Hospital Peshawar (2011-2017).
- Govt.Paramedical Institute of Medical Technologies Swat Best Lecturer performance Award by DG health, KPK (2024).
''')

txt('**Lab Experience**, **`Key skills`**',
'2008-Present')
st.markdown('''
Spectrophotometry / FTIR / EDX / UV-Vis Spectroscopy / SEM / HPLC / SDS-PAGE / Gel-electrophoresis /
ELIZA DNA, RNA extraction / PCR / Gel Doc / NANODROP / Enzyme kinetics / Chromatography / Gram staining /
Microscopy / Microbial isolation, culturing and identification / Autoclave / Antioxidant assays / Gram staining /
Synthesis and characterization of Nanoparticles / Production of bioplastic (PLA) / Fermentation / Instrumental
analysis / Plant Stress/ Antibiotics Characterization/ Antibacterial peptides Characterization.
''')

txt('**Seminar and Activities**, Certificates and Participations',
'2015-Present')
st.markdown('''
- Certified Professional in awareness seminar on tuberculosis (9th April 2015).
- Certified professional in World Ozone prevention day on 16th of September 2016.
- Certified in career counselling workshop for female students held on 23-24 May 2016.
- Certified in GENDER SENSITIZATION WORKSHOP FOR MEDIA STUDENTS
- Certified Professional with relief international on BIORISK MANAGEMENT (5-9 Sep 2016).
- International training in randomized controlled trails at COMSTECH, Islamabad.
- Inclusive Science Technology and Innovation policy for OIC member states at COMSTECH, Islamabad.
- Basic plant tissue culture techniques at COMSTECH, Islamabad.
- Member of Blood Donor Society Islamia College, Peshawar (2011-12).
- Funding Member of Shaukat Khanum Memorial Hospital Peshawar (2011-2016).
- Attended awareness seminar on tuberculosis (9th April 2015).
- Participate in World Ozone prevention day on 16th of September 2016.
- Participate in career counselling workshop for female students held on 23-24 May 2016.
- Five days’ work with relief international on BIORISK MANAGEMENT (5-9 September2016).
- Participate in GENDER SENSITIZATION WORKSHOP FOR MEDIA STUDENTS.
''')


st.markdown('''
### **REFEREES**, **`Refrences`** ###      
**Dr. Aamer Ali Shah**       
Chairperson (2020-2022)      
Professor at Department of Microbiology, Quaid-i-Azam, University Islamabad, Pakistan.       
Email: alishah@qau.edu.pk, Phone: +92-51-90643116   
     
**Prof. Dr. Naeem Ali**       
Chairperson and Professor at Department of Microbiology, Quaid-i-Azam University, Islamabad, Pakistan.      
E-mail: naeemali95@gmail.com , Tel. #. +92-51-906431.
''')


#####################
st.markdown('''
### **Digital Skills** ###         
SPSS and SAS / Matlab/Simulik / Graph Prism / Microsoft Office (Outlook, Excel, Word, PowerPoi
''')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/taskeen-ali-5424b32a7/')
txt2('Email', 'alitaskeen43@gmail.com')
txt2('WhatsApp', 'https://wa.me/923449681959')



with open("taskeen_profile.pdf", "rb") as pdf_file:
       pdf_bytes = pdf_file.read()
st.write("###")

    # Download CV button
st.download_button(label="📄 Download my CV", data=pdf_bytes, file_name="Taskeen_Ali_Khan_cv.pdf", mime="application/pdf",)
st.write("######")
st.write(f"""<div class="subtitle" style="text-align: center;">🌾🌻 Have A Wonderfull Day!!! 🌻🌾</div>""", unsafe_allow_html=True)

