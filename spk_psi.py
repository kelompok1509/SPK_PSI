import streamlit as st
import numpy as np
import pandas as pd


# Add a custom CSS style to center-align text
centered_text_style = """
    <style>
        .centered-text {
            text-align: center;
        }
    </style>
"""

# Render the custom CSS style
st.markdown(centered_text_style, unsafe_allow_html=True)

# Use st.header with the centered-text class
st.markdown('''
    <div class="centered-text">
        <h2>
            Sistem Pendukung Keputusan 
            Perekrutan Guru Bahasa Inggris Untuk Tingkat Sekolah Dasar 
            Menggunakan Metode <i> Preference Selection Index </i> (PSI)
        </h2>
    </div>
    <br>''', 
    unsafe_allow_html=True)

st.markdown('''
    :red[*Note :] Minimal jumlah alternatif adalah sebanyak <u><b>2 (DUA)</b></u>
    untuk mendapatkan hasil sebagai pendukung keputusan.''', unsafe_allow_html=True)


# Define array variable
alt_name_value          = np.array([])    
alt_pendidikan_value    = np.array([])
alt_pengalaman_value    = np.array([])
alt_kemampuan_mengajar  = np.array([])
alt_penguasaan_conver   = np.array([])
alt_penguasaan_toefl    = np.array([])
alt_usia                = np.array([])


#Define the value on an option array and convert it to number
education_levels        = {'SLTA': 1, 'Diploma': 2, 'S1': 3, 'S2': 4, 'S3': 5}
teach_ability           = {'Tidak Baik': 1, 'Kurang Baik': 2, 'Cukup Baik': 3, 'Baik': 4, 'Sangat Baik': 5}
conversation_ability    = {'Tidak Fasih': 1, 'Kurang Fasih': 2, 'Cukup Fasih': 3, 'Fasih': 4, 'Sangat Fasih': 5}

# ==================================== A set of lines for input value ===================================


alt_value = st.number_input('Input Jumlah Calon Guru Bahasa Inggris :', min_value=0, value=0, step=1)

# Inisialisasi list alt_name_value dengan panjang yang sesuai dengan inputan user
alt_name_value = ["" for _ in range(int(alt_value))]

for i in range(int(alt_value)):
    alt_name_value[i] = st.text_input(f'Nama Calon Guru ke-{i+1}:')


