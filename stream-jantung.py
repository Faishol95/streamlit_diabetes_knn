# load library
import pickle
import streamlit as st


# load save model/ Model yang telah dibuat sebelumnya
knn = pickle.load(open('gagal_jantung.sav','rb'))

# judul/Title web
st.title('Prediksi Penyakit Gagal Jantung')
st.markdown("""
### ini merupakan aplikasi web berbasis Machine Learning untuk prediksi penyakit jantung
### Dibuat oleh: kelompok 6 
Anggota: 1. Nurfaida Oktafiani 
         2. Faishol Nuris Solihin
         3. ZOFAN AFANDI
         4. Daffa Ardiyansyah
            
________________________________________________________________________________________________
            
""")

# Form inputan dengan 3 kolom
col1, col2, col3 = st.columns(3)

with col1:
    Age = st.slider("Inputkan Nilai Umur (Age) :",1,100) #Inputan untuk feature Age

with col2:
    optionGender = st.selectbox(        #Inputan untuk feature Gender
    'Pilih Jenis Kelamin (Gender) :',
    ('Male/Pria','Female/Wanita'),
    )

    if optionGender == 'Male/Pria':
        Sex = 1
    elif optionGender == 'Female/Wanita':
        Sex = 0
    

with col3:
    optionCPT = st.selectbox(
    'Pilih nyeri dada (ChestPainType) :',   #Inputan untuk feature ChestPainType
    ('TA: Typical Angina', 'ATA: Atypical Angina', 'NAP: Non-Anginal Pain', 'ASY: Asymptomatic'),
    )
    if optionCPT == 'TA: Typical Angina':
        ChestPainType = 3
    elif optionCPT == 'ATA: Atypical Angina':
        ChestPainType = 1
    elif optionCPT == 'NAP: Non-Anginal Pain':
        ChestPainType = 2
    elif optionCPT == 'ASY: Asymptomatic':
        ChestPainType = 0

with col1: #Inputan untuk feature RestingBP
    RestingBP = st.slider('Inputkan Nilai tekanan darah saat istirahat (RestingBP) :',0,250,110) 

with col2: #Inputan untuk feature Cholesterol
    Cholesterol = st.slider('Inputan Nilai Kolesterol (Cholesterol):',0,800,150)

with col3: #Inputan untuk feature FastingBS
    optionFBS = st.selectbox(
    'Pilih Kadar Gula Darah saat Puasa (FastingBS):',
    ('> 120 mg/dl(1)', '<= 120 mg/dl(0)'),
    )
    if optionFBS == '> 120 mg/dl(1)':
        FastingBS = 1
    elif optionFBS == '<= 120 mg/dl(0)':
        FastingBS = 0

with col1:#Inputan untuk feature RestingECG
    optionRECG = st.selectbox(
    'Pilih hasil elektrokardiogram istirahat (RestingECG):',
    ('Normal', 'ST','LVH'),
    )
    if optionRECG == 'Normal':
        RestingECG = 1
    elif optionRECG == 'ST':
        RestingECG = 2
    elif optionRECG == 'LVH':
        RestingECG = 0
    
with col2: #Inputan untuk feature MaxHR
    MaxHR = st.slider('Input Nilai Detak jantung maksimum (MaxHR):',60,202)

with col3: #Inputan untuk feature ExerciseAngina
    optionEAngina = st.selectbox(
    'Pilih angin duduk/angina akibat olahraga (ExerciseAngina):',
    ('Y: Yes', 'N: No'),
    )

    if optionEAngina == 'Y: Yes':
        ExerciseAngina = 1
    elif optionEAngina == 'N: No':
        ExerciseAngina = 0

with col1: #Inputan untuk feature Oldpeak
    Oldpeak = st.number_input('Inputkan oldpeak/Nilai diukur dalam Depresi (Oldpeak):')

with col2: #Inputan untuk feature ST_Slope
    optionSTslope = st.selectbox(
    'Pilih Segmen ST/kemiringan denyut jantung (ST_Slope):',
    ('Up: upsloping', 'Flat: flat', 'Down: downsloping'),
    )

    if optionSTslope == 'Up: upsloping':
        ST_Slope = 2
    elif optionSTslope == 'Flat: flat':
        ST_Slope = 1
    elif optionSTslope == 'Down: downsloping':
        ST_Slope = 0



# Variabel untuk menyimpan prediksi
heart_diagnosis = ''

# Membuat tombol prediksi
if st.button("Prediski Penyakit jantung"):
    # Melakukan prediksi/clasifikasi knn berdasarkan Nilai yang telah di inputkan
    heart_prediction = knn.predict([[Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]])

    # statment hasil dari prediksi :
    if (heart_prediction[0]==0):
        st.write(heart_prediction[0])
        heart_diagnosis='Pasien tidak terkena penakit jantung'
        st.success(heart_diagnosis) # memberi background warna hijau
    else:
        st.write(heart_prediction[0])
        heart_diagnosis= 'Pasien terkena penyakit jantung'
        st.error(heart_diagnosis) # memberi background warna Merah