if alt_value > 1:
    st.markdown('''
        <hr style="height:5px;border-width:0;color:gray;background-color:gray">
        <br>
        <h3>
        Memasukkan Nilai Jumlah Guru Bahasa Inggris Yang Ingin Di Rekrut  
        </h3>
        <br>''', 
    unsafe_allow_html=True)
    st.markdown('''
    :red[*Note : ]Maksimal Nilai Yang Dapat Di Masukkan Adalah Kurang Dari Jumlah Calon Guru Bahasa Inggris.
    ''', unsafe_allow_html=True)
    jum_alternatif = st.number_input('Input Jumlah Guru Bahasa Inggris Yang Ingin Di Rekrut :', min_value=0, value=0, step=1, max_value=alt_value-1)
    
    if jum_alternatif > 0:

        st.markdown('''
            <hr style="height:5px;border-width:0;color:gray;background-color:gray">
            <br>
            <h3>
            Memasukkan Nilai Pada Setiap Alternatif Calon Guru Di Setiap Kriteria :  
            </h3>
            <br>''', 
        unsafe_allow_html=True)
        
        st.title('Memasukkan Nilai Untuk Kriteria Pendidikan - C1')
        for i in range(int(alt_value)):
            
            #
            # C1 : Kriteria Pendidikan
            #
            education_levels_options = ['SLTA', 'Diploma', 'S1', 'S2', 'S3']
            selected_education_levels_option = st.selectbox(f"Calon Guru ke-{i + 1}: {alt_name_value[i]}", education_levels_options)
            
            c1 = education_levels[selected_education_levels_option]
            alt_pendidikan_value = np.append(alt_pendidikan_value, c1)
        
        #
        # C2 : Kriteria Pengalaman Kerja
        #
        st.title('Memasukkan Nilai Untuk Kriteria Pengalaman Kerja (Tahun) - C2 ')
        st.markdown('''
            :red[*]isi dengan nilai <u><b>0 (NOL) jika tidak memiliki pengalaman kerja.</b></u>
            ''', unsafe_allow_html=True)
        for i in range(int(alt_value)):
            
            years_of_experience = st.number_input(f"Calon Guru ke-{i + 1}: {alt_name_value[i]}", min_value=0, value=0, step=1)
            
            if years_of_experience > 5:
                c2 = 5
                alt_pengalaman_value = np.append(alt_pengalaman_value, c2)
            elif 4 < years_of_experience <= 5:
                c2 = 4
                alt_pengalaman_value = np.append(alt_pengalaman_value, c2)
            elif 3 < years_of_experience <= 4:
                c2 = 3
                alt_pengalaman_value = np.append(alt_pengalaman_value, c2)
            elif 2 < years_of_experience <= 3:
                c2 = 2
                alt_pengalaman_value = np.append(alt_pengalaman_value, c2)
            else: # 0 <= years_of_experience < 2
                c2 = 1
                alt_pengalaman_value = np.append(alt_pengalaman_value, c2)
        
        
        #
        # C3 : Kriteria Kemampuan Mengajar
        #
        st.title('Memasukkan Nilai Untuk kriteria Kemampuan Mengajar - C3')
        for i in range(int(alt_value)):
            
            teach_ability_options = ['Tidak Baik', 'Kurang Baik', 'Cukup Baik', 'Baik', 'Sangat Baik']
            selected_teach_ability_option = st.selectbox(f"Calon Guru ke-{i + 1}: {alt_name_value[i]}", teach_ability_options)
            
            c3 = teach_ability[selected_teach_ability_option]
            alt_kemampuan_mengajar = np.append(alt_kemampuan_mengajar, c3)
        
        
        #
        # C4 : Kriteria Penguasaan Conversation
        #
        st.title('Memasukkan Nilai Untuk Kriteria Penguasaan Conversation - C4')
        for i in range(int(alt_value)):
            
            conversation_ability_options = ['Tidak Fasih', 'Kurang Fasih', 'Cukup Fasih', 'Fasih', 'Sangat Fasih']
            selected_conversation_ability_option = st.selectbox(f"Calon Guru ke-{i + 1}: {alt_name_value[i]}", conversation_ability_options)

            c4 = conversation_ability[selected_conversation_ability_option]
            alt_penguasaan_conver = np.append(alt_penguasaan_conver, c4)
        
        
        #
        # C5 : Kriteria Penguasaan TOEFL
        #
        st.title('Memasukkan Nilai Untuk Kriteria Penguasaan TOEFL - C5')
        st.markdown('''
                :red[*]isi dengan <u><b>-1 jika bernilai "Tidak Ada".</b></u>
                <br>
                :red[*]isi dengan <u><b>Nilai Skor TOEFL Yang Dimiliki</b>.</u>
                ''', unsafe_allow_html=True)
        for i in range(int(alt_value)):
            
            master_of_toefl = st.number_input(f"Calon Guru ke-{i + 1}: {alt_name_value[i]}", min_value=-1, value=-1, step=1)

            if master_of_toefl == -1:
                c5 = 1
                alt_penguasaan_toefl = np.append(alt_penguasaan_toefl, c5)
            elif master_of_toefl > 400:
                c5 = 5
                alt_penguasaan_toefl = np.append(alt_penguasaan_toefl, c5)
            elif 300 < master_of_toefl <= 400:
                c5 = 4
                alt_penguasaan_toefl = np.append(alt_penguasaan_toefl, c5)
            elif 200 < master_of_toefl <= 300:
                c5 = 3
                alt_penguasaan_toefl = np.append(alt_penguasaan_toefl, c5)
            else: # 0 <= master_of_toefl < 200
                c5 = 2
                alt_penguasaan_toefl = np.append(alt_penguasaan_toefl, c5)  
        
        
        #
        # C6 : Kriteria Usia
        #
        st.title('Memasukkan Nilai Untuk Kriteria Usia (Tahun) - (C6)')
        st.markdown('''
            :red[*]Nilai minimal usia adalah <u><b>20 Tahun.</b></u>

            ''', unsafe_allow_html=True)
        for i in range(int(alt_value)):

            
            age = st.number_input(f"Calon Guru ke-{i + 1}: {alt_name_value[i]}", min_value=20, value=20, step=1)

            if 20 <= age <= 22:
                c6 = 5
                alt_usia = np.append(alt_usia, c6)
            elif 22 < age <= 24:
                c6 = 4
                alt_usia = np.append(alt_usia, c6)
            elif 24 < age <= 26:
                c6 = 3
                alt_usia = np.append(alt_usia, c6)
            elif 26 < age <= 28:
                c6 = 2
                alt_usia = np.append(alt_usia, c6)
            else: # master_of_toefl > 28
                c6 = 1
                alt_usia = np.append(alt_usia, c6)


        if st.button("Hitung Nilai", type="primary"):
            
            # The output for each value from user input :
            st.markdown('''
                <br>
                <h3>
                Hasil Masing-Masing Nilai Pada Setiap Alternatif Calon Guru Di Setiap Kriteria:  
                </h3>
                <br>''', 
            unsafe_allow_html=True)
            
            # Membuat dataframe
            df_alt_pendidikan_value = pd.DataFrame(alt_pendidikan_value, columns=['Pendidikan'], index=alt_name_value)
            df_alt_pengalaman_value = pd.DataFrame(alt_pengalaman_value, columns=['Pengalman Kerja'], index=alt_name_value)
            df_alt_kemampuan_mengajar = pd.DataFrame(alt_kemampuan_mengajar, columns=['Kemampuan Mengajar'], index=alt_name_value)
            df_alt_penguasaan_conver = pd.DataFrame(alt_penguasaan_conver, columns=['Penguasaan Conversation'], index=alt_name_value)
            df_alt_penguasaan_toefl = pd.DataFrame(alt_penguasaan_toefl, columns=['Penguasaan TOEFL'], index=alt_name_value)
            df_alt_usia = pd.DataFrame(alt_usia, columns=['Usia'], index=alt_name_value)
            
            # Menambahkan nama alternatif pada label indeks
            df_alt_pendidikan_value = df_alt_pendidikan_value.rename_axis('Alternatif', axis=0)
            df_alt_pengalaman_value = df_alt_pengalaman_value.rename_axis('Alternatif', axis=0)
            df_alt_kemampuan_mengajar = df_alt_kemampuan_mengajar.rename_axis('Alternatif', axis=0)
            df_alt_penguasaan_conver = df_alt_penguasaan_conver.rename_axis('Alternatif', axis=0)
            df_alt_penguasaan_toefl = df_alt_penguasaan_toefl.rename_axis('Alternatif', axis=0)
            df_alt_usia = df_alt_usia.rename_axis('Alternatif', axis=0)
            
            #Output :
            st.write('Kriteria Pendidikan - C1 : ', df_alt_pendidikan_value)
            st.write('Kriteria Pengalaman Kerja (Tahun) - C2 : ', df_alt_pengalaman_value)
            st.write('Kriteria Kemampuan Mengajar - C3 : ', df_alt_kemampuan_mengajar)
            st.write('Kriteria Penguasaan Conversation - C4: ', df_alt_penguasaan_conver)
            st.write('Kriteria Penguasaan TOEFL - C5: ', df_alt_penguasaan_toefl)
            st.write('Kriteria Usia (Tahun) - C6 : ', df_alt_usia)
            
            
            #
            # Matriks Keputusan
            #
            
            # Matriks Keputusan
            dataset = np.vstack([alt_pendidikan_value, alt_pengalaman_value, alt_kemampuan_mengajar, alt_penguasaan_conver, alt_penguasaan_toefl, alt_usia]).T
            df_datasets = pd.DataFrame(dataset, columns=['Pendidikan', 'Pengalaman Kerja', 'Kemampuan Mengajar', 'Penguasaan Conversation', 'Penguasaan TOEFL', 'Usia'], index=alt_name_value)
            df_datasets = df_datasets.rename_axis('Alternatif', axis=0)
            st.markdown('''
                <br>
                <h3>
                Matriks Keputusan :  
                </h3>
                <br>''', 
            unsafe_allow_html=True)
            st.write(df_datasets)
            
            
            #
            # Kategori Setiap Kriteria
            #
            
            # Kategori Setiap Kriteria
            st.markdown('''
                <br>
                <h3>
                Kategori Setiap kriteria :  
                </h3>
                <br>''', 
            unsafe_allow_html=True)
            kategori_krit = {
                'Pendidikan': ['Benefit'], 
                'Pengalaman Kerja' : ['Benefit'],
                'Kemampuan Mengajar': ['Benefit'],
                'Penguasaan Conversation': ['Benefit'],
                'Penguasaan TOEFL': ['Benefit'], 
                'Usia': ['Cost']
            }
            df_kategori_krit = pd.DataFrame(kategori_krit)
            st.markdown(df_kategori_krit.to_html(index=False), unsafe_allow_html=True)
            
            #============================================= Start from here for the calc =========================================
            
            #
            # Nilai Maksimum & Nilai Minimum
            #
            
            # Menemukan nilai maksimum dan minimum untuk setiap kolom (C1 hingga C6)
            max_values = np.max(dataset, axis=0)
            df_max_values = pd.DataFrame(max_values, columns=['Nilai Maksimum'], index=['Pendidikan', 'Pengalaman Kerja', 'Kemampuan Mengajar', 'Penguasaan Conversation', 'Penguasaan TOEFL', 'Usia'])
            df_max_values = df_max_values.rename_axis('Kriteria', axis=0)
            
            min_values = np.min(dataset, axis=0)
            df_min_values = pd.DataFrame(min_values, columns=['Nilai Minimum'], index=['Pendidikan', 'Pengalaman Kerja', 'Kemampuan Mengajar', 'Penguasaan Conversation', 'Penguasaan TOEFL', 'Usia'])
            df_min_values = df_min_values.rename_axis('Kriteria', axis=0)
            
            # Show the output
            st.markdown('''
                <br>
                <h3>
                Nilai Maksimum :  
                </h3>
                <br>''', 
            unsafe_allow_html=True)
            st.write(df_max_values)
            
            st.markdown('''
                <br>
                <h3>
                Nilai Minimum :  
                </h3>
                <br>''', 
            unsafe_allow_html=True)
            st.write(df_min_values)
            
            
            #
            # Normalisasi Data
            #
            
            # Memilah Data yang termasuk benefit
            benefit = dataset[:, :5]
            maxval_ben = max_values[:5]

            # Memilah Data yang termasuk cost
            cost = dataset[:, -1]
            minval_cost = min_values[-1]
            
            # Normalisasi Data
            matriks_ben = benefit/maxval_ben
            matriks_cost = minval_cost/cost
            
            normData = np.concatenate((matriks_ben, matriks_cost.reshape(-1, 1)), axis=1)
            df_normData = pd.DataFrame(normData, columns=['Pendidikan', 'Pengalaman Kerja', 'Kemampuan Mengajar', 'Penguasaan Conversation', 'Penguasaan TOEFL', 'Usia'], index=alt_name_value)
            df_normData = df_normData.rename_axis('Alternatif', axis=0)
            
            st.markdown('''
                <br>
                <h3>
                Normalisasi Data :  
                </h3>
                <br>''', 
            unsafe_allow_html=True)
            st.write(df_normData)
            
            #============================================= Menentukan Nilai Bobot Untuk Setiap Kriteria =========================================
            st.markdown('''
                <hr>
                <br>
                <h2>
                Menentukan Nilai Bobot Untuk Setiap Kriteria
                </h2>
                ''', 
            unsafe_allow_html=True)
            
            
            #
            # NIlai Rata-rata dari normalisasi data
            #
            
            # Mencari Nilai rata-rata
            ratarata = np.mean(normData, axis=0)
            df_ratarata = pd.DataFrame(ratarata, columns=['Rata-Rata'], index=['Pendidikan', 'Pengalaman Kerja', 'Kemampuan Mengajar', 'Penguasaan Conversation', 'Penguasaan TOEFL', 'Usia'])
            df_ratarata = df_ratarata.rename_axis('Kriteria', axis=0)
            
            st.markdown('''
                <h3>
                Nilai Rata-Rata Dari Matriks Normalisasi Data :  
                </h3>
                <br>''', 
            unsafe_allow_html=True)
            st.write(df_ratarata)
            
            
            #
            # NIlai Variasi Preferensi
            #
            
            # Mencari nilai matriks variasi preferensi
            VarPref = np.array((normData - ratarata)**2)
            VarPref_rounded = np.round(VarPref, decimals=4)
            df_VarPref_rounded = pd.DataFrame(VarPref_rounded, columns=['Pendidikan', 'Pengalaman Kerja', 'Kemampuan Mengajar', 'Penguasaan Conversation', 'Penguasaan TOEFL', 'Usia'], index=alt_name_value)
            df_VarPref_rounded = df_VarPref_rounded.rename_axis('Alternatif', axis=0)
            
            st.markdown('''
                <br>
                <h3>
                Matriks Nilai Variasi Preferensi :  
                </h3>
                <br>''', 
            unsafe_allow_html=True)
            st.write(df_VarPref_rounded)
            
            totvarpref = np.sum(VarPref_rounded, axis=0)
            df_totvarpref = pd.DataFrame(totvarpref, columns=['Total Nilai Variasi Preferensi'], index=['Pendidikan', 'Pengalaman Kerja', 'Kemampuan Mengajar', 'Penguasaan Conversation', 'Penguasaan TOEFL', 'Usia'])
            df_totvarpref = df_totvarpref.rename_axis('Kriteria', axis=0)
            
            st.markdown('''
                <br>
                <h3>
                Hasil Dari Penjumlahan Matriks Variasi Preferensi :  
                </h3>
                <br>''', 
            unsafe_allow_html=True)
            st.write(df_totvarpref)
            
            #
            # Penyimpangan Dalam Nilai Preferensi
            #
            
            # Mencari Penyimpangan Dalam Nilai Preferensi
            Inpref = np.array(1 - totvarpref)
            df_Inpref = pd.DataFrame(Inpref, columns=['Penyimpangan Dalam Nilai Preferensi'], index=['Pendidikan', 'Pengalaman Kerja', 'Kemampuan Mengajar', 'Penguasaan Conversation', 'Penguasaan TOEFL', 'Usia'])
            df_Inpref = df_Inpref.rename_axis('Kriteria', axis=0)
            
            st.markdown('''
                <br>
                <h3>
                Matriks Penyimpangan Dalam Nilai Preferensi :  
                </h3>
                <br>''', 
            unsafe_allow_html=True)
            st.write(df_Inpref)
            
            # Menghitung Total Penyimpangan Dalam Nilai Preferensi
            totinpref = np.sum(Inpref)
            totinpref_r4 = np.round(totinpref, decimals=4)
            st.write(f'Total Penyimpangan Dalam Nilai Preferensi: {totinpref_r4}')
            
            
            #
            # Nilai Bobot pada masing-masing kriteria
            #
            
            # Menentukan Nilai Bobot pada masing-masing kriteria
            kriteriabobot = np.array(Inpref/totinpref)
            bobot_kriteria = np.round(kriteriabobot, decimals=4)
            df_bobot_kriteria = pd.DataFrame(bobot_kriteria, columns=['Nilai Bobot'], index=['Pendidikan', 'Pengalaman Kerja', 'Kemampuan Mengajar', 'Penguasaan Conversation', 'Penguasaan TOEFL', 'Usia'])
            df_bobot_kriteria = df_bobot_kriteria.rename_axis('Kriteria', axis=0)
            
            st.markdown('''
                <br>
                <h3>
                Kriteria Bobot Pada Masing-Masing Kriteria :  
                </h3>
                <br>''', 
            unsafe_allow_html=True)
            st.write(df_bobot_kriteria)
            
            
            #============================================= Menghitung Nilai Preference Selection Index =========================================
            st.markdown('''
                <br>
                <h2>
                Menghitung Nilai Preference Selection Index
                </h2>
                ''', 
            unsafe_allow_html=True)
            #
            # Nilai Preference Alternative
            #
            
            # Preference Alternative 
            prefalter = np.array(normData * bobot_kriteria)
            prefalter_r4 = np.round(prefalter, decimals=4)
            df_prefalter_r4 = pd.DataFrame(prefalter_r4, columns=['Pendidikan', 'Pengalaman Kerja', 'Kemampuan Mengajar', 'Penguasaan Conversation', 'Penguasaan TOEFL', 'Usia'], index=alt_name_value)
            df_prefalter_r4 = df_prefalter_r4.rename_axis('Alternatif', axis=0)
            
            st.markdown('''
                <h3>
                Matriks Preference Selection Index :
                </h3>
                <br>''', 
            unsafe_allow_html=True)
            st.write(df_prefalter_r4)

            #============================================= Mencari Nilai Perangkingan Untuk Masing-masing alternatif =========================================
            
            #
            # Nilai Perangkingan Untuk Masing-masing alternatif
            #
            
            # Mencari Nilai Perangkingan Untuk Masing-masing alternatif
            rank = np.sum(prefalter_r4, axis=1)
            rank_r4 = np.round(rank, decimals=4)
            df_rank_r4 = pd.DataFrame(rank_r4, columns=['Nilai Perangkingan'], index=alt_name_value)
            df_rank_r4 = df_rank_r4.rename_axis('Alternatif', axis=0)
            
            st.markdown('''
                <br>
                <h3>
                Nilai Perangkingan Untuk Masing-Masing Alternatif :
                </h3>
                <br>''', 
            unsafe_allow_html=True)
            st.write("Hasil sebelum diurutkan :")
            st.write(df_rank_r4)
            
            # Menggabungkan alt_name_value dan rank_r4 menjadi numpy array
            result_array = np.column_stack((alt_name_value, rank_r4))

            # Mendapatkan indeks yang mengurutkan array dari nilai terbesar ke terkecil
            sorted_indices = np.argsort(result_array[:, 1])[::-1]

            # Menggunakan indeks untuk mengurutkan result_array
            result_array_sorted = result_array[sorted_indices]
            df_result_array_sorted = pd.DataFrame(result_array_sorted, columns=['Alternatif', 'Nilai Perangkingan'])
      
            st.write("Hasil setelah diurutkan :")
            st.markdown(df_result_array_sorted.to_html(index=False), unsafe_allow_html=True)
            
            st.markdown("<hr/>", unsafe_allow_html=True)
            #============================================= Kesimpulan =========================================
            
            # Proses pemilihan sejumlah guru bahasa inggris dari total kandidat yang tersedia
            alt_terpilih = int((jum_alternatif/alt_value) * alt_value)
            
            alt_names_only = ', '.join(result_array_sorted[:alt_terpilih, 0])  

            alt_names = result_array_sorted[:alt_terpilih, 0]
            rank_values = result_array_sorted[:alt_terpilih, 1]
            # Menyusun hasil dalam format yang diinginkan
            selected_alt_names_only = alt_names_only
            selected_rank_values = ', '.join([f'{name} = {value}' for name, value in zip(alt_names, rank_values)])

            st.write(f'''Dari perhitungan yang telah dilakukan dapat dilihat bahwa {selected_rank_values} memiliki nilai terbesar, 
                        sehingga dapat disimpulkan bahwa {selected_alt_names_only} yang akan dipilih 
                        sebagai guru bahasa inggris untuk tingkat sekolah dasar yang diterima di Sekolah Dasar (SD) Ceria 1.'''
            )
            
            
